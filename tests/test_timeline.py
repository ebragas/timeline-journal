import pendulum
from timeline.timeline import Timeline, Story


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
    timeline = Timeline()
    story1 = Story(timeline=timeline)
    assert story1.start_date == pendulum.today()
    assert story1.title == pendulum.today().to_datetime_string()
    assert str(story1).endswith("num_entries: 0>")
    assert len(timeline.stories) == 1

    story2 = Story(timeline=timeline, start_date="1994-02-18", title="My first birthday")
    assert story2.start_date == pendulum.datetime(1994, 2, 18, tz="local")
    assert story2.title == "My first birthday"
    assert len(timeline.stories) == 2