from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import OverviewPageLocators


class OverviewPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def open_overview_page(self):
        self.open("https://app.rivo.xyz")

    def should_be_connect_wallet_button(self):
        assert self.is_element_present(
            *OverviewPageLocators.connect_wallet_locator
        ), "Connect wallet button is not presented"

    def click_connect_wallet_button(self):
        self.connect_wallet_button().click()

    def should_be_wallet_option_create_rivo_wallet(self):
        assert self.is_element_present(
            *OverviewPageLocators.create_rivo_wallet_locator
        ), "Create Rivo wallet is not presented"

    def should_be_connect_wallet_option_rivo_wallet(self):
        assert self.is_element_present(
            *OverviewPageLocators.rivo_locator
        ), "Connect Rivo wallet is not presented"

    def connect_wallet_option_metamask(self):
        assert self.is_element_present(
            *OverviewPageLocators.metamask_locator
        ), "Connect Metamask wallet is not presented"

    def connect_wallet_option_walletconnect(self):
        assert self.is_element_present(
            *OverviewPageLocators.walletconnect_locator
        ), "Walletconnect is not presented"









