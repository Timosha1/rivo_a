from pages.overview_page import OverviewPage

def test_connect_wallet_exist(driver):
    overview_page = OverviewPage(driver)
    overview_page.open_overview_page()
    assert overview_page.connect_wallet_button().is_displayed()

def test_connect_wallet_click(driver):
    overview_page = OverviewPage(driver)
    overview_page.open_overview_page()
    overview_page.click_connect_wallet_button()

def test_connection_wallet_options_exist(driver):
    overview_page = OverviewPage(driver)
    overview_page.open_overview_page()
    assert overview_page.connect_wallet_option_create_rivo_wallet().is_displayed()
    assert overview_page.connect_wallet_option_rivo_wallet().is_displayed()
    assert overview_page.connect_wallet_option_metamask().is_displayed()
    assert overview_page.connect_wallet_option_walletconnect().is_displayed()



























"""
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
"""