'''
Created on 2020年8月20日

@author: qguan
'''
from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage, BaseAction
from Utils.HandleLoggingNew import HandleLogger

__author__ = "Joe"

logger = HandleLogger().get_logger()


class SearchPage(BasePage, BaseAction):
    '''
    classdocs：元素定义内属性
    '''
    # 搜索框
    search_bar = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llSearch")
    # 搜索输入框
    input_search = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/search_edit_text")

    # 选择其中一个时事热点
    hotpoint = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/tvHotTitle").instance(1)')

    # 取消/关注牛人
    antention_superman_x = (MobileBy.ANDROID_UIAUTOMATOR,
                            'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/baseTvState").instance(1)')
    # 推荐牛人头像
    superman_image = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/ivHeader").instance(1)')

    # <原生返回
    native_back_u = (MobileBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().className("android.widget.ImageView").instance(1)')
    native_back_x = (
        MobileBy.XPATH, "//android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.view.View[1]/android.widget.ImageView[1]")

    # <H5返回，需要切换上下文操作h5返回
    h5_back_x = (MobileBy.XPATH, "//*//div[@class='navigation_bar_left']")

    # 清空搜索内容，返回搜索页面
    clear_search = (MobileBy.ID, "com.chutzpah.yasibro.test:id/img_clear")

    # 取消搜索返回首页
    cancel_search = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/cancel_text_view")

    # 取消/关注朋友&点击头像元素通用

    # 清楚搜索历史记录
    clear_history = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivDelete")

    def clear_search_text(self):
        '''清空搜索内容'''
        self.get_element(self.clear_search).click()

    def clear_history_text(self):
        '''清空历史搜索内容'''
        self.get_element(self.clear_history).click()

    def cancel_search_x(self):
        '''取消搜索'''
        self.get_element(self.cancel_search).click()

    def input_content(self, content):
        '''输入内容并回车搜索'''
        self.get_element(self.input_search).send_keys(content)
        self.app_enter()

    def enter_search_page(self):
        '''点击搜索框进入搜索页面'''
        self.get_element(self.search_bar).click()

    def antention_superman(self):
        '''取消/关注牛人'''
        self.get_element(self.antention_superman_x).click()

    def enter_superman_page(self):
        '''点击牛人头像进入牛人主页'''
        self.get_element(self.superman_image).click()

    def enter_hotpoint_page(self):
        '''进入热点页面'''
        self.get_element(self.hotpoint).click()

    def hotpoint_back(self):
        '''热点返回'''
        try:
            self.get_element(self.native_back_u).click()
            logger.info("原生操作<返回")
        except:
            self.app_back()
            logger.info("使用按键返回")

    def mainpage_back(self):
        '''主页返回'''
        try:
            self.get_element(self.native_back_x).click()
            logger.info("原生操作<返回")
        except:
            self.app_back()
            logger.info("使用按键返回")

    def h5_back(self):
        '''h5返回'''
        try:
            self.driver.switch_to_webview()
            logger.info("操作h5<返回")
        except:
            self.app_back()
            logger.info("使用<按键返回")
        else:
            self.get_element(self.h5_back_x).click()
        finally:
            self.driver.switch_to_native()
