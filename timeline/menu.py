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
from exceptions import EntryNotFoundException


EDITOR = os.environ.get('EDITOR', 'vim')

console = Console()
prompt = Prompt()

class Menu:
    def __init__(self):

        self.timeline = Timeline()

        self.options = {
            "1": self.show_entries,
            "2": self.display_entry,
            "3": self.search_entries,
            "4": self.add_entry,
            "5": self.interactive_edit_entry,
            "6": self.delete_entry,
            "0": self.quit
        }

    def display_menu(self):
        """Print menu to terminal."""
        menu = """
        Main Menu:
        1) Show all entries
        2) Read entry
        3) Search entries
        4) Add entry
        5) Edit entry
        6) Delete entry
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

    def show_entries(self, entries=None):
        """Show all or just the provided stories."""
        if not entries:
            entries = self.timeline.entries

        table = Table(title="Entries")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Start Date", justify="right", style="green")
        table.add_column("End Date", justify="right", style="green")
        table.add_column("Title", style="magenta")

        for entry in entries:
            table.add_row(
                entry.uuid,
                entry.start_dt.to_datetime_string(),
                entry.end_dt.to_datetime_string(),
                entry.title
            )

        console.print(table)

    def display_entry(self, entry=None, entry_id: str=None):
        """Print to terminal."""
        if not entry:
            if not entry_id:
                entry_id = prompt.ask("Entry ID (last 7 letters sufficient)")
                try:
                    entry = self._find_entry_by_id(entry_id)
                except EntryNotFoundException as e:
                    console.print(e.args[0])
                    return
        
        console.print()
        console.rule(entry.title)
        console.print()
        console.print(f"Start Date:\t{entry.start_dt.to_datetime_string()}")
        console.print(f"End Date:\t{entry.end_dt.to_datetime_string()}")
        console.print(f"Body:\n{entry.body}")
        console.rule()

    def search_entries(self):
        # TODO: implement
        raise NotImplementedError

    def add_entry(self):
        """Create new entry and call up editor (Vim)
        https://stackoverflow.com/questions/6309587/call-up-an-editor-vim-from-a-python-script"""
        entry_args = {}
        entry_args["start_dt"] = prompt.ask(f"Start Date")
        entry_args["title"] = prompt.ask(f"Title")
        entry_args = {k: v for k, v in entry_args.items() if v}
        
        entry = self.timeline.add_entry(
            **entry_args
        )
        entry.body = self._editor(entry.body)
        self.display_entry(entry=entry)

    def _editor(self, initial_text: str=None):
        """Opens default editor starting with initial_text and returns edited
        text on editor closure"""
        initial_text = initial_text or ""
        
        with NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_text.encode("utf-8"))
            tf.flush()
            call([EDITOR, tf.name])
            text = open(tf.name, "r").read()

        return text

    def interactive_edit_entry(self, entry_id: str=None):
        """Edit a entry by editing the entry(s)."""
        if not entry_id:
            entry_id = prompt.ask("entry ID (last 7 letters sufficient)")
        try:
            entry = self._find_entry_by_id(entry_id)
            entry.body = self._editor(entry.body)
        except EntryNotFoundException as e:
            console.print(e.args[0])

    def delete_entry(self):
        # Search for entry
        # Show storie(s) to be deleted
        # TODO: use Confirm.ask()
        # Delete
        raise NotImplementedError

    def _find_entry_by_id(self, entry_id: str):
        """Return first matching entry by entry_id.
        Matches based on ID string ending"""
        try:
            return self.timeline._entries[entry_id]
        except KeyError as e:
            raise EntryNotFoundException(f"No Entry found with identifier matching: {entry_id}")

    def quit(self):
        console.print("Thank you, come again.\n")
        sys.exit()


if __name__ == "__main__":
    Menu().run()