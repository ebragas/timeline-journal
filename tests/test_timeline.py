import pendulum
from timeline.core import Timeline, Story, Entry


## Timeline Class ##
def test_timeline_init():
    """Test initialization options of Timeline"""
    timeline1 = Timeline()
    assert timeline1.start_date == pendulum.today()

    timeline2 = Timeline(start_date="1993-02-18")
    assert timeline2.start_date == pendulum.datetime(1993, 2, 18, tz="local")


## Story Class ##
def test_story_init():
    """Test initilization options of Story"""
    # import pdb; pdb.set_trace()
    timeline = Timeline()
    story1, _ = timeline.add_story()
    assert story1.start_date == pendulum.today()
    assert story1.title == pendulum.today().to_datetime_string()
    assert str(story1).endswith("num_entries: 1>")
    assert len(timeline.stories) == 1

    story2, _ = timeline.add_story(start_date="1994-02-18", title="My first birthday")
    assert story2.start_date == pendulum.datetime(1994, 2, 18, tz="local")
    assert story2.title == "My first birthday"
    assert len(timeline.stories) == 2


## Entry Class ##
def test_entry_init():
    """Test initilization options of Entry"""
    timeline = Timeline()
    story, default_entry = timeline.add_story(start_date="1993-02-18", title="The beginning")
    assert len(story.list_entries()) == 1
    story.add_entry(date="2021-01-01", body="The first day of the new year.")
    assert len(story.list_entries()) == 2
