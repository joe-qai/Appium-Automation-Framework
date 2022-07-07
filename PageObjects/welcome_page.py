'''
# -*- encoding=utf-8 -*-
'''

import time

from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage, BaseAction

__author__ = 'Joe'


class WelcomePage(BasePage, BaseAction):
    ''' 元素,定义为内属性'''

    # 启动页<bu同意>
    disagress = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvCancel")
    # 启动页<同意>
    agree_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvSure")
    # 体验之旅
    welcome = (MobileBy.ID, "com.chutzpah.yasibro.test:id/enter_app_button")
    # 第二次启动还有一个欢迎页
    skip_welcome = (MobileBy.ID, "com.chutzpah.yasibro.test:id/skip_text_view")

    agree_button2 = (MobileBy.XPATH, "//android.widget.TextView[@resource-id='com.chutzpah.yasibro:id/agreeTextView']")

    def agree_use(self):
        '''同意协议与政策'''
        self.get_element(self.agree_button2).click()

    def skip_second_welcome(self):
        '''非滑屏启动页，直接跳过'''
        self.get_element(self.skip_welcome).click()

    def click_agree(self):
        '''点击同意'''
        self.get_element(self.agree_button).click()

    def swipe_screen(self, times=5):
        '''滑屏操作'''
        for i in range(times):
            self.swipe_left()
            time.sleep(i * 0.25)
        self.get_element(self.welcome).click()
