from selenium.webdriver.common.by import By


class OverviewPageLocators:
    # connect wallet button
    connect_wallet_locator = (By.XPATH, "")

    # connect wallet options
    create_rivo_wallet_locator = (By.XPATH, "")
    rivo_locator = (By.XPATH, "")
    metamask_locator = (By.XPATH, "")
    walletconnect_locator = (By.XPATH, "")

    # Unlock page in MM
    mm_unlock_page_locator = (By.CSS_SELECTOR, '[data-testid="unlock-page"]')
    mm_unlock_page_password_field_locator = (By.CSS_SELECTOR, '[data-testid="unlock-password"]')
    mm_unlock_page_title_locator = (By.CSS_SELECTOR, '[data-testid="unlock-page-title"]')
    mm_unlock_page_submit_locator = (By.CSS_SELECTOR, '[data-testid="unlock-submit"]')


