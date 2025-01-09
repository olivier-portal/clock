def set_alarm():
    
    while True:
        try:
            create_alarm =input("Voulez-vous mettre une alarme ? O/N: ")
            if create_alarm == "o" or create_alarm == "O":
                while True:
                    try:
                        hours = int(input("Entrez l'heure de l'alarme: "))
                        if 0 <= hours < 24:
                            break
                        else:
                            print("L'heure doit être un nombre entier entre 0 et 23.")
                    except ValueError:
                        print("Veuillez entrer un nombre valide pour l'heure.")
                while True:
                    try:
                        minutes = int(input("Entrez les minutes de l'alarme: "))
                        if 0 <= hours < 60:
                            break
                        else:
                            print("Les minutes doivent être un nombre entier entre 0 et 59.")
                    except ValueError:
                        print("Veuillez entrer un nombre valide pour les minutes.")
                            
                while True:
                    try:
                        seconds = int(input("Entrez les secondes de l'alarme: "))
                        if 0 <= seconds < 60:
                            break
                        else:
                            print("Les secondes doivent être un nombre entier entre 0 et 59.")
                    except ValueError:
                        print("Veuillez entrer un nombre entier pour les secondes.")
                break
            elif create_alarm == "n" or create_alarm == "N":
                break
        except ValueError:
            print("Veuillez entrer O ou N")
        
    return (hours, minutes, seconds)
