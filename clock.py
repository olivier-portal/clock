from tkinter import *
import time

# import locale

# Mettre la date en français
# locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

window = Tk ()

# Define which format to show to user
hour_format = "24"

def date_format():
    date_string = time.strftime("%A %d %B, %Y")
    date_label.config(text=date_string)
    
    # update date every second
    date_label.after(1000, date_format) 

def time_format():
    global hour_format
    
    # If format == 24h
    if hour_format == "24":  
        time_string_24 = time.strftime("%H:%M:%S")
        time_label.config(text=time_string_24)
    # If format == 12h + AM/PM
    else:
        time_string_12= time.strftime("%I:%M:%S %p")
        time_label.config(text=time_string_12)
    # update time every second
    time_label.after(1000, time_format)
    
def change_format_24():
    global hour_format
    hour_format = "24"
    time_format()
    
def change_format_12():
    global hour_format
    hour_format = "12"
    time_format()
    
def stop_time():
    time.sleep(10)

######### define style

# define date
date_label = Label(window, font=("roboto", 25), fg="#00FF00", bg="black")
date_label.pack(side="top", fill="x", padx=1, pady=1, expand="yes")
# main clock
time_label = Label(window, font=("roboto", 50), fg="#00FF00", bg="black")

# define where it appears within the window
time_label.pack(side="top", fill="x", padx=1, pady=1, expand="yes")


# button to change hour format
button_12 = Button(window, font="roboto", text="12", fg="lime", bg="black", command=change_format_12)
button_12.pack(side="left", fill="x", padx=1, pady=1, expand="yes")
        
button_24 = Button(window, font="roboto", text="24", fg="lime", bg="black", command= change_format_24)
button_24.pack(side="left", fill="x", padx=1, pady=1, expand="yes")

# button to stop time
# icon_stop = PhotoImage(file= r"pause-solid.png")
button_sleep = Button(window, command=stop_time, text="Essaie Mamie", fg="lime", bg="black")
button_sleep.pack(side="left", fill="both", padx=1, pady=1, expand="yes")

######### Allow user to change time

# Show label to indicate user to change time
change_time = Label(window, text= "Changer l'heure", fg="lime", bg="black")
change_time.pack(side="bottom", fill="both", padx=1, pady=1, expand="yes", anchor= "center")

# Input time
# tabs_control = Notebook(windows)
# hour_tab = Frame(tabs)
# get_hour = get_hour_entry.get()
# minute_input = input('Minute: ').pack()

# hour_input.pack(side="bottom", fill="both", padx=1, pady=1, expand="yes", anchor= "center")
# minute_input.pack(side="bottom", fill="both", padx=1, pady=1, expand="yes", anchor= "center")


date_format()
time_format()

window.mainloop()