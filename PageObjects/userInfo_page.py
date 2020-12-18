'''
# -*- encoding=utf-8 -*-
Created on 2020年8月25日上午9:16:09
@author: Joe
@file:PageObjects.home_page.py
'''
from Common.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy

__author__ = "Joe"


class UserInfoPage(BasePage):
    '''
    classdocs
    '''
    # 元素定位
    # 返回
    back_x = (
        MobileBy.XPATH, "//android.view.View[1]/android.widget.ImageView[1]")

    # 昵称
    nick_name = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/nick_name_relative_layout")

    sex_selected = []

    # 性别
    sex = (MobileBy.ID, "com.chutzpah.yasibro.test:id/sex_relative_layout")
    # 男性
    male_sex = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvMale")
    # 女性
    female_sex = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvFemale")
    # 保密
    secret_sex = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvSecret")

    sex_selected.extend([male_sex, female_sex, secret_sex])

    # 生日
    birthday = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/birthday_relative_layout")

    # 目标分数
    goal_grade = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/goal_grade_relative_layout")

    # 上次成绩
    last_grade = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/last_grade_relative_layout")

    # 考试时间
    exam_time = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/test_time_relative_layout")

    # 考试地点
    exam_place = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/test_place_relative_layout")

    # 留学国家
    abroad_country = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/abroad_country_relative_layout")

    # 取相册
    from_albun = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvFromAlbum")

    # 拍照
    take_photo = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvTakePhoto")

    # 取消
    cancel = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvCancel")

    # 编辑昵称
    edit_nickName = (
        MobileBy.ID, "com.chutzpah.yasibro.test:id/nick_name_edit_text")

    # 完成
    finish = (MobileBy.ID, "com.chutzpah.yasibro.test:id/tvFinish")

    # toast提交成功
    toast_content = (MobileBy.XPATH, "//*[contains(@text,'提交成功')]")

    # toast保存成功
    save_success_toast = (MobileBy.XPATH, "//*[@text='保存成功']")

    # 确定
    sure_button = (MobileBy.ID, "com.chutzpah.yasibro.test:id/sure_text_view")
