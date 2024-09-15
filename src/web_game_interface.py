# src/web_game_interface.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from game_interface import AbstractGameInterface

class WebGameInterface(AbstractGameInterface):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get('http://dweeb.ninja/chromaxen/#game')
    
    def start_new_game(self):
        new_game_button = self.driver.find_element(By.ID, "entry_game_button")
        new_game_button.click()
    
    def click_random_game(self):
        random_game_button = self.driver.find_element(By.ID, "entry_random_button")
        random_game_button.click()
    
    def view_all_rules(self):
        all_rules_button = self.driver.find_element(By.ID, "entry_all_rules_button")
        all_rules_button.click()
    
    def continue_game(self):
        continue_button = self.driver.find_element(By.ID, "entry_continue_button")
        continue_button.click()
    

driver = webdriver.Chrome()
web_game = WebGameInterface(driver)
web_game.start_new_game()
