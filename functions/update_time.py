def update_time(current_time, time_format):
    hours, minutes, seconds = current_time[:3]
    
    # Incrémente les secondes
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if time_format == 1:  # Format 12h
        if hours == 12:
            current_time = (hours, minutes, seconds, "PM" if current_time[3] == "AM" else "AM")
        elif hours > 12:
            hours -= 12
    elif time_format == 2:  # Format 24h
        if hours == 24:
            hours = 0
    
    return (hours, minutes, seconds) + current_time[3:] if time_format == 1 else (hours, minutes, seconds)