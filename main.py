# import functions to run them
from functions.set_alarm import set_alarm
from functions.display_time import display_time
from functions.set_time import set_time


def main():
    # Define if there is an alarm or not
    alarm = set_alarm()
    if alarm:
        print(f"Alarme réglée pour {alarm[0]:02}:{alarm[1]:02}:{alarm[2]:02}.")
    else:
        print("Vous n'avez pas mis d'alarme.")
    
    # Launch the clock
    user_input = input("Voulez-vous mettre l'horloge à lheure ? O/N ")
    if user_input == "o" or user_input == "O":
        set_time(alarm)
    elif user_input == "n" or user_input == "N":
        display_time(alarm)
    else:
        print("Vous devez entrer O ou N")

if __name__ == "__main__":
    main()