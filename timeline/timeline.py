import pendulum

class Timeline:
    """The container for your stories"""
    
    def __init__(self, start_date: str = pendulum.today().to_datetime_string()):
        self.stories = []
        self.start_date = pendulum.parse(start_date, tz="local")
