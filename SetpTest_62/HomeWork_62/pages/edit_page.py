from SetpTest_62.HomeWork_62.pages.base_page import BasePage


class EditPage(BasePage):
    def edit_page(self):
        self.perse_action("../pages/edit_page.yaml","edit_page")