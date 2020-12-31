import pendulum
from timeline.timeline import Timeline


def test_timeline_init():
    """Test initialization options"""
    timeline1 = Timeline()
    assert timeline1.start_date == pendulum.today()
    
    timeline2 = Timeline(start_date='1993-02-18')
    assert timeline2.start_date == pendulum.datetime(1993, 2, 18, tz='local')
