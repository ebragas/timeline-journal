"""Core API for Timeline Journaling application"""
import pendulum
from uuid import uuid4 as uuid

from timeline.helpers import now_str, today_str, parse_dt_local_tz


class Timeline:
    """The container for your stories"""

    def __init__(self):
        self._entries = {}

    @property
    def entries(self):
        return list(self._entries.values())
    
    def add_entry(self, *args, **kwargs):
        """Create a new story. Return story and default first entry."""
        entry = Entry(*args, **kwargs)  # NOTE: not sure this is good
        self._entries[entry.uuid] = entry
        return entry

    def delete_story(self, story):
        """Delete story by id suffix. Doesn't require the entire id as long as 
        it's unique"""
        raise NotImplementedError


class Entry:
    """An entry on the timeline; where all content is stored and linked."""

    def __init__(
        self,
        start_dt: str = None,
        end_dt: str = None,
        title: str = None,
        body: str = None
    ):
        now = pendulum.now()
        self.start_dt = parse_dt_local_tz(start_dt) if start_dt else now
        self.end_dt = parse_dt_local_tz(end_dt) if end_dt else now
        self.created_dt = now
        self.modified_dt = now
        self.title = title if title else self.start_dt.to_day_datetime_string()
        self.body = body
        self.uuid = str(uuid())

    def __repr__(self):
        return f'<Entry uuid: {self.uuid} start_dt: {self.start_dt.to_datetime_string()} body: "{self.body}">'


# NOTE: dev only
if __name__ == "__main__":

    from rich.console import Console

    console = Console()

    t = Timeline()
    t.add_story('2020-02-18', '27th birthday')
    t.add_story()

    console.print(t.stories)
    console.print(t.stories[0].entries)
