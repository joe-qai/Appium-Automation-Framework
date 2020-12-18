'''
# -*- encoding=utf-8 -*-
'''
import os
import socket
import subprocess

from appium import webdriver
import yaml

from Common.conf_dirs import caps_dir, apk_path, logfile_dir, venv_path
from Utils.HandleLoggingNew import HandleLogger


__author__ = 'Joe'


class BaseDriver:
    '''
           设备基础信息,使用yaml文件管理器
    '''
    app_path = apk_path + "/app-ieltsBroServer-check.apk"
    logger = HandleLogger().get_logger()

    def is_connect_device(self):
        '''asserts whether device is connected'''
        devices = os.popen("adb devices").read()
        dev_list = devices.split('\n')[1:]
        new_list = dev_list[-len(dev_list):]
        for device in new_list:
            if device.startswith("127.0.0.1:21503"):
                self.logger.info("adb connected device")
                return True
            elif device.startswith("127.0.0.1:62001"):
                self.logger.info("adb connected device")
                return True
            elif device.endswith('device'):
                self.logger.info("adb connected device")
                return True
        self.logger.info("error: no devices/emulators found")
        return False

    def check_port(self, host, port):
        """检测指定的端口是否被占用"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.shutdown(2)
        except:
            self.logger.error(
                'port:%s is available.server not started! ' % port)
            return True
        else:
            self.logger.info(
                'port:%s already be in used,server started!' % port)
            return False

    def start_appium(self, port):
        '''启动appium服务,默认端口'''
        cmd_find = 'netstat -aon | findstr %s' % port
        result = os.popen(cmd_find).read()
        if not result:
            cmd = 'start /b appium -p %s' % port
            subprocess.call(cmd, shell=True, stdout=open(
                file=logfile_dir + '/appium.log', mode='w'), stderr=subprocess.STDOUT)
            self.logger.info("appium-server started！！！")
            return True
        self.logger.info("appium-server not started！！！")
        return False

    def stop_appium(self, port):
        """释放指定的端口"""
        cmd_find = 'netstat -aon | findstr %s' % port
        result = os.popen(cmd_find).read().split()[-1]
        if result:
            cmd_kill = 'taskkill -f -pid %s' % result
            os.popen(cmd_kill)
            self.logger.info("stop appium server now！！！")
        self.logger.info('port %s is available !' % port)

    def base_driver(self, device, automationName="appium", noReset=False):
        '''
        To start the device,need start appium-server and connect device < or emulator> ;
        init device info and return the driver
        '''
        if not self.is_connect_device() and device == 'XiaoYao':
            try:
                self.logger.info("adb not connected device")
                os.popen("adb connect 127.0.0.1:21503")
            except:
                self.logger.error("adb connected failed!!!")
                raise

        if not self.is_connect_device() and device == 'YeShen':
            try:
                self.logger.info("adb not connected device")
                os.popen("adb connect 127.0.0.1:62001")
            except:
                self.logger.error("adb connected failed!!!")
                raise

        with open(caps_dir + "/desired_caps.yaml", encoding="utf-8") as fs:
            devices = yaml.load(fs, Loader=yaml.FullLoader)

        for dev in devices:
            if device == dev.get("deviceDesc"):
                if automationName != "appium":
                    dev["desired_caps"]["automationName"] = "UIAutomator2"
                if noReset:
                    dev["desired_caps"]["noReset"] = True
                desired_caps = dev["desired_caps"]
                desired_caps['app'] = self.app_path
                desired_caps["chromedriverExecutableDir"] = venv_path

                if self.check_port(dev["server_url"], dev["server_port"]):
                    self.logger.info("appium-server not started")
                    self.start_appium(dev["server_port"])

                driver = webdriver.Remote(
                    "http://{0}:{1}/wd/hub".format(dev["server_url"], dev["server_port"]), desired_caps)
                return driver
