"""Helper functions"""
import pendulum


def now_str():
    """Returns current dt in ISO 8601 string format."""
    return pendulum.now().to_datetime_string()

def today_str():
    """Returns today's date formatted as dt string."""
    return pendulum.today().to_datetime_string()

def parse_dt_local_tz(dt_str: str):
    """Parse dt string to pendulum.dt in local timezone."""
    return pendulum.parse(dt_str, tz="local")
