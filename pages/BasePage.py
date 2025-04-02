from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def type_locator(self,text,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        element.click()
        element.clear()
        element.send_keys(text)

    def element_click(self,locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()

    def check_display_status_of_element(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        return element.is_displayed()

    def retrieve_element_text(self,locator_name,locator_value):
        element=self.get_element(locator_name,locator_value)
        return element.text

    def get_element(self,locator_name,locator_value):
        element = None
        if locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        return element