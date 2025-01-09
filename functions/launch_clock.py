from .display_time import display_time
from .set_time import set_time

def launch_clock():
    while True:
        user_input = input("Voulez-vous mettre l'horloge à lheure ? O/N ")
        if user_input == "o" or user_input == "O":
            set_time()
        elif user_input == "n" or user_input == "N":
            display_time()
        else:
            print("Vous devez entrer O ou N")