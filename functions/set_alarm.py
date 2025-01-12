def set_alarm():
    while True:
        create_alarm = input("Voulez-vous mettre une alarme ? O/N: ").strip().lower()
        if create_alarm == "o":
            while True:
                try:
                    hours = int(input("Entrez l'heure de l'alarme (0-23) : "))
                    if 0 <= hours < 24:
                        break
                    print("L'heure doit être entre 0 et 23.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            while True:
                try:
                    minutes = int(input("Entrez les minutes de l'alarme (0-59) : "))
                    if 0 <= minutes < 60:
                        break
                    print("Les minutes doivent être entre 0 et 59.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            while True:
                try:
                    seconds = int(input("Entrez les secondes de l'alarme (0-59) : "))
                    if 0 <= seconds < 60:
                        break
                    print("Les secondes doivent être entre 0 et 59.")
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            return (hours, minutes, seconds)
        elif create_alarm == "n":
            return None
        else:
            print("Veuillez répondre par O ou N.")