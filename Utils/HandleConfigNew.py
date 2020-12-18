# -*- encoding=utf-8 -*-

__author__ = "Joe"


from configparser import ConfigParser


class HandleConfig(ConfigParser):
    """封装配置文件读写工具类"""

    def __init__(self, filename, encoding="utf-8"):
        # 创建ConfigParser解析对象，继承原类
        super().__init__()
        self.filename = filename
        self.encoding = encoding
        # 读取指定配置文件
        self.read(self.filename, encoding=self.encoding)

    def __call__(self, section, option):
        '''魔术方法直接类调用即类本身'''
        return self.get(section, option)

    def write_data(self, section, option, value):
        '''写入配置文件方法'''
#         起始这里有一个判断，section是否存在，不存在则写入前创建section
        self.set(section, option, value)
        with open(self.filename, "w", encoding=self.encoding) as pf:
            self.write(pf)
