# src/page_objects/entry_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.all_rules_page import AllRulesPage
from selenium.common.exceptions import NoSuchElementException

WAIT_TIME = 10

class EntryPage:
    def __init__(self, driver):
        self.driver = driver
        self.entry_page = driver.find_element(By.ID, "entry_page")

    def is_displayed(self) -> bool:
        try: 
            entry_page_element = self.driver.find_element(By.ID, "entry_page")
            return entry_page_element.is_displayed()
        except NoSuchElementException:
            return False

    def view_all_rules(self):
        """Navigate to the All Rules page and return its page object."""
        all_rules_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "entry_all_rules_button"))
        )
        all_rules_button.click()
        # Wait until the All Rules page is loaded
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, "all_rules_container"))
        )
        return AllRulesPage(self.driver)
    
    def start_new_game(self):
        new_game_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "entry_game_button"))
        )
        new_game_button.click()
    
    def click_random_game(self):
        random_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "entry_random_button"))
        )
        random_button.click()
    
    def view_all_rules(self):
        all_rules_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "entry_all_rules_button"))
        )
        all_rules_button.click()

        # Wait until the URL changes to the All Rules page
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.url_contains("all_rules.htm")
        )

        # Wait until the unique element is present
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, "all_rules_container"))
        )
        return AllRulesPage(self.driver)

    def continue_game(self):
        continue_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "entry_continue_button"))
        )
        continue_button.click()