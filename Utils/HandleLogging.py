'''
Created on 2020年9月10日
装饰的应用：在其他模块导入该模块，使用@logger装饰器在方面名之前
@author: qguan
'''

import os
from functools import wraps
import logbook
from logbook.more import ColorizedStderrHandler

__author__ = "Joe"

check_path = '..'

LOG_DIR = os.path.join(check_path, 'logs')

file_stream = False

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='pytest框架执行测试用例日志输出', file_log=file_stream, level="DEBUG"):
    """ get logger Factory function """
    logbook.set_datetime_format('local')

    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)

LOG = get_logger(file_log=file_stream, level='INFO')


def logger(param):
    """ fcuntion from logger meta """
    def wrap(function):
        """ logger wrapper """
        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前方法 {}".format(param))
            if args:
                LOG.info("全部args参数参数信息 , {}".format(str(args)))
            if kwargs:
                LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            return function(*args, **kwargs)
        return _wrap
    return wrap