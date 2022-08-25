import time
import pytest
from appium import webdriver


def pytest_addoption(parser):
    parser.addoption('--platform_name',
                     action='store',
                     default="Android",
                     help="Choose your test platform: Android or iOS")
    parser.addoption('--platform_version',
                     action='store',
                     help="Choose your platform version: 10.0, 11.0, 12.0, etc")
    parser.addoption('--device_name',
                     action='store',
                     help="Enter your device or emulator name")
    parser.addoption('--automation_name',
                     action='store',
                     default='UiAutomator2',
                     help="Choose your automation tool: UiAutomator2 or something else")
    parser.addoption('--app_package',
                     action='store',
                     help="Enter your app package")
    parser.addoption('--app_activity',
                     action='store',
                     help="Enter your app activity")

@pytest.fixture()
def driver(request):
    platform_name = request.config.getoption('platform_name')
    platform_version = request.config.getoption('platform_version')
    device_name = request.config.getoption('device_name')
    automation_name = request.config.getoption('automation_name')
    app_package = request.config.getoption('app_package')
    app_activity = request.config.getoption('app_activity')

    desired_caps = {
        "platformName": platform_name,
        "platformVersion": platform_version,
        "deviceName": device_name,
        "automationName": automation_name,
        "appPackage": app_package,
        "appActivity": app_activity
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4724/wd/hub", desired_capabilities=desired_caps)

    yield driver
    time.sleep(2)
