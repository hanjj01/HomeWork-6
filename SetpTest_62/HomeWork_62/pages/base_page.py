import json
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import  logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime).19s %(filename)s[line:%(lineno)',
                    datefmt = '%a, %d %b, %Y %H:%M:%S',
                    filename = 'report.log',
                    filemode = 'w')


class BasePage:
    # _parames = {}
    # #定义一个字典，要替换的内容放在一个字典里
    driver: WebDriver
    _black_list = [(MobileBy.ID,'com.tencent.wework:id/ig0')]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,by,locator):
        logging.info(f"fine: by={by},locator={locator}")
        try:
            element = self.driver.find_element(by,locator)
            return  element
        except Exception as e:
            for ele in self._black_list:
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return  self.find(by,locator)
                raise e


    # def find(self, by, locator):
    #     logging.info(f"fine: by={by},locator={locator}")
    #     try:
    #         element =  self.driver.find_element(by,locator)
    #
    #         return  element
    #     except Exception as e:
    #         for ele in self._black_list:
    #             #find_elements会返回元素的列表，如果没有元素会返回一个空列表
    #             eles = self.driver.find_elements(*ele)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return  self.find(by,locator)
    #
    #         #如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
    #         raise e

    def find_click(self, by,locator):
        self.find(by,locator).click()

    def sttup_implicitly_wait(self,timeout):
        self.driver.implicitly_wait(timeout)

    def find_sendkeys(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def perse_action(self,path,fun_name):
        with open(path,"r",encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
            for step in steps:
                if step["action"] == "find_click":
                    self.find_click(step["by"],step["locator"])
                elif step["action"] == "find":
                    self.find(step["by"],step["locator"])
                elif step["action"] == "find_sendkeys":
                    self.find_sendkeys(step["by"],step["locator"],step["text"])
                elif step["action"] == "swip":
                    self.swip(step["text"])

    def swip(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        'scrollIntoView(new UiSelector().'
                                        f'text("{text}").instance(0));').click()


