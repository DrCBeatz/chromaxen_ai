# tests/test_web_game.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from web_game_interface import WebGameInterface
from selenium.webdriver.common.by import By
from time import sleep

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
    """Test that starting a new game transitions to the game page correctly"""
    web_game.entry_page.start_new_game()
    
    assert web_game.game_page.is_displayed(), "Game page should be displayed after starting a new game"

    assert not web_game.entry_page.is_displayed(), "Entry page should not be displayed after starting a new game"

    assert web_game.game_page.is_gameboard_displayed(), "Gameboard should be displayed after starting a new game"

    assert web_game.game_page.get_move_counter() == 0, "Move counter should be 0 after starting a new game"

    assert web_game.game_page.get_timer_text() == "00:00", "Timer should be 00:00 after starting a new game"
    

def test_click_random_game(web_game):
    web_game.entry_page.click_random_game()  
    assert "gameboard_container" in web_game.driver.page_source

    # Wait until the game page is displayed
    assert web_game.game_page.is_displayed(), "Game page should be displayed after starting a random game"

    # Assert that the entry page is not displayed
    assert not web_game.entry_page.is_displayed(), "Entry page should not be displayed after starting a random game"

    # Assert that the gameboard is displayed
    assert web_game.game_page.is_gameboard_displayed(), "Gameboard should be displayed after starting a random game"

    # Assert that the move counter is 0
    assert web_game.game_page.get_move_counter() == 0, "Move counter should be 0 after starting a random game"

    # Assert that the timer is reset
    assert web_game.game_page.get_timer_text() == "00:00", "Timer should be 00:00 after starting a random game"

    # Assert that the game title is displayed
    game_title = web_game.game_page.get_game_title()
    expected_title = "Random Game"
    assert game_title == expected_title, f"Game title should be {expected_title} but was {game_title}"

def test_all_rules_page(web_game):
    """Test that the All Rules page is accessible and functions correctly."""
    all_rules_page = web_game.view_all_rules_page()
    assert all_rules_page.is_displayed(), "All Rules page should be displayed after clicking 'All Rules'"

    # Check that the rule list is not empty
    rule_list = all_rules_page.get_rule_list()
    assert len(rule_list) > 0, "Rule list should not be empty"

    # Verify you can select a rule and the rule details are displayed
    all_rules_page.select_rule(1)
    rule_title = all_rules_page.get_current_rule_title()
    expected_title = "rule1"  # Adjust this value based on your application's expected title
    assert rule_title == expected_title, f"Rule title should be '{expected_title}', but got '{rule_title}'"

    # Test navigation buttons
    previous_rule_title = rule_title
    all_rules_page.show_next_rule()
    next_rule_title = all_rules_page.get_current_rule_title()
    assert next_rule_title != previous_rule_title, "Next rule should be different from the current rule"

    # Return to the list of all rules
    all_rules_page.back_to_rules()
    assert all_rules_page.is_displayed(), "Should be back to the All Rules list"


def test_advance_move(web_game):
    web_game.entry_page.start_new_game()

    assert web_game.game_page.is_displayed(), "Game page should be displayed after starting a new game"

    assert web_game.game_page.is_gameboard_displayed(), "Gameboard should be displayed after starting a new game"

    web_game.game_page.advance_move()

    assert web_game.game_page.get_move_counter() == 1, "Move counter should be 1 after making first move"


# def test_retreat_move(web_game):
#     web_game.entry_page.start_new_game()  
#     web_game.game_page.advance_move()  
#     web_game.game_page.retreat_move()  
#     assert True

# def test_reset_game(web_game):
#     web_game.entry_page.start_new_game()  
#     web_game.game_page.reset_game()  
#     assert True

# def test_drag_rule(web_game):
#     web_game.entry_page.start_new_game()  
#     web_game.game_page.drag_rule(from_row=1, to_row=2)  
#     assert True
