# src/game_interface.py

from abc import ABC, abstractmethod

class AbstractGameInterface(ABC):
    @abstractmethod
    def start_new_game(self):
        pass

    @abstractmethod
    def click_random_game(self):
        pass

    @abstractmethod
    def view_all_rules(self):
        pass

    @abstractmethod
    def continue_game(self):
        pass