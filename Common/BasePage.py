'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

import time

import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.conf_dirs import screen_dir
from Utils.HandleLoggingNew import HandleLogger
from selenium.common.exceptions import NoSuchElementException

# 创建日志收集器对象
logger = HandleLogger().get_logger()
# 获取当前执行系统时间
curTime = time.strftime("%Y-%m-%d_%H-%M")


class BasePage(object):
    '''
            封装appium操作app通用的方法
    '''

    def __init__(self, driver):
        self.driver = driver

    def force_wait_element(self, locator, timeout=30, frequcy=0.5):
        '''强制等待元素'''
        use_time = 0
        while use_time < timeout:
            try:
                e = self.get_element(locator)
                time.sleep(frequcy)
                return e
            except NoSuchElementException:
                time.sleep(frequcy)
                use_time += frequcy
        logger.error("等待元素：{},超时等待!!!".format(locator[1]))
        self.save_screenshots_png()
        raise NoSuchElementException

    def wait_eleVisisble(self, locator, wait_time=30):
        '''显示等待元素可见'''
        WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator))

    def wait_elePresence(self, locator, wait_time=30):
        '''显示等待元素存在'''
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator))

    def wait_eleClickable(self, locator, wait_time=30):
        '''显示等待元素可点击'''
        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator))

    def get_element(self, locator, wait_time=30):
        '''查找元素并返回'''
        by, loc = locator
        if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
            logger.error("{}元素定位方法不存在！".format(by))
            raise TypeError
        try:
            self.wait_eleVisisble(locator, wait_time)
            ele = self.driver.find_element(*locator)
        except:
            logger.error("{}元素不可见".format(loc))
            self.save_screenshots_png()
            raise NoSuchElementException
        else:
            return ele

    def get_elements(self, locator, wait_time=30):
        '''查找元素并返回多个元素'''
        by, loc = locator
        if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
            logger.info("{}元素定位方法不存在！".format(by))
        try:
            self.wait_eleVisisble(locator, wait_time)
            eles = self.driver.find_elements(*locator)
        except:
            logger.error("{}元素不可见!".format(loc))
            self.save_screenshots_png()
            raise NoSuchElementException
        else:
            return eles

    def get_elements_by_one(self, locator, wait_time=30):
        '''查找元素并返回多个元素'''
        by, loc = locator
        if by not in By.__dict__.values() and by not in MobileBy.__dict__.values():
            logger.info("{}元素定位方法不存在！".format(by))
        try:
            self.wait_eleVisisble(locator, wait_time)
            eles = self.driver.find_elements(*locator)
        except:
            logger.error("{}元素未找到!".format(loc))
            self.save_screenshots_png()
            raise NoSuchElementException
        else:
            return eles[0]

    def save_screenshots_png(self):
        '''截图保存'''
        filename = screen_dir + "/images_{}.png".format(curTime)
        self.driver.save_screenshot(filename)
        with open(filename, 'rb') as f:
            file = f.read()
        allure.attach(
            file, "失败截图时间：{}".format(curTime), allure.attachment_type.PNG)

    def get_toast_content(self, locator, wait_time=30):
        '''获取toast弹出框的文本内容'''
        try:
            self.wait_elePresence(locator, wait_time)
            toast_content = self.driver.find_element(*locator).text
        except:
            logger.error("%s,元素未出现!!!" % locator)
            self.save_screenshots_png()
            return NoSuchElementException
        else:
            return toast_content

    def switch_to_webview(self):
        '''切换上下文context，进入webview内置H5页面'''
        contexts = self.driver.contexts
        if contexts[-1].startswith("WEBVIEW_"):
            self.driver.switch_to.context(contexts[-1])
        else:
            logger.error("当前操作页仍是NATIVE_APP")
            raise

    def switch_to_native(self):
        '''用于操作完webview需要返回到原生app'''
        self.driver.switch_to.context("NATIVE_APP")

    def always_allow(self, number=3):
        """
            fuction:权限弹窗-允许
            args:1.传driver
            2.number，判断弹窗次数，默认给4次
                              其它：WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
        """
        while number:
            loc = "//*[@text='允许']"
            try:
                e = self.wait_elePresence(MobileBy.XPATH, loc)
                e.click()
            except:
                logger.info("没有找到该元素：{}".format(loc))
                break


class BaseAction:
    KEYCODE_ENTER = 66
    KEYCODE_BACK = 4

    def __init__(self, driver):
        self.driver = driver

    def app_back(self):
        '''返回：替换keyevent方法，测试可能不支持h5返回'''
        self.driver.press_keycode(self.KEYCODE_BACK)

    def app_enter(self):
        '''回车'''
        self.driver.press_keycode(self.KEYCODE_ENTER)

    def find_eles_by_page(self, text):
        '''从当前页面获取元素,向上滑动，查找元素'''
        old_page = None
        new_page = self.driver.page_source
        title = []
        while old_page != new_page:
            eles = self.driver.find_elements(
                by=MobileBy.XPATH, value="//*[contains(@text,'{}')]".format(text))
            for ele in eles:
                title.append(ele)
                if text == ele.text:
                    return ele
            self.swipe_up()
            old_page = new_page
            new_page = self.driver.page_source
        logger.error("{}:文本未找到!!!".format(text))

    def find_ele_by_page(self, text):
        '''翻页查找文本'''
        old_page = ''
        new_page = self.driver.page_source
        while old_page != new_page:
            try:
                ele = self.driver.find_element(
                    by=MobileBy.XPATH, value="//*[contains(@text,'{}')]".format(text))
                return ele
            except:
                self.swipe_up()
                old_page = new_page
                new_page = self.driver.page_source
        logger.error("{}:文本未找到!!!".format(text))
        raise RuntimeError("运行时异常!!!")

    def find_pageElement_by_uiselector(self, text, times=5):
        '''翻页查找，匹配标题'''
        old_page = None
        new_page = self.driver.page_source
        while old_page != new_page:
            try:
                ele = self.driver.find_element_by_android_uiautomator(
                    'new UiScrollable().scrollIntoView(new UiSelector().textMatches("{}").instance(0))'.format(text))
                return ele
            except:
                self.swipe_up()
                old_page = new_page
                new_page = self.driver.page_source
        logger.error("{}:文本未找到!!!".format(text))

    @property
    def width(self):
        '''获取屏幕宽度'''
        return self.driver.get_window_size()['width']

    @property
    def height(self):
        '''获取屏幕高度'''
        return self.driver.get_window_size()['height']

    def get_screen_size(self):
        '''获取当前屏幕大小'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipe_left(self, duration=500):
        '''
                    向左滑动
        duration:滑动屏幕等待时间
                    向左:y坐标不变,x坐标由大及小
                    向右:y坐标不变,x坐标由小及大
                    向上:x坐标不变,y坐标由大及小
                    向下:x坐标不变,y坐标由小及大
        '''
        self.driver.swipe(self.width * 0.75, self.height *
                          0.5, self.width * 0.25, self.height * 0.5, duration)

    def swipe_right(self, duration=500):
        '''右滑屏'''
        self.driver.swipe(self.width * 0.1, self.height *
                          0.5, self.width * 0.9, self.height * 0.5, duration)

    def swipe_up(self, duration=500):
        '''向上滑屏'''
        self.driver.swipe(self.width * 0.5, self.height *
                          0.75, self.width * 0.5, self.height * 0.25, duration)

    def swipe_down(self, duration=500):
        '''向下滑屏'''
        self.driver.swipe(self.width * 0.5, self.height *
                          0.1, self.width * 0.5, self.height * 0.9, duration)

    def zoom(self, scale):
        '''放大，scale倍数'''
        multiaction = MultiAction(self.driver)
        finger_1 = TouchAction(self.driver)
        finger_1.press(self.width() / 2, self.height() / 2).wait(
            200).move_to(self.width() / 2 - self.width() * scale / 2, self.height() / 2).release()
        finger_2 = TouchAction(self.driver)
        finger_2.press(self.width() / 2, self.height() / 2).wait(
            200).move_to(self.width() / 2 + self.width() * scale / 2, self.height() / 2).release()
        multiaction.add(finger_1, finger_2)
        multiaction.perform()

    def pinch(self, scale):
        '''
                    缩小
        scale:倍数
        '''
        multiaction = MultiAction(self.driver)
        finger_1 = TouchAction(self.driver)
        finger_1.press(self.width() / 2 - self.width() * scale / 2, self.height() / 2).wait(
            200).move_to(self.width() / 2, self.height() / 2).release()
        finger_2 = TouchAction(self.driver)
        finger_2.press(self.width() / 2 + self.width() * scale / 2, self.height() / 2).wait(
            200).move_to(self.width() / 2, self.height() / 2).release()
        multiaction.add(finger_1, finger_2)
        multiaction.perform()

    def dubble_click(self, ele=None, x=None, y=None):
        """双击"""
        ac = TouchAction(self.driver)
        ac.press(ele=None, x=None, y=None).wait(200).release().wait(
            200).press(ele=None, x=None, y=None).wait(200).release().perform()

    def single_click(self, ele=None, x=None, y=None):
        """单击"""
        ac = TouchAction(self.driver)
        ac.tap(ele=None, x=None, y=None).release().perform()

    def gesture_unlocking(self, ele, location: list):
        """绘制九宫格
        location=[1,2,3,4]
        """
        if len(location) < 5:
            raise ValueError("at least need four elements")
        action = TouchAction(self.driver)
        size = ele.rect()
        points = [
            {"x": size['x'] + size['width'] / 6 * 1,
             'y': size['y'] + size['height'] / 6},
            {"x": size['x'] + size['width'] / 6 * 3,
             'y': size['y'] + size['height'] / 6},
            {"x": size['x'] + size['width'] / 6 * 5,
             'y': size['y'] + size['height'] / 6},
            {"x": size['x'] + size['width'] / 6 * 1,
             'y': size['y'] + size['height'] / 6 * 3},
            {"x": size['x'] + size['width'] / 6 * 3,
             'y': size['y'] + size['height'] / 6 * 3},
            {"x": size['x'] + size['width'] / 6 * 5,
             'y': size['y'] + size['height'] / 6 * 3},
            {"x": size['x'] + size['width'] / 6 * 1,
             'y': size['y'] + size['height'] / 6 * 5},
            {"x": size['x'] + size['width'] / 6 * 3,
             'y': size['y'] + size['height'] / 6 * 5},
            {"x": size['x'] + size['width'] / 6 * 5, 'y': size['y'] + size['height'] / 6 * 5}]
        action.press(**points[location[0] - 1]).wait(200)
        for point in location[1:]:
            action.move_to(**points[point - 1]).wait(200)
        action.release().perform()
