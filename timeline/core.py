"""Core API for Timeline Journaling application"""
import pendulum
from uuid import uuid4 as uuid

from timeline.helpers import today_str, parse_datetime_local_tz


class Timeline:
    """The container for your stories"""

    def __init__(self, start_date: str = today_str()):
        self._stories = []
        self.start_date = parse_datetime_local_tz(start_date)

    def add_story(self, *args, **kwargs):
        """Create a new story. Return story and default first entry."""
        story = Story(self, *args, **kwargs)
        self._stories.append(story)
        return story, story.entries[0]  # TODO: provide get() or magic method for slicing

    def delete_story(self, story):
        """Delete story by id suffix. Doesn't require the entire id as long as 
        it's unique"""
        raise NotImplementedError   

    @property
    def stories(self):
        """List all available stories.
        # NOTE: Should merge with `search()` and provide no filter?"""
        return list(self._stories)


class Story:
    """A group of 1 or more Entries that create a narrative or should otherwise
    be sequenced."""

    def __init__(
        self,
        timeline: Timeline,
        start_date: str = None,
        title: str = None,
    ):
        self.timeline = timeline
        self.uuid = uuid()
        title = today_str() if not title else title
        self.title = title
        # TODO: make property; get from min entry date
        start_date = today_str() if not start_date else start_date
        self.start_date = parse_datetime_local_tz(start_date)
        self._entries = []
        self._entries.append(Entry(self, date=start_date))  # default first entry

    @property
    def entries(self):
        """Return all entries
        # TODO: sort by date"""
        return list(self._entries)

    def add_entry(self, *args, **kwargs):
        entry = Entry(story=self, *args, **kwargs)
        self._entries.append(entry)
        return entry

    def __repr__(self):
        return f'<Story uuid: {self.uuid} title: "{self.title}" num_entries: {len(self.entries)}>'


class Entry:
    """An component of a story. Where all content is stored/linked"""

    def __init__(self, story: Story, date: str, body: str = ""):
        self.story = story
        self.body = body
        self.uuid = uuid()
        self.date = parse_datetime_local_tz(date) if date else pendulum.today()

    def __repr__(self):
        return f'<Entry uuid: {self.uuid} date: {self.date.to_datetime_string()} body: "{self.body[:10]}">'


# NOTE: dev only
if __name__ == "__main__":

    from rich.console import Console

    console = Console()

    t = Timeline()
    t.add_story('2020-02-18', '27th birthday')
    t.add_story()

    console.print(t.stories)
    console.print(t.stories[0].entries)
