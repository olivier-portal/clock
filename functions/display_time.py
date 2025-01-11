from .update_time import update_time
import time
import keyboard

def display_time():
    hours = 0
    minutes = 0
    seconds = 0
    current_time = (hours, minutes, seconds)
    
    pause = False
    
    while True:
        if pause == False:
            current_time = update_time(current_time)
            print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "hold f to put time on pause      ", end="\r")
            time.sleep(1)
            
        if pause == True:# pause fonctionnel
            print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "it's paused, press g to restart", end="\r")
        
        if keyboard.is_pressed("f"):
            pause = True
            time.sleep(0.01)
            
        if pause == True and keyboard.is_pressed("g"): 
            pause = False
            time.sleep(0.01)
        
