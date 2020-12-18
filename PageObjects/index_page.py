'''
# -*- encoding=utf-8 -*-
'''
import time
from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage, BaseAction
from Utils.HandleLoggingNew import HandleLogger

__author__ = 'Joe'

logger = HandleLogger().get_logger()


class IndexPage(BasePage, BaseAction):
    '''元素定义内属性'''

    # 扫一扫
    scan = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivScan")
    # 首页tab
    index_tab = (
        MobileBy.XPATH, "//android.widget.TextView[contains(@text,'首页')]")
    # 头像
    headImage = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/ivHeader")

    # 登录成功toast
    login_success_msg = (MobileBy.XPATH, "//*[@text='登录成功']")

    # 首页专栏
    fine_of_write = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("写作精批")')

    exam_QA = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("考场问答")')

    recommend_list = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("推荐")')

    # 暂不更新
    update_later = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("暂不更新")')

    # 广告弹窗
    ivad_w = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivAd")

    # <H5返回，需要切换上下文操作h5返回
    h5_back = (MobileBy.XPATH, "//div[@class='navigation_bar_left']")

    # 进入个人中心，首页右侧栏
    index_right = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llContent")

    def back_of_h5(self):
        '''h5返回，如果不是h5就使用键盘返回'''
        try:
            self.driver.switch_to_webview()
        except:
            self.app_back()
            logger.error("使用按键返回")
        else:
            self.get_element(self.h5_back).click()
            logger.info("操作h5<返回")
        finally:
            self.driver.switch_to_native()

    def back_for_index(self):
        '''返回首页'''
        self.get_element(self.index_right).click()

    def click_ad(self):
        '''点击广告弹框'''
        try:
            self.click_later_update()
        except:
            self.get_element(self.ivad_w, wait_time=8).click()
        else:
            self.get_element(self.ivad_w, wait_time=8).click()

    def click_later_update(self):
        '''暂不更新'''
        self.get_element(self.update_later, wait_time=8).click()

    def click_index(self):
        '''点击首页tab'''
        self.get_element(self.index_tab).click()

    def click_scan(self):
        '''点击首页扫一扫：未登录触发条件'''
        self.get_element(self.scan).click()

    def click_head_image(self):
        '''点击首页头像登录或者拉开个人中心：用于未登录'''
        self.click_index()
        try:
            self.click_ad()
        except:
            self.get_element(self.headImage).click()
        else:
            time.sleep(3)
            self.back_of_h5()
            self.get_element(self.headImage).click()

    def noFirst_click_headImage(self):
        '''非首次操作首页头像'''
        self.get_element(self.headImage).click()

    def click_fine_of_write(self):
        '''点击首页写作精批'''
        self.get_element(self.fine_of_write).click()

    def click_exam_ask_answer(self):
        '''点击首页考场问答'''
        self.get_element(self.exam_QA).click()

    def click_recommend(self):
        '''点击首页推荐'''
        self.get_element(self.recommend_list).click()

    def get_login_success_toast(self):
        '''获取登录成功toast'''
        return self.get_toast_content(self.login_success_msg)
