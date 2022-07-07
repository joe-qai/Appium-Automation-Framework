'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage


class GoToClassPage(BasePage):
    class_tab = (MobileBy.XPATH, "//android.widget.TextView[contains(@text,'直播')]")

    def click_class(self):
        self.get_element(self.class_tab).click()