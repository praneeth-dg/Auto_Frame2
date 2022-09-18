import pytest
from selenium.webdriver.common.by import By
class LogoutPage():

     def __init__(self, driver):
         self.driver = driver
         self.Welcome_Link_xpath = "//p[@class='oxd-userdropdown-name']"
         self.Logout_Xpath = "//a[text()='Logout']"

     def click_welcome(self):
         self.driver.find_element(By.XPATH,self.Welcome_Link_xpath).click()

     def click_logout(self):
         self.driver.find_element(By.XPATH,self.Logout_Xpath).click()

