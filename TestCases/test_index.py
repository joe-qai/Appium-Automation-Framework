'''
# -*- encoding=utf-8 -*-
'''
import allure
import pytest

from PageObjects.comment_page import CommentPage
from PageObjects.index_page import IndexPage
from PageObjects.infomation_page import InfomationPage


__author__ = 'Joe'


class TestIndex():
    '''首页资讯测试用例集'''
    @pytest.mark.skip(season="demo")
    @allure.feature("首页列表操作")
    def test_index_switch(self, login_driver):
        with allure.step("首页专题tab切换"):
            IndexPage(login_driver).click_exam_ask_answer()
            IndexPage(login_driver).click_fine_of_write()
            IndexPage(login_driver).swipe_right()
        with allure.step("切换推荐列表向上滑动点击资讯"):
            IndexPage(login_driver).click_recommend()
            IndexPage(login_driver).swipe_up()
            InfomationPage(login_driver).get_info_title()

    @pytest.mark.skip(season="demo")
    @allure.feature("资讯详情操作")
    def test_infomation_detail(self, login_driver):
        with allure.step("进入资讯详情点赞"):
            InfomationPage(login_driver).click_praise_button()
            assert InfomationPage(login_driver).get_praise_success_toast()
        with allure.step("资讯详情收藏"):
            InfomationPage(login_driver).click_collect_star()
            assert InfomationPage(login_driver).get_collect_success_toast()
        with allure.step("资讯详情评论"):
            InfomationPage(login_driver).click_comment_box()
            InfomationPage(login_driver).input_comment_and_send()
            assert InfomationPage(login_driver).get_send_success_toast()
        with allure.step("资讯详情举报评论"):
            InfomationPage(login_driver).click_tip_off_pic()
            InfomationPage(login_driver).click_tip_off_button()
            InfomationPage(login_driver).select_tip_off_text()
            assert InfomationPage(login_driver).get_tip_off_success_toast()
            InfomationPage(login_driver).click_comment_pic()

    @pytest.mark.skip(season="demo")
    @allure.feature("评论列表操作")
    def test_comment_list(self, login_driver):
        with allure.step("评论列表点赞"):
            CommentPage(login_driver).click_praise_button()
            assert CommentPage(login_driver).get_praise_success_toast()
        with allure.step("进入评论列表举报"):
            CommentPage(login_driver).click_tip_off_pic()
            CommentPage(login_driver).click_tip_off_button()
            CommentPage(login_driver).select_tip_off_text()
            assert CommentPage(login_driver).get_tip_off_success_toast()
        with allure.step("评论列表评论"):
            CommentPage(login_driver).click_comment_box()
            CommentPage(login_driver).input_comment_and_send()
            assert CommentPage(login_driver).get_send_success_toast()