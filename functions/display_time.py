from .update_time import update_time
import time
import keyboard

def display_time():
    # Choose time format
    while True:
        try:
            time_format_input = int(input("Veuillez choisir le format de l'horloge :\n"
                                          "Pour un format de 12h, entrez 1 :\n"
                                          "Pour un format de 24h, entrez 2 : "))
            if time_format_input in [1, 2]:
                break
            else:
                print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide (1 ou 2).")
            
    # initiate time to 00:00:00 AM/PM (12H format)
    if time_format_input == 1:
        hours = 0
        minutes = 0
        seconds = 0
        am_pm = input("AM ou PM ? (entrez AM/PM) : ").strip().upper()
        if am_pm == "PM" and hours == 11 and minutes == 59 and seconds == 59:
            hours = 0
        elif am_pm == "AM" and hours == 12:
            hours = 0
        
        # return current time in 12h format
        current_time = (hours, minutes, seconds, am_pm)
        
    # initiate time to 00:00:00 (24h format)
    elif time_format_input == 2:
        hours = 0
        minutes = 0
        seconds = 0
        
        # return current time in 24h format
        current_time = (hours, minutes, seconds)
    
    # Add a loop to update the new hour every second
    pause = False
    while True:
        '''Add a possibility to put time on pause'''
        # time is running
        if pause == False:
            current_time = update_time(current_time, time_format_input)
            if time_format_input == 1:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02} {current_time[3]} - Appuyez sur 'p' pour mettre en pause", end="\r")
            else:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02} - Appuyez sur 'p' pour mettre en pause", end="\r")
            time.sleep(1)
        
        # time is on pause
        if pause == True:
            if time_format_input == 1:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02} {current_time[3]}", "En pause, appuyez sur r pour reprendre", end="\r")
            else:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "En pause, appuyez sur r pour reprendre", end="\r")
        
        # press p to put time on pause
        if keyboard.is_pressed("p"):
            pause = True
            time.sleep(0.01)
        
        # press r to run time again    
        if pause == True and keyboard.is_pressed("r"): 
            pause = False
            time.sleep(0.01)
        
