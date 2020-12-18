'''
Created on 2020年8月24日

@author: qguan
'''

import allure
import pytest

from PageObjects.index_page import IndexPage
from PageObjects.userCenter_page import UserCenterPage


__author__ = "Joe"


class TestUserCenter():
    '''
    classdocs
    '''

    @pytest.mark.skipif(True, reason="demo")
    @allure.feature("点击用户头像,进入个人中心")
    def test_personal_center(self, common_driver):
        with allure.step("点击头像展示个人中心"):
            IndexPage(common_driver).noFirst_click_headImage()
            UserCenterPage(common_driver).click_headImage()
