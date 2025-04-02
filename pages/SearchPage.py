import pytest
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text_xpath="//a[normalize-space()='HP LP3065']"
    no_product_message_xpath= "//p[text()='There is no product that matches the search criteria.']"

    def display_status_of_valid_product(self):
       return self.check_display_status_of_element("valid_hp_product_link_text_xpath",self.valid_hp_product_link_text_xpath)




    def retrieve_no_product_message(self):
        return self.retrieve_element_text("no_product_message_xpath",self.no_product_message_xpath)
