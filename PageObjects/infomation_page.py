'''
# -*- encoding=utf-8 -*-
'''
import random

from appium.webdriver.common.mobileby import MobileBy

from Common.BasePage import BasePage, BaseAction

__author__ = 'Joe'


class InfomationPage(BasePage, BaseAction):
    '''
    classdocs:元素定位
    details-infomation
    DELETE FROM user_comment WHERE from_user_id='1592533156822153753';
    '''

    # 返回<
    native_back = (MobileBy.CLASS_NAME, "android.widget.ImageView")
    # 点赞按钮
    praise_button = (MobileBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().resourceId("com.chutzpah.yasibro.test:id/like_text_view").instance(0)')
    #  "com.chutzpah.yasibro.test:id/like_text_view"

    # 收藏
    collect = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivCollect")
    # 收藏toast
    collect_success_toast = (MobileBy.XPATH, "//*[contains(@text,'收藏成功')]")
    # 分享
    share_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/share")
    # 评论框
    comment_box = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvComment")
    # 评论图标
    comment_pic = (MobileBy.ID, "com.chutzpah.yasibro.test:id/llComment")
    # 编辑输入评论
    edit_comment_input = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/editComment")
    # 发送评论
    send_comment = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvSend")
    # 发送成功toast
    send_comment_success_toast = (MobileBy.XPATH, "//*[@text='发布评论成功']")
    # 点赞/取消点赞成功toast
    praise_comment_toast = (MobileBy.XPATH, "//*[contains(@text,'点赞成功')]")

    # 举报入口图片
    tip_off_pic = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/more_comment_image_view")
    # 举报按钮
    tip_off_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMenuItem")
    # 举报原因
    tip_off_reason = (
        MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("广告")')
    # 举报成功toast
    tip_off_toast = (MobileBy.XPATH, "//*[@text='举报成功']")

    # + 上传图片按钮
    pic_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivPic")
    # 表情按钮+
    moji_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/ivEmoji")
    # 所有表情框，可以通过计算坐标位置点击表情
    all_moji_button = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/recycler_view")

    # 定位指定资讯，移动至可见区域
    infomation = (MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiSelector().className("android.widget.TextView").instance(0).textMatches("测试专用")')
    information_text = "留学测试"

    # 查看更多评论
    more_comment_text = "查看更多"
    more_comment = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/more_comment_button")

    def view_more_comment(self):
        '''查看更多'''
        self.find_ele_by_page(self.more_comment_text).click()

    def get_info_title(self):
        '''翻页获取资讯标题并点击'''
        self.find_ele_by_page(self.information_text).click()

    def click_tip_off_pic(self):
        '''点击举报入口图片按钮'''
        self.get_element(self.tip_off_pic).click()

    def click_tip_off_button(self):
        '''点击举报按钮'''
        self.get_element(self.tip_off_button).click()

    def select_tip_off_text(self):
        '''选择举报原因'''
        self.get_element(self.tip_off_reason).click()

    def click_praise_button(self):
        '''点赞/取消'''
        self.get_element(self.praise_button).click()

    def click_back_button(self):
        '''点击<返回'''
        self.get_element(self.native_back).click()

    def click_infomation(self):
        '''点击资讯'''
        self.get_element(self.infomation).click()

    def click_collect_star(self):
        '''点击收藏'''
        self.get_element(self.collect).click()

    def click_comment_box(self):
        '''点击评论框'''
        self.get_element(self.comment_box).click()

    def input_comment_and_send(self, content="我只是个测试!!!"):
        '''输入评论'''
        content = content + str(random.randint(1, 100))
        self.click_comment_box()
        self.get_element(self.edit_comment_input).send_keys(content)
        self.click_send_button()

    def click_send_button(self):
        '''点击发送'''
        self.get_element(self.send_comment).click()

    def get_send_success_toast(self):
        '''获取发送评论后的toast'''
        return self.get_toast_content(self.send_comment_success_toast)

    def get_praise_success_toast(self):
        '''获取点赞/取消toast'''
        return self.get_toast_content(self.praise_comment_toast)

    def get_collect_success_toast(self):
        '''收藏成功toast'''
        return self.get_toast_content(self.collect_success_toast)

    def get_tip_off_success_toast(self):
        '''举报成功toast'''
        return self.get_toast_content(self.tip_off_toast)

    def click_comment_pic(self):
        '''点击评论按钮-进入评论列表'''
        try:
            self.view_more_comment()
        except:
            self.get_element(self.comment_pic).click()
