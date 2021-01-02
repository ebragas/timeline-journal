"""Core API for Timeline Journaling application"""
import pendulum
from uuid import uuid4 as uuid

from .helpers import today_str, parse_datetime_local_tz


class Timeline:
    """The container for your stories"""

    def __init__(self, start_date: str = today_str()):
        self.stories = []
        self.start_date = parse_datetime_local_tz(start_date)

    def add_story(self, *args, **kwargs):
        """Create a new story. Return story and default first entry."""
        story = Story(self, *args, **kwargs)
        self.stories.append(story)
        return story, story.entries[0]  # TODO: provide get() or magic method for slicing

    def list_stories(self):
        """List all available stories.
        # NOTE: Should merge with `search()` and provide no filter?"""
        return list(self.stories)


class Story:
    """A group of 1 or more Entries that create a narrative or should otherwise
    be sequenced."""

    def __init__(
        self,
        timeline: Timeline,
        start_date: str = today_str(),
        title: str = today_str(),
    ):
        self.timeline = timeline
        self.uuid = uuid()
        self.title = title
        # TODO: make property; get from min entry date
        self.start_date = parse_datetime_local_tz(start_date)
        self.entries = []
        self.entries.append(Entry(self, date=start_date))  # default first entry

    def list_entries(self):
        """Return all entries
        # TODO: sort by date"""
        return list(self.entries)

    def add_entry(self, *args, **kwargs):
        entry = Entry(story=self, *args, **kwargs)
        self.entries.append(entry)
        return entry

    def __repr__(self):
        return f'<uuid: {self.uuid} title: "{self.title}" num_entries: {len(self.entries)}>'


class Entry:
    """An component of a story. Where all content is stored/linked"""

    def __init__(self, story: Story, date: str, body: str = "Such empty :("):
        self.story = story
        self.body = body
        self.uuid = uuid()
        self.date = parse_datetime_local_tz(date) if date else pendulum.today()

    def __repr__(self):
        return f'<uuid: {self.uuid} date: {self.date.to_datetime_string()} body: "{self.body[:10]}">'


# # NOTE: dev only
# if __name__ == "__main__":

#     from rich.console import Console

#     console = Console()

#     t = Timeline()
#     t.add_story('2020-02-18', '27th birthday')
#     t.add_story()

#     stories = t.list_stories()
#     console.print(stories)

#     entries = stories[0].list_entries()
#     console.print(entries)
