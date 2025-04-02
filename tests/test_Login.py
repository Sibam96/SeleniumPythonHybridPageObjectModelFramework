import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestLogin(BaseTest):

  @pytest.mark.parametrize("email_address,password",ExcelUtils.get_data_from_excel(".//ExcelFiles//Tutorialsninja.xlsx","LoginTest"))
  def test_login_with_valid_credentials(self,email_address,password):
    homePage=HomePage(self.driver)
    login_page=homePage.navigate_to_login_page()
    account_Page=login_page.login_to_application(email_address,password)
    assert account_Page.display_status_of_edit_your_account_information_option()



  def test_login_with_invalid_email_and_valid_password(self):
    homePage = HomePage(self.driver)
    login_page=homePage.navigate_to_login_page()
    login_page.login_to_application(self.generate_email_with_time_stamp(),"12345")
    time.sleep(2)
    expected_warning_message="Warning: No match for E-Mail Address and/or Password."

    assert login_page.retrieve_warning_message().__contains__(expected_warning_message)




  def test_login_with_valid_email_and_invalid_password(self):
    homePage = HomePage(self.driver)
    login_page=homePage.navigate_to_login_page()
    login_page.login_to_application("amotooriapril2023@gmail.com","123456789")
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert login_page.retrieve_warning_message().__contains__(
        expected_warning_message)


  def test_login_without_entering_credentials(self):
    homePage = HomePage(self.driver)
    login_page=homePage.navigate_to_login_page()
    login_page.login_to_application("","")
    time.sleep(2)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert login_page.retrieve_warning_message().__contains__(
      expected_warning_message)





