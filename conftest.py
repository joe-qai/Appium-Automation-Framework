'''
# -*- encoding=utf-8 -*-
'''
import os

import pytest
import yaml

from Common.BaseDriver import BaseDriver
from Common.conf_dirs import caps_dir
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from PageObjects.welcome_page import WelcomePage
from TestDatas.user_login_mobile import login_success
from Utils.HandleLoggingNew import logger

__author__ = 'Joe'

# 如果需要多设备依次进行,在列表中追加即可:,"XiaoYao","HongMi"
params = ["RedMi"]
# 如果需要多设备并发进行，可能需要使用多线程或者selenium gird分布式

with open(caps_dir + "/desired_caps.yaml", encoding="utf-8") as fs:
    devices = yaml.load(fs, Loader=yaml.FullLoader)
    for device in devices:
        for param in params:
            if param == device['deviceDesc']:
                # 读出被测引用的packagename用于adb命令卸载
                packageName = device.get("desired_caps").get("appPackage")
                # 读取启动appium-server的端口用于关闭appium服务
                port = device.get("server_port")


@pytest.fixture(params=params, scope='class')
def login_driver(request):
    '''需要先登录再执行其他测试用例'''
    driver = BaseDriver().base_driver(device=request.param)
    is_second_welcome(driver)
    # is_login_ok(driver)
    yield driver
    # driver.close_app()
    # driver.remove_app(packageName)
    driver.quit()


@pytest.fixture(params=params, scope='class')
def common_driver(request):
    '''需要先登录再执行其他测试用例'''
    driver = BaseDriver().base_driver(device=request.param)
    is_second_welcome(driver)
    yield driver
    driver.close_app()
    stop_appium()
    driver.quit()


@pytest.fixture(params=params, scope='class')
def nologin_driver(request):
    '''不需要先登录再执行其他测试用例'''
    driver = BaseDriver().base_driver(device=request.param)
    is_welcome(driver)
    yield driver
    driver.close_app()
    driver.remove_app(packageName)
    driver.quit()


@pytest.fixture(params=params, scope='module')
def uiauto_login_driver(request):
    '''登录：重置; 需要UIAutomator2正则匹配来定位toast弹出框'''
    driver = BaseDriver().base_driver(
        device=request.param, automationName="UIAutomator2")
    is_welcome(driver)
    is_login_ok(driver)
    yield driver
    driver.close_app()
    driver.remove_app(packageName)
    driver.quit()


def stop_appium():
    """释放指定的appium服务端口"""
    cmd_find = 'netstat -aon | findstr %s' % port
    result = os.popen(cmd_find).read().split()[-1]
    if result:
        cmd_kill = 'taskkill -f -pid %s' % result
        os.popen(cmd_kill)
        logger.info('port %s is closed !' % port)
    else:
        logger.info('port %s is available !' % port)


def is_welcome(driver):
    """
      判断当前页面是否是欢迎页
      启动页后面就是WelcomeActivity欢迎页面
    """
    cur_activity = driver.current_activity
    if cur_activity.endswith("SplashActivity"):
        WelcomePage(driver).click_agree()
        WelcomePage(driver).swipe_screen()


def is_second_welcome(driver):
    """
      判断当前页面是否是欢迎页
      启动页后面就是WelcomeActivity欢迎页面
    """
    cur_activity = driver.current_activity
    if cur_activity.endswith("CheckPermissionActivity"):
        WelcomePage(driver).agree_use()


def is_login_ok(driver):
    '''
    判断是否登录页面<启动页面activity>
     获取当前app的activity类来判断是否是登录页
    也就是说,如果是登录页必定调用一次登录app的方法
    '''
    IndexPage(driver).click_head_image()
    cur_activity = driver.current_activity
    if cur_activity.find("LoginActivity"):
        login_app(driver)
    else:
        IndexPage(driver).back_for_index()
        logger.info("用户已登录当前APP")


def login_app(driver):
    '''
    先触发一个必定登录的事件,判断是否跳转到登录页面,然后再进行登录操作,否则
    '''
    LoginPage(driver).click_passwdLogin()
    LoginPage(driver).click_country_area()
    LoginPage(driver).search_country_area(login_success.get('country'))
    LoginPage(driver).selected_area_number()
    LoginPage(driver).input_mobile(login_success.get('mobile'))
    LoginPage(driver).input_passwd_and_login(login_success.get('passwd'))
    # assert IndexPage(driver).get_login_success_toast()


def pytest_sessionfinish(session):
    '''
    这个hook函数的原理是在allure生成的结果文件目录创建一个environment.properties配置文件
    在allure生成报告的时候会将该配置文件的的信息写入allure测试报告中展示；
    session其实也是个fixture，session.config.rootdir获取工程根目录
    '''
    with open("{}/allure-results/environment.properties".format(session.config.rootdir), "w") as f:
        f.write("browser=chromedriver\nbackend=test\ndomain=ieltsbro")
