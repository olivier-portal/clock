from .update_time import update_time
import time

'''Permitt user to set a new time'''
def set_time():
    # ask user if he wants to change the hour
    print("Veuillez régler l'heure de l'horloge")
    
    # handle user's mistakes
    while True:
        try:
            hours = int(input("Entrez l'heure: "))
            if 0 <= hours < 24:
                break
            else:
                print("L'heure doit être un nombre entier entre 0 et 23.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'heure.")
            
            
    while True:
        try:
            minutes = int(input("Entrez les minutes: "))
            if 0 <= hours < 60:
                break
            else:
                print("Les minutes doivent être un nombre entier entre 0 et 59.")
        except ValueError:
            print("Veuillez entrer un nombre valide pour les minutes.")
            
    while True:
        try:
            seconds = int(input("Entrez les secondes: "))
            if 0 <= seconds < 60:
                break
            else:
                print("Les secondes doivent être un nombre entier entre 0 et 59.")
        except ValueError:
            print("Veuillez entrer un nombre entier pour les secondes.")
    
    current_time = (hours, minutes, seconds)
    
    # Add a loop to update the new hour every second
    while True:
        current_time = update_time(current_time)
        print(f"{current_time[0]:02}:{current_time[1]:02}:{current_time[2]:02}", end="\r")
        time.sleep(1)