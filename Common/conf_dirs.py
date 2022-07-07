'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

import os

# 获取工程BASE路径
BASEPATH = os.path.dirname(os.path.dirname(__file__))

# Caps目录
caps_dir = os.path.join(BASEPATH, "Caps")

# 配置文件路径
config_dir = os.path.join(BASEPATH, "config")

# 日志路径
logfile_dir = os.path.join(BASEPATH, "Logs")

# allure生成报告路径
allurereports_dir = os.path.join(BASEPATH, "allure-results")

# htmlreports_dir
htmlreports_dir = os.path.join(BASEPATH, "//HtmlTestReports//")

# screenshotdir
screen_dir = os.path.join(BASEPATH, "Screenshots")

apk_path = os.path.join(BASEPATH, "apk")

venv_path = os.path.join(BASEPATH, 'venv')

if __name__ == '__main__':
    print(config_dir)
