from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "C:\Everything\IT\Testing\Automation_08_09_2019\AppiumClassTests/app_binaries\org.wikipedia.apk",
}

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
