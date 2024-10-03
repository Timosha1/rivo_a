from conftest import driver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest

xusd_apy_selector = (By.ID, "index-Locus Yield USD-apy")

class IndexesPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    @pytest.mark.usefixtures("driver")
    def open_xusd_page(self):
        self.driver.get("https://app.rivo.xyz/asset/0x95611DCBFfC93b97Baa9C65A23AAfDEc088b7f32")

    def locate_xusd_apy(self):
        return self.find(xusd_apy_selector)

    def get_xusd_apy_text(self):
        xusd_apy = self.locate_xusd_apy()
        # Форматируем текст
        apy_text = xusd_apy.text.strip().replace("\n", " ")

        # Извлекаем числовое значение
        apy_value_str = apy_text.split()[0]  # Функция split разделяет строку в случае нахождения разделителя
        apy_value = float(apy_value_str.strip('%'))  # Превращаем в float число и убираем '%'

        return apy_value





"""
    def open_xpendle_page(self):
        self.driver.get("https://app.rivo.xyz/asset/0xA31eC4C877C65bEa5C5d4c307473624A0B377090")
    def open_xdefi_page(self):
        self.driver.get("https://app.rivo.xyz/asset/0xB0a66dD3B92293E5DC946B47922C6Ca9De464649")
    def open_xeth_page(self):
        self.driver.get("https://app.rivo.xyz/asset/0x0CD5cda0E120F7E22516f074284e5416949882C2")
    def open_xarb_page(self):
        self.driver.get("https://app.rivo.xyz/asset/0xF8F045583580C4Ba954CD911a8b161FafD89A9EF")
"""



"""
    xUSD_TVL = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/p[1]/div"))
    )
    xUSD_HOLDERS = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[5]/p[1]/div"))
    )
    xUSD_RISK_SCORE = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[7]/p[1]/div"))
    )
    xUSD_PRICE = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[3]/div[1]/p"))
    )
    compoundUSDC_allocation = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[1]/div[2]/div/div[2]/div[1]/p"))
    )
    compoundUSDC_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[1]/div[2]/div/div[2]/div[2]/p"))
    )
    usdBc_allocation = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[2]/div[2]/div/div[2]/div[1]/p"))
    )
    usdBc_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[2]/div[2]/div/div[2]/div[2]/p"))
    )
    curve2Pool_allocation = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[3]/div[2]/div/div[2]/div[1]/p"))
    )
    curve2Pool_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[2]/div[5]/div[3]/div[3]/div[2]/div/div[2]/div[2]/p"))
    )

    print("___xUSD stats___")

# check if apy is > 0
    xUSD_APY_text = xUSD_APY.text
    apy_value_xUSD = float(xUSD_APY_text.strip('%')) / 100
    if apy_value_xUSD > 0:
        print("APY - ", xUSD_APY.text)
    else:
        print("!!!APY ERROR!!!")

# check if TVL > 0
    xUSD_TVL_text = xUSD_TVL.text
    def parse_TVL_xUSD(xUSD_TVL_text):
        if xUSD_TVL_text.endswith('K'):
            return float(xUSD_TVL_text.rstrip('K')) * 1000
        elif xUSD_TVL_text.endswith('M'):
            return float(xUSD_TVL_text.rstrip('M')) * 1_000_000
        else:
            return float(xUSD_TVL_text)
    parsed_xUSD_TVL = parse_TVL_xUSD(xUSD_TVL_text)
    if parsed_xUSD_TVL > 0:
        print("TVL - ", xUSD_TVL.text)
    else:
        print("!!!TVL ERROR!!!")

# check if holders > 0
    xUSD_HOLDERS_count = int(xUSD_HOLDERS.text)
    if xUSD_HOLDERS_count > 0:
        print("Holders - ", xUSD_HOLDERS.text)
    else:
        print("!!!Holders ERROR!!!")

# check if Risk score > 0
    xUSD_risk_score = int(xUSD_RISK_SCORE.text)
    if xUSD_risk_score > 0:
        print("Risk Score - ", xUSD_RISK_SCORE.text)
    else:
        print("!!!Risk Score ERROR!!!")

# check if Price > 0
    def parse_PRICE_xUSD(price_text):
        if price_text.startswith('$'):
            return float(price_text.lstrip('$'))
        else:
            return float(price_text)
    parsed_xUSD_PRICE = parse_PRICE_xUSD(xUSD_PRICE.text)
    if parsed_xUSD_PRICE > 0:
        print("Price - ", xUSD_PRICE.text)
    else:
        print("!!!Price ERROR!!!")

    print("___xUSD Strategies stats___")
    print("compoundUSDC allocation - ", compoundUSDC_allocation.text)
    print("compoundUSDC APY - ", compoundUSDC_APY.text)
    print("usdBc allocation - ", usdBc_allocation.text)
    print("usdBc APY - ", usdBc_APY.text)
    print("curve2Pool allocation - ", curve2Pool_allocation.text)
    print("curve2Pool APY - ", curve2Pool_APY.text)
    print()


except Exception as e:
    print(f"An error occurred: {e}")
"""
