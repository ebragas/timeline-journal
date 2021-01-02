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
            "1": self.show_stories,
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
        1) Show all stories
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
            choice = prompt.ask("Choose an option", choices=self.options.keys())
            action = self.options.get(choice)
            action()

    def show_stories(self, stories=None):
        """Show all or just the provided stories."""
        if not stories:
            stories = self.timeline.stories
        for story in stories:
            console.print(story)

    def search_stories(self):
        raise NotImplementedError

    def add_story(self):
        """Create new story and call up editor (Vim)
        https://stackoverflow.com/questions/6309587/call-up-an-editor-vim-from-a-python-script"""
        start_date = prompt.ask("Start Date")
        title = prompt.ask("Title")
        story = self.timeline.add_story(start_date=start_date, title=title)

        # content = self.editor()
        # story.entries.edit()

    def edit_story(self):
        raise NotImplementedError

    def delete_story(self):
        # TODO: use Confirm.ask()
        raise NotImplementedError
    
    def quit(self):
        console.print("Thank you, come again.")
        sys.exit()


if __name__ == "__main__":
    Menu().run()