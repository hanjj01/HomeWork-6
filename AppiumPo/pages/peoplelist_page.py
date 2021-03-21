from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from SetpTest_6.HomeWork_6.AppiumPo.pages.addpeople_page import AddpeoplePage
from SetpTest_6.HomeWork_6.AppiumPo.pages.basepage import BasePage


class PeoplelistPage(BasePage):


    def goto_addpeoplepage(self):
        self.swip_click("添加成员")
        return AddpeoplePage(self.driver)



