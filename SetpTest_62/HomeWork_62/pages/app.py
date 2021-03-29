
from appium import webdriver

from SetpTest_62.HomeWork_62.pages.base_page import BasePage
from SetpTest_62.HomeWork_62.pages.main_page import Main


class App(BasePage):
    _package = 'com.tencent.wework'
    _activity = '.launch.WwMainActivity'

    def app_start(self):
        if self.driver is None:
            caps = {}

            caps["platformName"] = "android"
            caps["devicesName"] = "127.0.0.1:7555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 0
            caps["dontStopAppOnReset"] = "true"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self.driver.start_activity(self._package, self._activity)
        self.driver.implicitly_wait(10)
        return  self

    def goto_main(self):
        return Main(self.driver)

