#### appium移动项目自动化工程
- allure-results: 结合allure-pytest升级的测试报告,使用pytest测试框架
- Caps：存放移动设备启动信息
- Common:公共文件，存放appium启动类
- Libs：依赖，结合unittest测试框架的jinja2测试报告类
- Logs：存放日志文件
- PageObjects：存放页面对象
- config：存放配置文件
- HtmlTestReports：报告目录
- Screenshots：截屏
- Testcases：测试用例
- Utils：工具类
- venv：虚拟环境
- .gitignore 忽略文件配置
- requirements.txt ：是由pipreqs 指定项目导出的使用的工具类

#### 有用的pytest框架依赖库
- pytest-dependency  解决测试用例之间的依赖关系：上一个用例执行失败，下一个用例会被跳过，值得思考的问题：若仅是断言失败，后面的用例并不一定受影响，是不是有些过于草率了？
- - 先mark住前一个用例：@pytest.mark.dependency()
- - 再mark住后一个用例：@pytest.mark.dependency(depends=['上一个依赖的用例方法名'])
- allure-pytest  allure测试报告相关的插件
- pytest-rerunfailures  重试测试用例，用法:pytest --reruns 2 *.py
- - 命令参数：--reruns=RERUNS 重试失败的测试用例次数,--reruns-delay=RERUNS_DELAY, 间隔多长时间重试
- - tips:@pytest.mark.flaky(reruns=6, reruns_delay=2) 可以直接在用例方法上加上mark
- pytest-assume 多重校验，场景：脚本中若是有多个断言，第一个失败了，要想下面的断言继续就需要这个插件，用法：pytest.assume(表达式)替代了assert关键字
- pytest-ordering 指定执行顺序，某些场景有先后顺序，解决一定的依赖关系，用法：@pytest.mark.run(order=1)，由order值来决定执行顺序；
- - 试想：pytest执行测试用例顺序是自上往下，那么这个插件作用不算太大
- pytest-sugar 焦糖：更改pytest-sugar的默认外观，添加进度条，并立即显示失败的测试
- pytest-cov 有点像测试代码覆盖率
- pytest-instafail 修改pytest的默认行为以立即显示失败和错误，而不是等到pytest完成每个测试的运行
- pytest-xdist 允许您通过-n标志并行运行多个测试，pytest -n 2 



#### 项目工程搭建事项
- 逍遥/夜神模拟器，设置打开usb调试模式
- appium启动服务，-p 参数可以指定服务端口，默认4723
- - 优先安装nodejs，使用npm install -g appium命令行安装
- cmd命令：adb connect 127.0.0.1:21503 连接逍遥模拟器，
- - 62001是夜神模拟器的默认端口
- - 优先安装Android-SDK,再配置adb环境变量即可
- 否则：adb devices 找不到该设备
- - adb get-state 如果获取到多设备时返回的不是device而是error: more than one device/emulator更多虚拟设备连接
- appium启动设备的基础配置信息写入配置文件，建议：yaml文件
- eclipse或者pycharm都需要配置指定venv虚拟环境的python解释器
- venv虚拟环境也需要有浏览器驱动chromedriver.exe文件

##### Python PEP8编码规范
- 1、英文版地址：http://legacy.python.org/dev/peps/pep-0008/
```text
要求：
1、文档字符串注释及方法<函数>注释尽量使用三引号
2、import导包顺序依次：内置库、第三方库、封装库，且每组之间空行隔开
3、模块命名规范同函数命名：单词下线隔开，类命名请使用大驼峰命名规则
4、类属性命名及所有命名尽量做到见名知意
5、所有常量命名请使用全大写字母：ACTIONENTER=22
6、空格才是python编码缩进方式的所选，制表符tab不建议使用
```

##### 类型	命名规则	举例说明：
- 模块名/包名:全小写字母，简单有意义，多单词组合可使用下划线增加可阅读性
- 函数名:全小写字母，可以使用下划线增加可阅读性	foo(), my_func()
- 变量名:全小写字母，可以使用下划线增加可阅读性 	age、my_var
- 类名:采用PascalCase命名规则，由多个单词组成名称，其每个单词的首字母大写：MyClass
- 常量名:全部大写字母，可以使用下划线增加可阅读性	LEFT、TAX_RATE
- 基类可以使用Base、Abstract前缀来命名
- 所有命名切莫带罗马数字，以及勿以数字开头


#### 疑问
- python+appium+pytest<logging\pyyaml\allure-pytest>
- UI自动化框架的PO分层思想
- - 基础层<BasePage:对于appium实现的常用api进行的二次封装，用多少就封装多少>
- - 页面对象层<逻辑层>--继承了基础层
- - 测试用例层<业务层>--面向过程？
- - - utils：日志收集器、配置文件处理、excel文件处理、发送邮件、测试报告

#### pytest框架:conftest.py/pytest.ini
- @pytest.fixture<夹具：环境处理器：setup、teardown，setupClass、teardownClass>
- - 默认(scope='function'),作用域范围：session > mudole > class > function
```python
@pytest.mark.usefixture(driver)
def test_01(self,driver):
    pass
```
- 耦合处理用例依赖，不影响下一条用例的执行环境：即测试模块不要试图请求一次运行环境<conftest>将所有测试用例模块执行完成.

#### allure测试报告
```
支持java、python、ruby等等
```
- allure-pytest 等插件
- allure generate allure-dir -o html-dir   # 生成html报告到指定目录
- allure serve allure-dir
- pytest --help 帮助文档
- - -s 输出信息 、 -q 简要信息、 -v 详细信息、-m 指定标签、-k 关键字<and/not >