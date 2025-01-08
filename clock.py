from tkinter import *
import time

# import locale

# Mettre la date en français
# locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

window = Tk ()

def date_format():
    date_string = time.strftime("%A %d %B, %Y")
    date_label.config(text=date_string)
    
    # update date every second
    date_label.after(1000, date_format) 

def time_format_24():
    time_string_24 = time.strftime("%H:%M:%S")
    time_label_24.config(text=time_string_24)

    # update time every second
    time_label_24.after(1000, time_format_24)

def time_format_12():
    time_string_12= time.strftime("%I:%M:%S %p")
    time_label_12.config(text=time_string_12)
    
    # update time every second
    time_label_12.after(1000, time_format_12)
    
def stop_time():
    time.sleep(10)

######### define style

# define date
date_label = Label(window, font=("roboto", 25), fg="#00FF00", bg="black")
date_label.pack(side="top", fill="x", padx=1, pady=1, expand="yes")
# main clock
time_label_12 = Label(window, font=("roboto", 50), fg="#00FF00", bg="black")
time_label_24 = Label(window, font=("roboto", 50), fg="#00FF00", bg="black")
# define where it appears within the window
time_label_12.pack(side="top", fill="x", padx=1, pady=1, expand="yes")
time_label_24.pack(side="top", fill="x", padx=1, pady=1, expand="yes")

# button to change hour format
button_12 = Button(window, font="roboto", text="12", fg="lime", bg="black", command=time_format_12)
button_12.pack(side="left", fill="x", padx=1, pady=1, expand="yes")
        
button_24 = Button(window, font="roboto", text="24", fg="lime", bg="black", command= time_format_24)
button_24.pack(side="left", fill="x", padx=1, pady=1, expand="yes")

# button to stop time
# icon_stop = PhotoImage(file= r"pause-solid.png")
button_sleep = Button(window, command=stop_time, text="Essaie Mamie", fg="lime", bg="black")
button_sleep.pack(side="bottom", fill="both", padx=1, pady=1, expand="yes")


date_format()
time_format_24()

window.mainloop()