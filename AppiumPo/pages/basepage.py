import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class  BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_send_name(self,locator,massage):
        self.driver.find_element_by_xpath(locator).send_keys(massage)

    def find_send_phone(self,locator,massage):
        self.driver.find_element_by_xpath(locator).send_keys(massage)

    def find_id_click(self,locator):
        self.driver.find_element_by_id(locator).click()

    def find_xpath_click(self,locator):
        self.driver.find_element_by_xpath(locator).click()

    def find_xpath_click_save(self, locator):
        self.driver.find_element_by_xpath(locator).click()


    def swip_click(self,text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def perse_action(self,path):
        with open(path,'r',encoding='utf-8') as f:
            setps = yaml.safe_load(f)
            print(setps)
            for setp in setps:
                if setp['action'] == 'find_send':
                    self.find_send(setp['locator'],setp['massage'])
                elif setp['action'] == 'find_id_click':
                    self.find_id_click(setp['locator'])
                elif setp['action'] == 'find_xpath_click':
                    self.find_xpath_click(setp['locator'])
                elif setp['action'] =='find_xpath_click':
                    self.find_send(setp['locator'],setp['massage'])













        # def parse_action(self, path):
        #     with open(path, "r", encoding="utf-8") as f:
        #         steps = yaml.safe_load(f)
        #         print(steps)
        #     for step in steps:
        #         if step["action"] == "find_click":
        #             self.find_click(step["locator"])
        #         elif step["action"] == "find":
        #             self.find(step["locator"])
