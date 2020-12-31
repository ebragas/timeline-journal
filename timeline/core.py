"""Core API for Timeline Journaling application"""
import pendulum
from uuid import uuid4 as uuid

from .helpers import today_str, parse_datetime_local_tz


class Timeline:
    """The container for your stories"""
    
    def __init__(self, start_date: str = today_str()):
        self.stories = set()
        self.start_date = parse_datetime_local_tz(start_date)


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
        self.timeline.stories.add(self)
        self.entries = set()
        self.uuid = uuid()
        self.start_date = parse_datetime_local_tz(start_date)
        self.title = title

    def __repr__(self):
        return f'<uuid: {self.uuid} title: "{self.title}" num_entries: {len(self.entries)}>'


class Entry:
    """An component of a story. Where all content is stored/linked"""

    def __init__(self, story: Story, body: str, date: str = None):
        self.story = story
        self.story.entries.add(self)
        self.date = self.story.start_date
        self.body = body



# NOTE: dev only
# if __name__ == "__main__":
#     t = Timeline()
#     s = Story(t)
