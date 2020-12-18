'''
# -*- encoding=utf-8 -*-
Created on 2020年8月28日上午9:59:32
@author: Joe
@file:PageObjects.userCollect_page.py
'''
from appium.webdriver.common.mobileby import MobileBy
from Common.BasePage import BasePage

__author__ = "Joe"


class UserCollectPage(BasePage):
    '''
    classdocs：    收藏页tab标题切换，数据展示，点击数据跳转，并返回
    '''

    # 元素定位
#     返回按钮
    back_button = (
        MobileBy.XPATH, '//android.view.View[@resource-id="com.chutzpah.yasibro.test:id/baseToolBar"]/android.widget.ImageView[1]')

    # 全部
    total_collect = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("全部")')
    # 推文
    push_article = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("推文")')
    # 口语话题
    oral_topic = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("口语话题")')
    # 口语录音
    oral_recoding = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("口语录音")')
    # 口语回忆
    oral_memory = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("口语回忆")')
    # 笔试回忆
    write_memory = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvTitle").text("笔试回忆")')

    # 口语录音标签
    oral_recoding_tag = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvInfoType").text("口语录音")')

    # 口语话题标签
    oral_topic_tag = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvInfoType").text("口语话题")')
