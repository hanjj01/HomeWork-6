from appium import webdriver



from SetpTest_6.HomeWork_6.AppiumPo.pages.informationpage import InformationPage


class AppMassage:
    def __init__(self):
        self.driver = None
        self.app_start()

    def app_start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["devicesName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 0
        # caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(20)

    def goto_infomation(self):
        return InformationPage(self.driver)