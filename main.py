# import functions to run them
from functions.display_time import display_time
from functions.set_time import set_time
from functions.update_time import update_time
from functions.set_alarm import set_alarm
import time

# permitt to switch between functions
# enable_display_time = True
# enable_set_time = False
# run functions in order of appearence

while True:
    user_input = input("Voulez-vous mettre l'horloge à lheure ? O/N ")
    if user_input == "o" or user_input == "O":
        set_time()
    elif user_input == "n" or user_input == "N":
        display_time()
    else:
        print("Vous devez entrer O ou N")
        


