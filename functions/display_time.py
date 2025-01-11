from .update_time import update_time
import time
import keyboard

def display_time():
    hours = 0
    minutes = 0
    seconds = 0
    current_time = (hours, minutes, seconds)
    
    # Add a loop to update the new hour every second
    pause = False
    while True:
        if pause == False:
            current_time = update_time(current_time)
            print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "Appuyez sur p pour mettre en pause    ", end="\r")
            time.sleep(1)
        
        if pause == True:# activate pause
            print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "En pause, appuyez sur r pour reprendre", end="\r")
        
        if keyboard.is_pressed("p"):
            pause = True
            time.sleep(0.01)
            
        if pause == True and keyboard.is_pressed("r"): 
            pause = False
            time.sleep(0.01)
        
