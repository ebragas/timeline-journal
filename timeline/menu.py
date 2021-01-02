"""Interactive menu"""
import sys
from textwrap import dedent

from rich.console import Console
from rich.prompt import Prompt, Confirm

from core import Timeline


console = Console()
prompt = Prompt()

class Menu:
    def __init__(self):
        
        self.timeline = Timeline()
        
        self.options = {
            "1": self.list_stories,
            "2": self.search_stories,
            "3": self.add_story,
            "4": self.edit_story,
            "5": self.delete_story,
            "0": self.quit
        }

    def display_menu(self):
        """Print menu to terminal."""
        menu = """
        Main Menu:
        1) List stories
        2) Search stories
        3) Add story
        4) Edit story
        5) Delete story
        0) Quit
        """
        console.print(dedent(menu), justify="left")

    def run(self):
        """Main menu"""
        while True:
            self.display_menu()
            # choice = input("Choose an option: ")
            choice = prompt.ask("Choose an option", choices=self.options.keys())
            action = self.options.get(choice)
            if action:
                action()
            else:
                console.print("Not a valid option.")

    def list_stories(self):
        raise NotImplementedError

    def search_stories(self):
        raise NotImplementedError

    def add_story(self):
        raise NotImplementedError

    def edit_story(self):
        raise NotImplementedError

    def delete_story(self):
        # TODO: use Confirm.ask()
        raise NotImplementedError
    
    def quit(self):
        print("Thank you, come again.")
        sys.exit()


if __name__ == "__main__":
    Menu().run()