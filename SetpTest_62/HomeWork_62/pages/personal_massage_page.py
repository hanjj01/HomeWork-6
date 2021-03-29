from SetpTest_62.HomeWork_62.pages.base_page import BasePage
from SetpTest_62.HomeWork_62.pages.edit_page import EditPage


class PersonalmassgePage(BasePage):
    def goto_edit_page(self):
        self.perse_action("../pages/personal_massage_page.yaml", "goto_edit_page")
        return EditPage(self.driver)
