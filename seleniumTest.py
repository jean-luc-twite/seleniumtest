import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class AppTest(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver (ensure the path is correct)
        chrome_service = Service("C:/Users/jeanl/Documents/jeantwite/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_login(self):
        # Navigate to the URL
        self.driver.get("https://cms-frontends.agreeablesky-b053da30.southafricanorth.azurecontainerapps.io/auth/signin")

        try:
            # Fill in email
            email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
            email_input.send_keys("test@example.com")
            time.sleep(2)

            # Fill in password
            password_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']")))
            password_input.send_keys("testPassword")
            time.sleep(2)

            register_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                       "#root > div > div.w-full.max-w-md.mt-20.sm\:mt-24.rounded-lg.bg-gray-200.p-6.shadow-default.dark\:bg-\[\#033977\].opacity-90 > div > div.mb-5 > button")))
            register_btn.click()

            time.sleep(5)



        except Exception as e:
            self.fail(f"Test failed due to: {e}")

  

    def tearDown(self):
        # Clean up and close the browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
