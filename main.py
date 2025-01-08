from datetime import datetime
import time
import os

# Define which format to show to user
hour_format = "24"

dt = datetime.now()

'''def date_format():
   
    # print(dt.day, "/", dt.month, "/", dt.year)
    
    # update date every second'''
    

def time_format():
    global hour_format
    
    # If format == 24h
    if hour_format == "24":
        os.system("cls")
        while True:  
            '''date_string = dt.strftime("Le %d/%m/%Y")
            print(date_string, end="\r")'''
            start_time_24 = datetime.now()
            # print(dt.hour, ":", dt.minute, ":", dt.second)
            print( "%s/%s/%s %s:%s:%s" % (start_time_24.day, start_time_24.month, start_time_24.year, start_time_24.hour , start_time_24.minute, start_time_24.second), end="\r")
            if start_time_24.second==0:
                os.system("cls")
            time.sleep(0.01)
    # If format == 12h + AM/PM
    else:
        time_string_12= dt.strftime("%I:%M:%S %p")
        # print(dt.hour, ":", dt.minute, ":", dt.second)
        print(time_string_12)
    # update time every second
    
    
def change_format_24():
    global hour_format
    hour_format = "24"
    time_format()
    
def change_format_12():
    global hour_format
    hour_format = "12"
    time_format()
    
def stop_time():
    datetime.sleep(10)


#date_format()
time_format()
