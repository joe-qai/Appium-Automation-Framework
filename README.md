# ai_appium_po

ai_appium_po 是一个基于 Python 的移动端 UI 自动化示例框架，采用 Page Object (PO) 分层设计，基于 Appium + pytest + Allure，包含页面对象、测试用例、设备启动配置与常用工具。该仓库为框架 demo，包含示例 PageObjects 与 TestCases，便于快速上手与二次开发。

快速概览
- 语言：Python（requirements.txt）
- 测试框架：pytest
- 自动化驱动：Appium（Appium Python Client）
- 报告：Allure（allure-python 插件）
- 项目目录（主要项）：
  - APK/           存放被测 APK（示例）
  - Caps/          设备 / capabilities 配置
  - Common/        公共启动/Driver 封装（App 启动管理）
  - Libs/          额外依赖或自定义库（demo 中用于报告等）
  - PageObjects/   页面对象实现（示例：login_page.py、index_page.py 等）
  - TestCases/     示例测试用例（test_demo.py、test_index.py、test_search.py…）
  - TestDatas/     测试数据
  - Utils/         工具类（日志、截图等）
  - allure-results/Allure 的结果目录（运行 pytest 时产出）
  - conftest.py    pytest fixtures 与 driver 管理
  - requirements.txt  Python 依赖清单

依赖
仓库内 requirements.txt（示例）包含：
- Appium_Python_Client
- pytest
- allure_python_commons
- selenium
- PyYAML
- Logbook

建议使用 Python 3.8+ 并在虚拟环境中安装依赖：
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
# .\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

快速运行（示例）
1. 启动 Appium Server（本地或远端），并确保设备或模拟器可用（adb devices）。
2. 配置 Caps/ 下的设备能力或在 conftest.py 中按需修改。
3. 运行测试并把 Allure 结果输出到仓库内的 allure-results：
```bash
pytest TestCases -q --alluredir=allure-results
```
4. 查看报告（需安装 Allure CLI）：
```bash
# 临时启动查看
allure serve allure-results

# 或生成静态报告到目录并打开
allure generate allure-results -o allure-report --clean
allure open allure-report
```

关于 conftest.py（仓库中已有）
- conftest.py 中包含 driver 的创建/销毁逻辑、若干 fixture（可在测试中通过参数注入 driver）。
- 你可以在 conftest.py 中修改设备参数来源（例如从 Caps/ 下的 yaml、环境变量或 pytest 参数读取）以适配你的运行环境。

示例 Page Object 与测试（仓库内示例）
- PageObjects/login_page.py：封装登录相关元素与操作（示例）
- TestCases/test_demo.py、test_index.py：演示如何使用 PageObjects 与 fixtures 编写业务层测试

常见实践
- 把设备能力（capabilities）与环境配置放在 Caps/ 或 config 文件中，通过 pytest 参数或环境变量选择目标设备/环境。
- conftest.py 负责统一管理 driver 生命周期（scope 可选 function/class/session）。
- 失败时在 teardown 中截屏并把截图、日志附加到 Allure 报告（仓库 Utils/ 可扩展）。
- 并行执行时（pytest-xdist）注意每个进程使用不同设备/端口，避免冲突。

调试提示
- 无法连接设备：检查 adb devices、模拟器是否启动、Appium 服务端口是否可达。
- 元素定位不稳：优先使用 resource-id / accessibility id；必要时加显式等待（WebDriverWait）。
- Allure 无内容或报错：确认已安装 allure 命令行工具并且 pytest 执行时使用了 --alluredir 参数。

如何贡献
1. Fork 并创建分支：feature/xxx 或 fix/xxx
2. 在本地运行并验证测试（pytest TestCases）
3. 提交 PR，并在描述中说明变更内容与影响范围

许可与声明
- 当前仓库未在 README 中指定具体许可证，请在仓库中添加 LICENSE 文件（例如 MIT / Apache-2.0）以明确授权。

联系
- 如需我帮助把本 README 提交到仓库、或把 conftest.py、Caps 配置做成更灵活的入参（例如支持 --device / --caps-file 参数），我可以继续帮你修改并提交 PR 或直接更新 README（需要你授权写入仓库）。
