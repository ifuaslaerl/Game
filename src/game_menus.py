""" Module providing Hanoi Game Menu. """

from src.menu import SelectionMenu
from games import hanoi, pacman, robery

SCREEN_SIZE = (1000, 500)
OPTIONS = ["Play", "Walkthrough", "Go Back"]
TITLE = "Hanoi Menu"

class HanoiMenu(SelectionMenu):
    """ Hanoi Menu. """

    def __init__(self, main_menu):
        super().__init__(SCREEN_SIZE, OPTIONS, TITLE)
        self.callback = main_menu

    def select_option(self):
        """ Function to select option in menu. """
        option = self.options[self.selected_option]

        match option:
            case "Play":
                self.running_option = hanoi.Hanoi()
            case "Walkthrough":
                self.running_option = Bot()
            case "Go Back":
                self.running_option = self.callback() # TODO make this work

class PacmanMenu(SelectionMenu):
    """ Hanoi Menu. """

    def __init__(self, main_menu):
        super().__init__(SCREEN_SIZE, OPTIONS, TITLE)
        self.callback = main_menu

    def select_option(self):
        """ Function to select option in menu. """
        option = self.options[self.selected_option]

        match option:
            case "Play":
                self.running_option = pacman.Pacman()
            case "Walkthrough":
                self.running_option = Bot()
            case "Go Back":
                self.running_option = self.callback()

class RoberyMenu(SelectionMenu):
    """ Hanoi Menu. """

    def __init__(self, main_menu):
        super().__init__(SCREEN_SIZE, OPTIONS, TITLE)
        self.callback = main_menu

    def select_option(self):
        """ Function to select option in menu. """
        option = self.options[self.selected_option]

        match option:
            case "Play":
                self.running_option = robery.Robery()
            case "Walkthrough":
                self.running_option = Bot()
            case "Go Back":
                self.running_option = self.callback()
