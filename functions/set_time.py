from .update_time import update_time
import time
import keyboard


'''Permitt user to set a new time'''
def set_time():
    # ask user if he wants to change the hour
    while True:
        try:
            time_format_input = int(input("Veuillez régler l'heure de l'horloge :\n"
                                          "Pour un format de 12h, entrez 1 :\n"
                                          "Pour un format de 24h, entrez 2 : "))
            if time_format_input in [1, 2]:
                break
            else:
                print("Veuillez entrer 1 ou 2.")
        except ValueError:
            print("Veuillez entrer un nombre valide (1 ou 2).")

    # Manage 12h format
    if time_format_input == 1:
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
    elif time_format_input == 2:
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
    
    
    # Add a loop to update the new hour every second and manage pause
    pause = False
    while True:
        '''Add a possibility to put time on pause'''
        # time is running
        if pause == False:
            current_time = update_time(current_time, time_format_input)
            if time_format_input == 1:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02} {current_time[3]}", "Appuyez sur 'p' pour mettre en pause", end="\r")
            else:
                print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", "Appuyez sur 'p' pour mettre en pause", end="\r")
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