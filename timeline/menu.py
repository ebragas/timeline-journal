"""Interactive menu"""
import sys
import os
from textwrap import dedent
from tempfile import NamedTemporaryFile
from subprocess import call

import pendulum
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

from core import Timeline


EDITOR = os.environ.get('EDITOR', 'vim')

console = Console()
prompt = Prompt()

class Menu:
    def __init__(self):

        self.timeline = Timeline()

        self.options = {
            "1": self.show_stories,
            "2": self.display_story,
            "3": self.search_stories,
            "4": self.add_story,
            "5": self.interactive_edit_story,
            "6": self.delete_story,
            "0": self.quit
        }

    def display_menu(self):
        """Print menu to terminal."""
        menu = """
        Main Menu:
        1) Show all stories
        2) Read story
        3) Search stories
        4) Add story
        5) Edit story
        6) Delete story
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

    def display_story(self):
        """Print to terminal."""
        story_id = prompt.ask("Story ID (last 7 letters sufficient)")
        story = self._find_story_by_id(story_id)
        
        # console.print("\nTitle:\t{story.title}")
        console.print()
        console.rule(story.title)
        console.print()
        for entry in story.entries:
            console.print(f"Date:\t{entry.date.to_datetime_string()}")
            console.print(f"Body:\n{entry.body}\n")
        console.rule()

    def search_stories(self):
        raise NotImplementedError

    def add_story(self):
        """Create new story and call up editor (Vim)
        https://stackoverflow.com/questions/6309587/call-up-an-editor-vim-from-a-python-script"""
        default = pendulum.now().to_date_string()
        start_date = prompt.ask(f"Start Date (default: {default})")
        title = prompt.ask(f"Title (default: {default})")
        
        story, default_entry = self.timeline.add_story(
            start_date=start_date, 
            title=title
        )
        default_entry.body = self.open_editor(default_entry.body)

    def open_editor(self, initial_text: str = None):
        """Opens default editor starting with initial_text and returns edited
        text on editor closure"""
        with NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_text.encode("utf-8"))
            tf.flush()
            call([EDITOR, tf.name])
            text = open(tf.name, "r").read()

        return text

    def interactive_edit_story(self, story_id: str = None):
        """Edit a story by editing the entry(s)."""
        if not story_id:
            story_id = prompt.ask("Story ID (last 7 letters sufficient)")
        story = self._find_story_by_id(story_id)
        entry = story.entries[0]  # TODO: determine how to edit multiple entries later
        entry.body = self.open_editor(entry.body)

    def delete_story(self):
        # Search for story
        # Show storie(s) to be deleted
        # TODO: use Confirm.ask()
        # Delete
        raise NotImplementedError

    def _find_story_by_id(self, story_id: str):
        """Return first matching story by story_id.
        Matches based on ID string ending"""
        for story in self.timeline.stories:
            if str(story.uuid).endswith(story_id):
                return story

    def _editor(self, text_to_edit: str = None):
        """Open the users default editor with the provided text (if any), allow
        them to edit, then return the contents."""
        

    def quit(self):
        console.print("Thank you, come again.\n")
        sys.exit()


if __name__ == "__main__":
    Menu().run()