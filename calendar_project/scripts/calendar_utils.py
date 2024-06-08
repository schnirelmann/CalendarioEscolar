from event_class import Event
from datetime import datetime
from itertools import combinations

def parse_time(time_str):
    """Helper function to parse time from HH:MM format."""
    return datetime.strptime(time_str, '%H:%M').time()

def schedules_collide(schedule1, schedule2):
    """Helper function to check if schedules collide."""
    day1, time_range1 = schedule1
    day2, time_range2 = schedule2

    if day1 != day2:
        return False  # Different days, no collision
    
    start_time1, end_time1 = time_range1.split('-')
    start_time2, end_time2 = time_range2.split('-')

    start_time1 = parse_time(start_time1)
    end_time1 = parse_time(end_time1)
    start_time2 = parse_time(start_time2)
    end_time2 = parse_time(end_time2)

    return max(start_time1, start_time2) < min(end_time1, end_time2)

def can_events_coexist(event1, event2):
    """
    Check if two events can coexist in a calendar.

    Parameters:
    - event1: The first Event instance.
    - event2: The second Event instance.

    Returns:
    - True if the events can coexist, False otherwise. If they are the same event, returns True with a notification.
    """
    # Check if the events are identical
    if (event1.subject == event2.subject and event1.room == event2.room and
        event1.professor == event2.professor and event1.schedule == event2.schedule and
        event1.group == event2.group):
        print("Note: The events are identical.")
        return True

    # Check if the schedules collide
    if schedules_collide(event1.schedule, event2.schedule):
        # Check if the professors are the same
        if event1.professor == event2.professor:
            return False
        
        # Check if the rooms are the same
        if event1.room == event2.room:
            return False
        
        # Check if the groups are the same
        if event1.group == event2.group:
            return False

    # Check if the subjects are the same
    if event1.subject == event2.subject:
        if (event1.professor != event2.professor and event1.room != event2.room):
            return True
        if event1.professor == event2.professor and not schedules_collide(event1.schedule, event2.schedule):
            return True
        if (event1.professor != event2.professor and event1.room == event2.room and
            not schedules_collide(event1.schedule, event2.schedule)):
            return True
        return False

    return True  # They can coexist if there are no conflicts

def find_conflicting_events(events):
    """
    Find pairs of events that cannot coexist and return conflict descriptions.

    Parameters:
    - events: A list of Event instances.

    Returns:
    - A list of strings describing which events cannot coexist.
    """
    conflicts = []
    for i, (event1, event2) in enumerate(combinations(events, 2), start=1):
        if not can_events_coexist(event1, event2):
            idx1 = events.index(event1) + 1
            idx2 = events.index(event2) + 1
            conflicts.append(f"Event {idx1} conflicts with Event {idx2}")
    return conflicts

# Example usage (for testing)
if __name__ == "__main__":
    class Event:
        def __init__(self, subject, room, professor, schedule, group):
            self.subject = subject
            self.room = room
            self.professor = professor
            self.schedule = schedule
            self.group = group

        def __repr__(self):
            return f"Event(subject={self.subject}, room={self.room}, professor={self.professor}, schedule={self.schedule}, group={self.group})"

    event1 = Event(
        subject="Math",
        room="101",
        professor="Antonio",
        schedule=("Monday", "09:00-11:00"),
        group="A"
    )
    event2 = Event(
        subject="Physics",
        room="101",
        professor="Maria",
        schedule=("Monday", "10:00-11:00"),
        group="B"
    )
    event3 = Event(
        subject="Chemistry",
        room="102",
        professor="Rocio",
        schedule=("Monday", "10:00-11:00"),
        group="A"
    )
    event4 = Event(
        subject="Math",
        room="101",
        professor="Antonio",
        schedule=("Monday", "09:00-11:00"),
        group="A"
    )
    event5 = Event(
        subject="Math",
        room="102",
        professor="Maria",
        schedule=("Monday", "10:00-11:00"),
        group="B"
    )

    events = [event1, event2, event3, event4, event5]

    conflicts = find_conflicting_events(events)
    if conflicts:
        print("Conflicting events found:")
        for conflict in conflicts:
            print(conflict)
    else:
        print("All events can coexist.")