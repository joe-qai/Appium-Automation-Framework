'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

import os

# 获取攻城当前路径
basepath = os.path.abspath(os.path.dirname(__file__))
# cur_dir = os.path.split(os.path.abspath(__file__))[0]

# Caps目录
caps_dir = basepath.replace("Common", "Caps")

# 配置文件路径
# yaml_dir = os.path.join(basepath + "//Propertices//")
yaml_dir = basepath.replace("Common", "Propertices")

# 日志路径
logfile_dir = basepath.replace("Common", "Logs")
#logfile_dir = os.path.join(basepath + "//Logs//")

# allure生成报告路径
# allurereports_dir = os.path.join(basepath + "//AllureReports//")
allurereports_dir = basepath.replace("Common", "allure-results")

# htmlreports_dir
htmlreports_dir = os.path.join(basepath + "//HtmlTestReports//")

# screenshotdir
screen_dir = basepath.replace("Common", "Screenshots")

apk_path = basepath.replace("Common", "apk")

venv_path = basepath.replace("Common", 'venv')
