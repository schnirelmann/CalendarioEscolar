def test_can_events_coexist():
    event1 = Event(
        subject="Math",
        room="101",
        professor="Antonio",
        schedule=("Monday", "10:00-11:00"),
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
        schedule=("Monday", "10:00-11:00"),
        group="A"
    )
    event5 = Event(
        subject="Math",
        room="102",
        professor="Maria",
        schedule=("Monday", "10:00-11:00"),
        group="B"
    )

    # Test 1: Check if events with different subjects, professors, rooms, and groups can coexist
    assert can_events_coexist(event1, event2) == False

    # Test 2: Check if events with the same subject, different professors, and different rooms can coexist
    assert can_events_coexist(event1, event3) == False

    # Test 3: Check if identical events can coexist
    assert can_events_coexist(event1, event4) == True

    # Test 4: Check if events with the same subject, different professors, and the same room can coexist
    assert can_events_coexist(event1, event5) == True

    print("All tests passed!")

test_can_events_coexist()