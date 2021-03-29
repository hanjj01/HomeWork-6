from SetpTest_62.HomeWork_62.pages.base_page import BasePage
from SetpTest_62.HomeWork_62.pages.name_massge_pge import NamemassagePage


class AddresslistPage(BasePage):
    def goto_name_massage_page(self):
        self.perse_action("../pages/addresslist_page.YAML", "goto_name_massage_page")
        return NamemassagePage(self.driver)
