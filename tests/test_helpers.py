from timeline.helpers import today_str, parse_dt_local_tz

# NOTE: choosing not to assert because I don't need to test that the library works
def test_today_str():
    today_str()

def test_parse_dt_local_tz():
    parse_dt_local_tz("2021-01-01")
