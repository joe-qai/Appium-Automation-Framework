'''
# -*- encoding=utf-8 -*-
'''

import allure
import pytest

from PageObjects.search_page import SearchPage


__author__ = 'Joe'


class TestSearch(object):
    '''
            搜索页面操作测试用例集
    '''

    @allure.feature("搜索页面操作")
    def test_search_page(self, common_driver):
        with allure.step("点击实时热点"):
            SearchPage(common_driver).enter_search_page()
            SearchPage(common_driver).enter_hotpoint_page()
            SearchPage(common_driver).hotpoint_back()
        with allure.step("点击达人头像"):
            SearchPage(common_driver).enter_superman_page()
            SearchPage(common_driver).mainpage_back()
        with allure.step("取消/关注达人"):
            SearchPage(common_driver).antention_superman()

    @allure.feature("搜索内容")
    @pytest.mark.parametrize("content", ["留学"])
    def test_search_content(self, common_driver, content):
        with allure.step("输入搜索内容确认"):
            SearchPage(common_driver).input_content(content)
        with allure.step("点击朋友头像"):
            SearchPage(common_driver).enter_superman_page()
            SearchPage(common_driver).mainpage_back()
        with allure.step("取消/关注朋友"):
            SearchPage(common_driver).antention_superman()
        with allure.step("返回搜索页"):
            SearchPage(common_driver).clear_search_text()
        with allure.step("清空搜索历史"):
            SearchPage(common_driver).clear_history_text()
        with allure.step("取消搜索返回首页"):
            SearchPage(common_driver).cancel_search_x()