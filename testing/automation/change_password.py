# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ChangePassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_change_password(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("inputUser").clear()
        driver.find_element_by_id("inputUser").send_keys("bob@concordia.ca")
        driver.find_element_by_id("inputPassword").clear()
        driver.find_element_by_id("inputPassword").send_keys("student")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("My Profile").click()
        driver.find_element_by_link_text("Change Password").click()
        driver.find_element_by_id("inputNewPassword").clear()
        driver.find_element_by_id("inputNewPassword").send_keys("student")
        driver.find_element_by_id("verifyNewPassword").clear()
        driver.find_element_by_id("verifyNewPassword").send_keys("student")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
