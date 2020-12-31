"""Helper functions"""
import pendulum


def today_str():
    """Returns today's date formatted as datetime string."""
    return pendulum.today().to_datetime_string()

def parse_datetime_local_tz(datetime_str):
    """Parse datetime string to pendulum.datetime in local timezone."""
    return pendulum.parse(datetime_str, tz="local")

