def current_time():
    
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
    set_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(set_time)

current_time()