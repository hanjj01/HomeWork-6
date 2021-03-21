from appium import webdriver


from SetpTest_6.HomeWork_6.AppiumPo.pages.basepage import BasePage
from SetpTest_6.HomeWork_6.AppiumPo.pages.peoplelist_page import PeoplelistPage


class InformationPage(BasePage):

    def goto_peoplelistpage(self):
        # self.find_xpath_click('//*[@text="通讯录"]')
        self.perse_action('../pages/informationpage.YAML')
        return PeoplelistPage(self.driver)