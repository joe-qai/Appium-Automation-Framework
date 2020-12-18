'''
# -*- encoding=utf-8 -*-
Created on 2020年8月28日上午10:22:28
@author: Joe
@file:PageObjects.studyRecoding_page.py
'''
from appium.webdriver.common.mobileby import MobileBy
from Common.BasePage import BasePage


__author__ = "Joe"


class StudyRecodingPage(BasePage):
    '''
    classdocs
    '''

    # 元素定位
    # 返回按钮
    back_button = (
        MobileBy.XPATH, '//android.view.View[@resource-id="com.chutzpah.yasibro.test:id/baseToolBar"]/android.widget.ImageView[1]')

    # 写作记录
    write_recoding = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("写作").instance(0)')

    # 阅读记录
    read_recoding = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("阅读").instance(0)')

    # 口语记录
    ocal_recoding = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("口语").instance(0)')
