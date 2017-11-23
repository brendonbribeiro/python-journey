def minutes_to_hours(minutes):
    return minutes/60

def seconds_to_minutes(seconds):
    return seconds/60

def seconds_to_hours(seconds, [bla]):
    minutes = seconds_to_minutes(seconds)
    hours = minutes_to_hours(minutes)
    return hours

print(seconds_to_hours(7200))
