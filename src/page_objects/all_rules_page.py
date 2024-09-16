# src/page_objects/all_rules_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 10

class AllRulesPage:
    def __init__(self, driver):
        self.driver = driver

    def is_displayed(self) -> bool:
        """Check if the All Rules page is displayed."""
        try:
            return WebDriverWait(self.driver, WAIT_TIME).until(
                EC.visibility_of_element_located((By.ID, "all_rules_container"))
            ).is_displayed()
        except:
            return False

    def get_rule_list(self) -> list:
        """Retrieve the list of rules displayed on the page."""
        rule_elements = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "rule"))
        )
        return rule_elements

    def select_rule(self, rule_number):
        """Select a rule to view its details."""
        rule_id = f"rule{rule_number}"
        rule_element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.element_to_be_clickable((By.ID, rule_id))
        )
        rule_element.click()
        # Wait until the rule display is updated with the selected rule
        expected_rule_title = f"rule{rule_number}"
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.text_to_be_present_in_element((By.ID, "rule_display"), expected_rule_title)
        )

    def show_prev_rule(self):
        """Navigate to the previous rule."""
        current_rule_title = self.get_current_rule_title()
        prev_button = self.driver.find_element(By.XPATH, "//span[text()='prev']")
        prev_button.click()
        # Wait until the rule title changes
        WebDriverWait(self.driver, WAIT_TIME).until(
            lambda driver: self.get_current_rule_title() != current_rule_title
        )

    def show_next_rule(self):
        """Navigate to the next rule."""
        current_rule_title = self.get_current_rule_title()
        next_button = self.driver.find_element(By.XPATH, "//span[text()='next']")
        next_button.click()
        # Wait until the rule title changes
        WebDriverWait(self.driver, WAIT_TIME).until(
            lambda driver: self.get_current_rule_title() != current_rule_title
        )

    def back_to_rules(self):
        """Return to the list of all rules."""
        all_rules_button = self.driver.find_element(By.XPATH, "//span[text()='all_rules']")
        all_rules_button.click()
        # Wait until the all_rules_container is visible again
        WebDriverWait(self.driver, WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, 'all_rules_container'))
        )

    def refresh_rule(self):
        """Refresh the current rule display."""
        refresh_button = self.driver.find_element(By.XPATH, "//span[text()='refresh']")
        refresh_button.click()
        # Optionally wait for any specific condition if needed

    def get_current_rule_title(self):
        """Retrieve the title of the currently displayed rule."""
        rule_title_element = WebDriverWait(self.driver, WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, "rule_display"))
        )
        return rule_title_element.text
