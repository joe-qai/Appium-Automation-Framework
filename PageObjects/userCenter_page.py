'''
# -*- encoding=utf-8 -*-
Created on 2020年8月24日下午5:31:12
@author: Joe
@file:PageObjects.userCenter_page.py
'''
from appium.webdriver.common.mobileby import MobileBy
from Common.BasePage import BasePage

__author__ = "Joe"


class UserCenterPage(BasePage):
    '''
    classdocs
    '''

    # 元素定位
    # 个人中心头像
    head_image = (
        MobileBy.XPATH, "//androidx.drawerlayout.widget.DrawerLayout[1]/android.view.View[2]/android.widget.FrameLayout[@resource-id='com.chutzpah.yasibro.test:id/ivHeader']")

    # 用户名
    user_name = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvName")

    # 粉丝
    fans = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llFans")

    # 关注
    attention = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llFollow")

    # 收藏
    collect = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llCollect")

    # 练习
    practise = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llPractice")

    # 学习记录
    study_recode = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvLearnRecord")

    # 我的回忆
    my_memory = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMyMemories")

    # 我的主页
    my_homePage = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMyHomePage")

    # 我的权益
    my_rights = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMyBought")

    # 我的留学
    my_abroad = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMyAbroad")

    # 我的笔记
    my_notes = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMyNote")

    # 消息中心
    msg_center = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMessageCenter")

    # 推荐朋友
    share_friend = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvShareFriend")

    # 设置
    settings = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvSetting")

    # 帮助
    helping = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvHelp")

    # 原生<返回
    back_button = (MobileBy.CLASS_NAME, "android.widget.ImageView")

    # 个人主页<返回
    native_back_x = (
        MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.ImageView[1]")

    def click_headImage(self):
        '''点击头像进入主页'''
        self.get_element(self.head_image).click()

    def click_userName(self):
        '''点击用户名'''
        self.get_element(self.user_name).click()

    def click_fans(self):
        '''点击粉丝'''
        self.get_element(self.fans).click()

    def click_atten(self):
        '''点击关注'''
        self.get_element(self.attention).click()

    def click_collect(self):
        '''点击收藏'''
        self.get_element(self.collect).click()

    def click_practise(self):
        '''点击练习'''
        self.get_element(self.practise).click()

    def click_studyRecode(self):
        '''点击学习记录'''
        self.get_element(self.study_recode).click()

    def click_myMemory(self):
        '''点击我的回忆'''
        self.get_element(self.my_memory).click()

    def click_homePage(self):
        '''点击我的主页'''
        self.get_element(self.my_homePage).click()

    def click_myRights(self):
        '''点击我的权益'''
        self.get_element(self.my_rights).click()

    def click_myAbroad(self):
        '''点击我的权益'''
        self.get_element(self.my_abroad).click()

    def click_myNotes(self):
        '''点击我的笔记'''
        self.get_element(self.my_notes).click()

    def click_msgCenter(self):
        '''点击消息中心'''
        self.get_element(self.msg_center).click()

    def click_shareFriend(self):
        '''点击推荐朋友'''
        self.get_element(self.share_friend).click()

    def click_settings(self):
        '''点击设置'''
        self.get_element(self.settings).click()

    def click_helper(self):
        '''点击帮助'''
        self.get_element(self.helping).click()
