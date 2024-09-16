# src/web_game_interface.py

from page_objects.entry_page import EntryPage
from page_objects.game_page import GamePage
from page_objects.all_rules_page import AllRulesPage
from game_interface import AbstractGameInterface


class WebGameInterface(AbstractGameInterface):
    def __init__(self, driver, url="http://dweeb.ninja/chromaxen/#game"):
        self.driver = driver
        self.driver.get(url)
        self._entry_page = EntryPage(driver)
        self._game_page = GamePage(driver)
        self._all_rules_page = None
    
    @property
    def entry_page(self):
        return self._entry_page

    @property
    def game_page(self):
        return self._game_page
    
    def view_all_rules_page(self):
        """Navigate to the All Rules page and return its page object."""
        self._all_rules_page = self._entry_page.view_all_rules()
        return self._all_rules_page