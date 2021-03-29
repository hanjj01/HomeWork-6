from SetpTest_62.HomeWork_62.pages.base_page import BasePage
from SetpTest_62.HomeWork_62.pages.personal_massage_page import PersonalmassgePage


class NamemassagePage(BasePage):
    def goto_pensonal_massage_page(self):
        self.perse_action("../pages/name_massge_pge.yaml", "goto_pensonal_massage_page")
        return PersonalmassgePage(self.driver)
