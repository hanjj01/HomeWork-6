from SetpTest_62.HomeWork_62.pages.app import App


class TestDelAddress:
    def setup(self):
        self.app = App()

    def test_del_address(self):
        self.app.app_start().goto_main().goto_addresslist_page().goto_name_massage_page().goto_pensonal_massage_page().goto_edit_page().edit_page()




