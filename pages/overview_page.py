from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# connect wallet button
connect_wallet_selector = (By.XPATH, "")

# connect wallet options
create_rivo_wallet_selector = (By.XPATH, "")
rivo_selector = (By.XPATH, "")
metamask_selector = (By.XPATH, "")
walletconnect_selector = (By.XPATH, "")


class OverviewPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def open_overview_page(self):
        self.open("https://app.rivo.xyz")

    def connect_wallet_button(self):
        return self.find(connect_wallet_selector)

    def connect_wallet_button_is_displayed(self):
        return self.connect_wallet_button().is_displayed()

    def click_connect_wallet_button(self):
        self.connect_wallet_button().click()

    def connect_wallet_option_create_rivo_wallet(self):
        return self.find(create_rivo_wallet_selector)

    def connect_wallet_option_rivo_wallet(self):
        return self.find(rivo_selector)

    def connect_wallet_option_metamask(self):
        return self.find(metamask_selector)

    def connect_wallet_option_walletconnect(self):
        return self.find(walletconnect_selector)









