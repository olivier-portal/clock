def update_time(current_time, time_format):        
    if time_format == 1:
        hours, minutes, seconds, am_pm = current_time
    else:
        hours, minutes, seconds = current_time

    # Ajouter une seconde
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1
    if minutes >= 60:
        minutes = 0
        hours += 1

    if time_format == 1:  # Gestion du format 12h
        if hours > 12:
            hours = 1
        if hours == 12 and minutes == 0 and seconds == 0:
            am_pm = "PM" if am_pm == "AM" else "AM"
        return (hours, minutes, seconds, am_pm)
    else:  # Gestion du format 24h
        if hours >= 24:
            hours = 0
        return (hours, minutes, seconds)
