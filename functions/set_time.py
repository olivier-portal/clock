from .update_time import update_time
import time
import keyboard


'''Permitt user to set a new time'''
def set_time(alarm):
    # Initialse pause
    pause = False
    
    # Format choice
    while True:
        try:
            time_format = int(input("Choisissez le format d'horloge :\n1 - 12 heures\n2 - 24 heures\n"))
            if time_format in [1, 2]:
                break
            print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Manage 12h format
    if time_format == 1:
        while True:
            try:
                hours = int(input("Entrez l'heure (1-12) : "))
                if 1 <= hours <= 12:
                    break
                else:
                    print("L'heure doit être entre 1 et 12.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour l'heure.")
        
        while True:
            try:
                minutes = int(input("Entrez les minutes (0-59) : "))
                if 0 <= minutes < 60:
                    break
                else:
                    print("Les minutes doivent être entre 0 et 59.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour les minutes.")
        
        while True:
            try:
                seconds = int(input("Entrez les secondes (0-59) : "))
                if 0 <= seconds < 60:
                    break
                else:
                    print("Les secondes doivent être entre 0 et 59.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour les secondes.")
        
        am_pm = input("AM ou PM ? (entrez AM/PM) : ").strip().upper()
        if am_pm == "PM" and hours == 11 and minutes == 59 and seconds == 59:
            hours = 0
        elif am_pm == "AM" and hours == 12:
            hours = 0

        current_time = (hours, minutes, seconds, am_pm)

    # manage 24h format
    elif time_format == 2:
        while True:
            try:
                hours = int(input("Entrez l'heure (0-23) : "))
                if 0 <= hours < 24:
                    break
                else:
                    print("L'heure doit être entre 0 et 23.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour l'heure.")
        
        while True:
            try:
                minutes = int(input("Entrez les minutes (0-59) : "))
                if 0 <= minutes < 60:
                    break
                else:
                    print("Les minutes doivent être entre 0 et 59.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour les minutes.")
        
        while True:
            try:
                seconds = int(input("Entrez les secondes (0-59) : "))
                if 0 <= seconds < 60:
                    break
                else:
                    print("Les secondes doivent être entre 0 et 59.")
            except ValueError:
                print("Veuillez entrer un nombre valide pour les secondes.")
        
        current_time = (hours, minutes, seconds)
    
    
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