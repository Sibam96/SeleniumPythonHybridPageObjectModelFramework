import pytest
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_xpath= "//input[@name='search']"
    search_button_xpath="//button[@class='btn btn-default btn-lg']"
    my_account_drop_menu_xpath= "//span[text()='My Account']"
    login_option_link_text_xpath="//a[text()='Login']"
    register_option_link_text_xpath="//a[text()='Register']"


    def enter_product_into_search_box_field(self,product_name):
        self.type_locator(product_name,"search_box_field_xpath",self.search_box_field_xpath)


    def click_on_search_button(self):
        self.element_click("search_button_xpath",self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.element_click("my_account_drop_menu_xpath",self.my_account_drop_menu_xpath)

    def select_login_option(self):
        self.element_click("login_option_link_text_xpath",self.login_option_link_text_xpath)
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.element_click("register_option_link_text_xpath",self.register_option_link_text_xpath)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()

    def search_for_a_product(self,product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

