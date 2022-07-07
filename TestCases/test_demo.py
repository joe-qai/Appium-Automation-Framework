'''
# -*- encoding=utf-8 -*-
'''
import time

import allure
import pytest

from PageObjects.exam_page import ExamPage
from PageObjects.goToClass_page import GoToClassPage
from PageObjects.index_page import IndexPage
from PageObjects.login_page import LoginPage
from TestDatas.user_login_mobile import login_success

__author__ = 'Joe'


class TestDemo():
    '''测试样例'''

    @pytest.mark.skip(reason="启动app即登录,测试用例的登录操作步骤已无效")
    @allure.feature("首次进入app,发布回忆按钮触发登录")
    def test_first_exam(self, login_driver):
        with allure.step("默认进入考试tab:点击发布回忆按钮"):
            ExamPage(login_driver).click_send_exam_memory()

        with allure.step("点击密码登录:输入账号密码"):
            LoginPage(login_driver).click_passwdLogin()
            LoginPage(login_driver).input_mobile(
                login_success['mobile'])
            LoginPage(login_driver).input_passwd(login_success["passwd"])
            time.sleep(3)

    @pytest.mark.skip(reason="调试已登录,首页进入个人中心,已经无需登录操作步骤")
    @allure.feature("点击首页,扫一扫触发登录")
    def test_personal_info(self, login_driver):
        with allure.step("点击首页:扫一扫"):
            IndexPage(login_driver).click_index()
            IndexPage(login_driver).click_scan()
        with allure.step("点击密码登录:输入账号密码"):
            LoginPage(login_driver).click_passwdLogin()
            LoginPage(login_driver).input_mobile(
                login_success['mobile'])
            LoginPage(login_driver).input_passwd(login_success["passwd"])
            time.sleep(2)

    def test_click_class(self, login_driver):
        GoToClassPage(login_driver).click_class()
        time.sleep(3)
