'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'


from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage


class PracticesPage(BasePage):
    '''
            元素定义为内属性
    '''
    # 练习tab
    practice_tab = (MobileBy.XPATH, "//android.widget.TextView[(@text='练习')]")

    def click_practice_tab(self):
        '''点击练习tab'''
        self.get_element(self.practice_tab).click()
