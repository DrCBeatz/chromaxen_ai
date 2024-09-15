# tests/test_web_game.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_game_interface import WebGameInterface


@pytest.fixture(scope="class")
def driver():
    """Fixture to set up and tear down the WebDriver instance."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def web_game(driver):
    """Fixture to initialize the WebGameInterface."""
    return WebGameInterface(driver)

def test_start_new_game(web_game):
    web_game.start_new_game()
    # add assertions, e.g. if game board is being displayed
    assert "gameboard_container" in web_game.driver.page_source

def test_click_random_game(web_game):
    web_game.click_random_game()
    assert "gameboard_container" in web_game.driver.page_source

def test_view_all_rules(web_game):
    web_game.view_all_rules()
    # Add asserts to chck if "All Rules" page is loaded
    assert "all_rules.htm" in web_game.driver.current_url

# def test_continue_game(web_game):
#     web_game.continue_game()
#     assert "gameboard_container" in web_game.driver.page_source