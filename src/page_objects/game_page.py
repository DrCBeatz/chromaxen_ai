# src/page_objcts/game_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

WAIT_TIME = 10

class GamePage:
    def __init__(self, driver):
        self.driver = driver
        self.container = driver.find_element(By.ID, "container")
    
    def is_displayed(self) -> bool:
        return self.container.is_displayed()
    
    def is_gameboard_displayed(self) -> bool:
        gameboard_container = self.driver.find_element(By.ID, "gameboard")
        return gameboard_container.is_displayed()

    def get_game_title(self) -> str:
        game_title_element = self.driver.find_element(By.ID, "game_title_display")
        return game_title_element.text
    
    def get_move_counter(self) -> int:
        move_counter = self.driver.find_element(By.ID, "update_counter").text
        return int(move_counter)

    def get_timer_text(self) -> str:
        timer_text = self.driver.find_element(By.ID, "timer").text
        return timer_text
    
    def advance_move(self):
        advance_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "update_button"))
        )
        advance_button.click()
    
    def retreat_move(self):
        retreat_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "retreat_button"))
        )
        retreat_button.click()
    
    def reset_game(self):
        reset_button = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, "reset_button"))
        )
        reset_button.click()
    
    def drag_rule(self, from_row, to_row):
        from_row_id = f"label_{from_row - 1}"
        to_row_id = f"label_{to_row - 1}"

        source_element = self.driver.find_element(By.ID, from_row_id)
        target_element = self.driver.find_element(By.ID, to_row_id)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()