import pendulum
from uuid import uuid4 as uuid


def today_str():
    return pendulum.today().to_datetime_string()


class Timeline:
    """The container for your stories"""
    
    def __init__(self, start_date: str = today_str()):
        self.stories = set()
        self.start_date = pendulum.parse(start_date, tz="local")


class Story:
    """A group of 1 or more Entries that create a narrative or should otherwise
    be grouped"""

    def __init__(
        self, 
        timeline: Timeline,
        start_date: str = today_str(),
        title: str = today_str(),
    ):
        self.timeline = timeline
        self.timeline.stories.add(self)
        self.entries = []
        self.uuid = uuid()
        self.start_date = pendulum.parse(start_date, tz="local")
        self.title = title

    def __repr__(self):
        return f'<uuid: {self.uuid} title: "{self.title}" num_entries: {len(self.entries)}>'


# NOTE: dev only
if __name__ == "__main__":
    t = Timeline()
    s = Story(t)
