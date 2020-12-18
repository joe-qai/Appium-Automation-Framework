# -*- encoding=utf-8 -*-

__author__ = "Joe"

import logging.handlers
import time
from Common.conf_dirs import logfile_dir


class HandleLogger():
    '''扩展：灵活配置，日志收集器输出文件路径，日志输出格式、日志级别输出'''

    @staticmethod
    def get_logger():
        # 获取当前日期
        curTime = time.strftime("%Y-%m-%d_%H")
        # ERROR、WARNING、INFO、DEBUG
        # 第一步创建日志收集器
        # so 这个里面的name字符串可以通过%(name)日志格式输出,也可以不使用
        logger = logging.getLogger()

        # 第二步设置收集器等级
        logger.setLevel("DEBUG")

        # 第三步添加输出渠道
        # 1、创建输出控制台
#         sh = logging.StreamHandler()
        # 2、输出级别
#         sh.setLevel("DEBUG")
        # 3、绑定日志收集器
#         logger.addHandler(sh)

        # 第四步添加输出渠道：文件
#         fh = logging.FileHandler(
#             filename=logfile_dir + 'test.log', mode='a', encoding='utf8')
#         sh.setLevel("INFO")
#         logger.addHandler(fh)

        # 日志轮转
        # 时间分割轮转
        # 文件大小轮转
        # tips:修改日志输出渠道：1024 * 1024=1Mb,1024=1kb
        # 8Bit=1Bytes,1024Bytes=1KB,1024KB=1MB

        fh2 = logging.handlers.RotatingFileHandler(
            filename=logfile_dir + "/test_{}.log".format(curTime), maxBytes=1024 * 1024 * 20, backupCount=3, encoding='utf8')
#         logging.handlers.TimedRotatingFileHandler(filename=logfile_dir + "test.log", when="M", encoding='utf8',backupCount=3)

        logger.handlers.clear()

        fh2.setLevel('ERROR')

        logger.addHandler(fh2)

        # 第五步设置日志格式,%(funcName)s 在函数中的日志文件会带上def定义的方法名
        formatter = logging.Formatter(
            "%(asctime)s:%(module)s ：%(funcName)s：%(thread)d ：%(process)d  :%(lineno)d :%(levelname)s :%(message)s")

        # 设置日志输出格式
#         sh.setFormatter(formatter)
#         fh.setFormatter(formatter)
        fh2.setFormatter(formatter)
        return logger


if __name__ == '__main__':
    logger = HandleLogger().get_logger()

    def ddd():
        logger.info("test")
    ddd()
    logger.debug("msg")
    logger.error("1")
