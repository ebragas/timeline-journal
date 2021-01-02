"""Interactive menu"""
import sys
from textwrap import dedent

import pendulum
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

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
            console.print()
            action = self.options.get(choice)
            action()

    def show_stories(self, stories=None):
        """Show all or just the provided stories."""
        if not stories:
            stories = self.timeline.stories

        table = Table(title="Stories")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Start Date", justify="right", style="green")
        table.add_column("Title", style="magenta")

        for story in stories:
            table.add_row(
                str(story.uuid),
                story.start_date.to_datetime_string(),
                story.title
            )

        console.print(table)

    def search_stories(self):
        raise NotImplementedError

    def add_story(self):
        """Create new story and call up editor (Vim)
        https://stackoverflow.com/questions/6309587/call-up-an-editor-vim-from-a-python-script"""
        default = pendulum.now().to_date_string()
        start_date = prompt.ask(f"Start Date (default: {default})")
        title = prompt.ask(f"Title (default: {default})")
        story = self.timeline.add_story(start_date=start_date, title=title)  # TODO: default everything to None and use conditionals to "default"

        # content = self.editor()
        # story.entries.edit()

    def edit_story(self):
        raise NotImplementedError

    def delete_story(self):
        # TODO: use Confirm.ask()
        raise NotImplementedError

    def quit(self):
        console.print("Thank you, come again.\n")
        sys.exit()


if __name__ == "__main__":
    Menu().run()