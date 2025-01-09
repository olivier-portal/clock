def update_time(current_time):
    
    while True:
        hours, minutes, seconds = current_time
        seconds += 1
        
        if seconds >=60:
            seconds = 0
            minutes += 1
            
        if minutes >=60:
            minutes = 0
            hours += 1
        
        if hours >=24:
            hours = 0
        while True:
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
            
            return (hours, minutes, seconds)
        
    # while True:
    #     hours, minutes, seconds = current_time
    #     seconds += 1
        
    #     if seconds >=60:
    #         seconds = 0
    #         minutes += 1
            
    #     if minutes >=60:
    #         minutes = 0
    #         hours += 1
        
    #     if hours >=24:
    #         hours = 0
    #     while True:
    #         print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
            
    #         return (hours, minutes, seconds)
