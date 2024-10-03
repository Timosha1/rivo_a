from pages.indexes_page import IndexesPage
import pytest

@pytest.mark.indexes
def test_xusd_apy(driver):
    index_page = IndexesPage(driver)
    index_page.open_xusd_page()
    assert index_page.locate_xusd_apy().is_displayed()
    apy_value = index_page.get_xusd_apy_text()
    assert apy_value != 0, "APY value should not be zero!"




























"""

try:
    driver.get("https://app.rivo.xyz/asset/0xA31eC4C877C65bEa5C5d4c307473624A0B377090")
    pendleETH_APY = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]"))
    )
    print("---pendleETH stats---")
    print("APY", pendleETH_APY.text)
except Exception as e:
    print(f"An error occurred: {e}")

try:
    driver.get("https://app.rivo.xyz/asset/0xF8F045583580C4Ba954CD911a8b161FafD89A9EF")
    xARB_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]"))
    )
    print("---xARB stats---")
    print("APY", xARB_APY.text)
except Exception as e:
    print(f"An error occurred: {e}")

try:
    driver.get("https://app.rivo.xyz/asset/0x0CD5cda0E120F7E22516f074284e5416949882C2")
    xETH_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]"))
    )
    print("---xETH stats---")
    print("APY", xETH_APY.text)
except Exception as e:
    print(f"An error occurred: {e}")

try:
    driver.get("https://app.rivo.xyz/asset/0xB0a66dD3B92293E5DC946B47922C6Ca9De464649")
    xDEFI_APY = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/main/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]"))
    )
    xDEFI_APY_text = xDEFI_APY.text
    print("---xDEFI stats---")

    apy_value_xDEFI = float(xDEFI_APY_text.strip('%')) / 100

    if apy_value_xDEFI > 0:
        print("APY", xDEFI_APY.text)
    else:
        print("APY ERROR")
except Exception as e:
    print(f"An error occurred: {e}")



finally:
    driver.quit()
"""