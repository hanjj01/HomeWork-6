from SetpTest_6.HomeWork_6.AppiumPo.pages.appmassage import AppMassage
from SetpTest_6.HomeWork_6.AppiumPo.pages.informationpage import InformationPage


class TestAdd:
    def setup(self):
        self.appmassage = AppMassage()


    def testcase(self):
        self.appmassage.goto_infomation().goto_peoplelistpage().goto_addpeoplepage().goto_action_page().action()
        # self.appmassage.goto_infomation().goto_peoplelistpage().goto_addpeoplepage().goto_action_page().action()