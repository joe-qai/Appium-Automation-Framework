'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage


class LoginPage(BasePage):
    '''元素定位'''
    # 登录页面：密码登录
    passwd_login = (
        MobileBy.XPATH, "//android.widget.TextView[contains(@text,'密码登录')]")
    # 下一步
    next_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/btnLoginNext")
    # 输入手机号码 框
    input_phoneNumber = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/etMobileNum")
    # 输入密码框
    input_passwd = (MobileBy.ID, "com.chutzpah.yasibro.test:id/et_password")
    # 登录按钮
    login_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/btnLoginNext")
    # 取消登录<左上角的x>
    cancel_login = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivCancel")
    # 国别区号
    country_area = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/phone_area_text_view")
    # 国别码搜索框
    search_block = (
        MobileBy.ID, 'com.chutzpah.yasibro.test:id/search_edit_text')
    # 国别码列表选择
    selected_area = (MobileBy.XPATH, "//android.widget.TextView[@text='中国']")

    def click_passwdLogin(self):
        '''点击密码登录'''
        self.get_element(self.passwd_login).click()

    def click_cancel_login(self):
        '''点击取消登录'''
        self.get_element(self.cancel_login).click()

    def click_country_area(self):
        '''点击国别码选择'''
        self.get_element(self.country_area).click()

    def search_country_area(self, country):
        '''搜索国家地区'''
        self.get_element(self.search_block).send_keys(country)

    def selected_area_number(self):
        '''选择国别码'''
        self.get_element(self.selected_area).click()

    def input_mobile(self, mobile):
        '''输入手机号'''
        self.get_element(self.input_phoneNumber).send_keys(mobile)

    def input_passwd_and_login(self, passwd):
        '''输入密码并点击登录'''
        self.get_element(self.input_passwd).send_keys(passwd)
        self.get_element(self.login_button).click()
