from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestWordleGame(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin')  # Update path to your ChromeDriver
        self.driver.get("https://www.nytimes.com/games/wordle/index.html")
        time.sleep(2)  

    def tearDown(self):
        self.driver.quit()

    def test_game_interaction(self):
        driver = self.driver

        play_button = driver.find_element(By.XPATH, '//button[@data-testid="Play"]')
        play_button.click()
        time.sleep(3)

        close_modal = driver.find_element(By.XPATH '//button[@data-testid="icon-close"]')

        invalid_word_input = "xxxxx" 
        input_field.send_keys(invalid_word_input)
        input_field.send_keys(Keys.RETURN)
        time.sleep(2)  
        error_message = driver.find_element(By.XPATH, '//div[contains(text(), "Not in word list")]')
        self.assertIsNotNone(error_message, "Error message for invalid word not found.")

        valid_word_input = "apple"  
        input_field.clear()
        input_field.send_keys(valid_word_input)
        input_field.send_keys(Keys.RETURN)
        time.sleep(2)

        error_message = driver.find_elements(By.XPATH, '//div[contains(text(), "Not in word list")]')
        self.assertEqual(len(error_message), 0, "There should be no error message for valid word.")