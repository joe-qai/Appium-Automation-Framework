'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'


from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage


class StudyAbroadPage(BasePage):
    '''
            元素定位内属性
    '''

    # 留学tab
    abroad_tab = (MobileBy.XPATH, "//android.widget.TextView[(@text='留学')]")

    def click_abroad_tab(self):
        '''点击留学tab'''
        self.get_element(self.abroad_tab).click()
