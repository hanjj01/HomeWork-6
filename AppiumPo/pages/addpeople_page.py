from appium.webdriver.webdriver import WebDriver

from SetpTest_6.HomeWork_6.AppiumPo.pages.action_add import ActionPage
from SetpTest_6.HomeWork_6.AppiumPo.pages.basepage import BasePage


class AddpeoplePage(BasePage):

    def goto_action_page(self):
        # self.find_xpath_click("//*[@text = '手动输入添加']")
        self.perse_action('../pages/addpeople.YAML')
        return ActionPage(self.driver)

