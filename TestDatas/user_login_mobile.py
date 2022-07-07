# -*- encoding=utf-8 -*-

__author__ = 'Joe'

login_success = {"country": "中国",
                 "mobile": "13800138000",
                 "passwd": "111111",
                 "check": "登录成功"}

login_noMobile = {"mobile": "",
                  "passwd": "python",
                  "check": "无效的手机号"}

login_errorPasswd = {"mobile": "13266515340",
                     "passwd": "123456",
                     "check": "手机号或密码错误"}

login_noRegisterM = {"mobile": "13266515340",
                     "passwd": "python",
                     "check": "验证码已经发送到手机号为135\*\*\*\*5340,注意查收,验证码有效时间为60秒,验证码为\d{4}"}
