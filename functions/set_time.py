from .update_time import update_time
import time

def set_time(current_time):
    while True:
        input_time = input("\nVoulez-vous régler l'heure ? O/N: ")
        if input_time == "o" or input_time == "O":
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
            return (hours, minutes, seconds)

        elif input_time == "n" or input_time == "N":
            return current_time
        else:
            print("Veuillez entrer O ou N")
        
        current_time = (hours, minutes, seconds)
    
        while True:
            current_time = update_time(current_time)
            print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
            time.sleep(1)
            return current_time
