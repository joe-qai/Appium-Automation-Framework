'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage


class ExamPage(BasePage):
    '''
    classdocs元素定义内属性
    '''

    # 发布回忆
    send_memory_button = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/tvEditMemory")
    # 考试tab
    exam_menu = (
        MobileBy.XPATH, "//android.widget.TextView[contains(@text,'考试')]")

    def click_index(self):
        '''点击考试tab'''
        self.get_element(self.exam_menu).click()

    def click_send_exam_memory(self):
        '''点击发布回忆按钮'''
        self.get_element(self.send_memory_button).click()
