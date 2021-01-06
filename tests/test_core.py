import pytest

from timeline import default_timeline
from timeline.core import Timeline, Entry
import pendulum


## Fixtures
@pytest.fixture
def empty_timeline_fixture():
    t = Timeline()
    yield t
    del t

@pytest.fixture
def timeline_w_blank_entry_fixture(empty_timeline_fixture):
    t = empty_timeline_fixture
    _ = t.add_entry()
    return t


## Entry Class Tests
def test_default_entry(timeline_w_blank_entry_fixture):
    t = timeline_w_blank_entry_fixture
    assert len(t.entries) == 1
    blank_entry = t.entries[0]
    assert isinstance(blank_entry.start_dt, pendulum.DateTime)
    assert isinstance(blank_entry.end_dt, pendulum.DateTime)
    assert blank_entry.start_dt.to_day_datetime_string() == blank_entry.title


## Timeline Class Tests
# TODO:
def test_default_timeline():
    assert isinstance(default_timeline, Timeline)

def test_timeline_add_story(empty_timeline_fixture):
    """Test initialization options of Timeline"""
    t = empty_timeline_fixture
    new_entry = t.add_entry(
        start_dt="1993-02-18",
        # default end_dt same as start_dt
        title="Day 1",
        body="The day I was born."
    )
    assert isinstance(new_entry, Entry)
    assert isinstance(new_entry.created_dt, pendulum.DateTime)
    assert new_entry.created_dt == new_entry.modified_dt
