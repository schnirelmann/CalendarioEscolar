import re

# Define global allowed lists and days of the week
ALLOWED_SUBJECTS = ["Math", "Physics", "Chemistry", "Biology"]
ALLOWED_ROOMS = ["101", "102", "103", "104"]
ALLOWED_PROFESSORS = ["Antonio", "Rocio", "Maria", "Francisco"]
ALLOWED_GROUPS = ["A", "B", "C", "D"]
DAYS_OF_WEEK = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

class Event:
    def __init__(self, subject, room, professor, schedule, group):
        if subject not in ALLOWED_SUBJECTS:
            raise ValueError(f"Invalid subject: {subject}. Must be one of {ALLOWED_SUBJECTS}")
        
        if room not in ALLOWED_ROOMS:
            raise ValueError(f"Invalid room: {room}. Must be one of {ALLOWED_ROOMS}")
        
        if professor not in ALLOWED_PROFESSORS:
            raise ValueError(f"Invalid professor: {professor}. Must be one of {ALLOWED_PROFESSORS}")
        
        if group not in ALLOWED_GROUPS:
            raise ValueError(f"Invalid group: {group}. Must be one of {ALLOWED_GROUPS}")
        
        validated_schedule = self._validate_schedule(schedule)
        if validated_schedule is None:
            raise ValueError(f"Invalid schedule: {schedule}. Must be a tuple (day_of_the_week, time) with time in HH:MM format in 24-hour format")

        self.subject = subject
        self.room = room
        self.professor = professor
        self.schedule = validated_schedule
        self.group = group

    def _validate_schedule(self, schedule):
        time_pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')  # HH:MM format in 24-hour time
        
        if isinstance(schedule, tuple) and len(schedule) == 2:
            day, time = schedule
            if day not in DAYS_OF_WEEK:
                raise ValueError(f"Invalid day: {day}. Must be one of {DAYS_OF_WEEK}")
            if not isinstance(time, str) or not time_pattern.match(time):
                raise ValueError(f"Invalid time format: {time}. Must be in HH:MM format in 24-hour format")
            return schedule
        raise ValueError(f"Invalid schedule format: {schedule}. Must be a tuple (day_of_the_week, time)")

# Example test cases
def test_event_creation():
    try:
        event = Event(
            subject="Math",
            room="101",
            professor="Antonio",
            schedule=("Monday", "10:00"),
            group="A"
        )
        print("Event created successfully")
    except ValueError as e:
        print(e)

def test_invalid_schedule():
    try:
        event = Event(
            subject="Math",
            room="101",
            professor="Antonio",
            schedule=("InvalidDay", "25:00"),
            group="A"
        )
    except ValueError as e:
        print(e)

# Run the test cases
if __name__ == "__main__":
    test_event_creation()
    test_invalid_schedule()