'''
# -*- encoding=utf-8 -*-
'''

__author__ = 'Joe'

import pytest
import time


# %Y-%m-%d_%H-%M-%S
curTime = time.strftime("%Y-%m-%d")

# "-m", "smoke","-s", "-q",
pytest.main(["--alluredir", "allure-results"])
# allure generate allure-results/ -o allure-html-reports/ 将xml报告转换成html报告
# allure serve allure-results  临时生成访问html报告服务器