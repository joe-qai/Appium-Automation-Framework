'''
# -*- encoding=utf-8 -*-
'''
from appium.webdriver.common.mobileby import MobileBy

__author__ = 'Joe'

import time

from Common.BasePage import BasePage, BaseAction
from Utils.HandleLoggingNew import HandleLogger

logger = HandleLogger().get_logger()


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
