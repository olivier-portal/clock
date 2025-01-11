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
        if am_pm == "PM" and hours != 12:
            hours += 12
        elif am_pm == "AM" and hours == 12:
            hours = 0

        current_time = (hours, minutes, seconds)

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