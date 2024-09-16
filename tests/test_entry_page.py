# tests/test_entry_page.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects.entry_page import EntryPage
from page_objects.game_page import GamePage
from page_objects.all_rules_page import AllRulesPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

@pytest.fixture(scope="function")
def driver():
    """Fixture to set up and tear down the WebDriver instance."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://dweeb.ninja/chromaxen/#game")
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def entry_page(driver):
    """Fixture to initialize the EntryPage."""
    return EntryPage(driver)

def test_entry_page_is_displayed(entry_page):
    """Test that the Entry Page is displayed correctly."""
    assert entry_page.is_displayed(), "Entry Page should be displayed when navigating to the URL."

def test_start_new_game(entry_page):
    """Test that starting a new game navigates to the Game Page."""
    entry_page.start_new_game()
    game_page = GamePage(entry_page.driver)
    assert game_page.is_displayed(), "Game Page should be displayed after"

def test_click_random_game(entry_page):
    """Test that clicking the random game button navigates to the Game Page with a random game."""
    entry_page.click_random_game()
    game_page = GamePage(entry_page.driver)
    assert game_page.is_displayed(), "Game page should be displayed after starting a random game"
    assert not entry_page.is_displayed(), "Entry page should not be displayed after starting a random game"

def test_view_all_rules(entry_page):
    """Test that viewing all rules navigates to the All Rules Page."""
    all_rules_page = entry_page.view_all_rules()
    assert all_rules_page.is_displayed(), "All Rules pag should be displayed after clicking 'View All Rules'"
    assert not entry_page.is_displayed(), "Entry page should not be displayed after navigating to All Rules page"
