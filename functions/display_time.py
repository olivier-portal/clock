import time
import keyboard
from .update_time import update_time

def display_time(alarm):
    # Format choice
    while True:
        try:
            time_format = int(input("Choisissez le format d'horloge :\n1 - 12 heures\n2 - 24 heures\n"))
            if time_format in [1, 2]:
                break
            print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Initialise time
    current_time = (0, 0, 0, "AM") if time_format == 1 else (0, 0, 0)
    pause = False
    
    while True:
        # update time each seconds if not paused
        if not pause:
            current_time = update_time(current_time, time_format)
            
            if time_format == 1:
                formatted_time = f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02} {current_time[3]}"
            else:
                formatted_time = f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}"
            
            # Vérify if it is the time for the alarm
            if alarm and (current_time[0], current_time[1], current_time[2]) == alarm:
                print("\nIl est l'heure de se réveiller!")
                break
            
            print(f"{formatted_time} - Maintenir 'p' appuyer pour mettre en pause", end="\r")
            time.sleep(1)
        
        # Manage pause
        if keyboard.is_pressed("p"):
            pause = True
            print("\nHorloge en pause. Appuyez sur 'r' pour reprendre.", end="\r")
            time.sleep(0.3)
        elif pause and keyboard.is_pressed("r"):
            pause = False
            print("\nHorloge reprise.", end="\r")
            time.sleep(0.3)