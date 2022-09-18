import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.Loginpage import LoginPage
from pages.LogoutPage import LogoutPage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestFramwework():

    #Login Page
      def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        Login = LoginPage(driver)
        time.sleep(3)
        Login.enter_username(utils.USERNANE)
        Login.enter_password(utils.PASSWORD)
        Login.click_login()
        print("Login success")

    # Home page
      def test_logout(self):
        driver = self.driver
        Logout = LogoutPage(driver)
        Logout.click_welcome()
        Logout.click_logout()

        print("Logout Success")