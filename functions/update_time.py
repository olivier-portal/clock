def update_time(current_time):        
    while True:
        # stock hours, minutes and seconds
        hours, minutes, seconds = current_time
        
        # add a second for update
        seconds += 1
        
        # keep time in right format
        if seconds >=60:
            seconds = 0
            minutes += 1
            
        if minutes >=60:
            minutes = 0
            hours += 1
        
        if hours >=24:
            hours = 0
            
        return (hours, minutes, seconds)
