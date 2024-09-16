# src/game_interface.py

from abc import ABC, abstractmethod

class AbstractGameInterface(ABC):
    @abstractmethod
    def entry_page(self):
        pass

    @abstractmethod
    def game_page(self):
        pass

    @abstractmethod
    def view_all_rules_page(self):
        """Navigate to the All Rules page and return its page object."""
        pass