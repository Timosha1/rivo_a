from .base_page import BasePage


class ConnectWalletPage(BasePage):
    def should_be_connect_wallet(self):
        self.should_be_connect_wallet_button()
        self.should_be_mm_connect_button()
        self.should_be_mm_unlock_window()

    def should_be_connect_wallet_button(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True