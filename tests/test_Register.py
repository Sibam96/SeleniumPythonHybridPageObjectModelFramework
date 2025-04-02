import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
  def test_register_with_mandatory_fields(self):
    homePage = HomePage(self.driver)
    registerPage=homePage.navigate_to_register_page()
    account_success_page=registerPage.register_an_account(ExcelUtils.get_cell_data(".//ExcelFiles//Tutorialsninja.xlsx","RegisterTest",2,1),ExcelUtils.get_cell_data(".//ExcelFiles//Tutorialsninja.xlsx","RegisterTest",2,2),self.generate_email_with_time_stamp(),"1234567890","12345","12345","no","select")
    expected_heading_text="Your Account Has Been Created!"

    assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)



  def test_register_with_all_fields(self):
    homePage = HomePage(self.driver)
    registerPage=homePage.navigate_to_register_page()
    account_success_page=registerPage.register_an_account("Arun","Motoori",self.generate_email_with_time_stamp(),"1234567890","12345","12345","yes","select")
    expected_heading_text = "Your Account Has Been Created!"
    assert  account_success_page.retrieve_account_creation_message().__eq__(
        expected_heading_text)



  def test_register_with_duplicate_email(self):
    homePage = HomePage(self.driver)
    registerPage=homePage.navigate_to_register_page()
    registerPage.register_an_account("Arun","Motoori","amotooriapril2023@gmail.com","1234567890","12345","12345","yes","select")
    expected_warning_message = "Warning: E-Mail Address is already registered!"
    time.sleep(5)
    assert registerPage.retrieve_duplicate_email_warning().__eq__(
       expected_warning_message)



  def test_register_without_entering_any_fields(self):
    homePage = HomePage(self.driver)
    registerPage=homePage.navigate_to_register_page()
    registerPage.register_an_account("","","","","","","no","no")
    time.sleep(2)
    assert  registerPage.verify_all_warnings("First Name must be between 1 and 32 characters!","Last Name must be between 1 and 32 characters!")










