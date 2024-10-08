from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def find(self, args):
        return self.driver.find_element(*args)

    # Проверка наличия элемента по локатору с try/except. Если элемент не найден, возникнет исключение
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def click(self, *args):
        element = self.find(*args)
        element.click()

    def fill_input(self, element, text):
        input_field = self.find(element)
        input_field.clear()
        input_field.send_keys(text)

