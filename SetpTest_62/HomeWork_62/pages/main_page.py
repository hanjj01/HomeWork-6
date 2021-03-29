from SetpTest_62.HomeWork_62.pages.addresslist_page import AddresslistPage
from SetpTest_62.HomeWork_62.pages.base_page import BasePage


class Main(BasePage):
    def goto_addresslist_page(self):
        self.perse_action("../pages/main.YAML", "goto_addresslist_page")
        return AddresslistPage(self.driver)
