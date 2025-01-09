from .update_time import update_time
import time

def display_time():
    hours = 0
    minutes = 0
    seconds = 0
    current_time = (hours, minutes, seconds)
    while True:
        current_time = update_time(current_time)
        print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", end="\r")
        time.sleep(1)
