import time

from SetpTest_6.HomeWork_6.AppiumPo.pages.basepage import BasePage

class ActionPage(BasePage):


    def action(self):
        #姓名
        # self.find_send('//*[@text="必填"]','name14')
        # #性别
        # self.find_id_click('com.tencent.wework:id/av2')
        # time.sleep(2)
        # self.find_xpath_click("//*[@text='男']")
        # #手机号码
        # self.find_send('//*[@text="手机号"]','11111111124')
        # #保存
        # self.find_xpath_click('//*[@text="保存"]')
        self.perse_action('../pages/action.YAML')





