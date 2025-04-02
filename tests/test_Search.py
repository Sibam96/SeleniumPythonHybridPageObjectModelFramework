import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest



class TestSearch(BaseTest):
  def test_search_for_a_valid_product(self):
    homePage=HomePage(self.driver)
    time.sleep(2)
    search_page= homePage.search_for_a_product("HP")
    assert search_page.display_status_of_valid_product()


  def test_search_for_an_invalid_product(self):
    homePage = HomePage(self.driver)
    search_page=homePage.search_for_a_product("Honda")
    expected_text="There is no product that matches the search criteria ABC."
    assert search_page.retrieve_no_product_message().__eq__(expected_text)





  def test_search_without_entering_any_product(self):
    homePage = HomePage(self.driver)
    search_page=homePage.search_for_a_product("")
    expected_text = "There is no product that matches the search criteria."
    assert search_page.retrieve_no_product_message().__eq__(expected_text)




