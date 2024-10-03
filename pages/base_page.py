class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def find(self, args):
        return self.driver.find_element(*args)

    def click(self, *args):
        element = self.find(*args)
        element.click()

    def fill_input(self, element, text):
        input_field = self.find(element)
        input_field.clear()
        input_field.send_keys(text)

