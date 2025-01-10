import time
import os
import keyboard




def clock():
    s=00
    m=00
    h=00
    pause=False
    p=""# var pause
    
    while True: # boucle
        if pause==False:#pas pause 
            s+=1
            if s==60:
                m+=1
                s=00
                os.system("cls") #efface tout 
                if m==60:
                    h+=1
                    m=00
                    os.system("cls")
                    if h==24:
                        h=00
                        os.system("cls")
            hour_now="%s:%s:%s" % (h, m, s)
            time.sleep(1)   
            print(hour_now,"  ","hold f to pause ", "                                                  ",end="\r") # end r affiche tout dans la meme ligne
        if pause==True:# pause fonctionnel
            print(p,"it's paused, press g to restart", "                                              ", end="\r")
        
        if keyboard.is_pressed("f"):
            pause=True
            p=hour_now
            time.sleep(0.01)
        if pause==True and keyboard.is_pressed("g"): 
            pause=False
            time.sleep(0.01)

        
        
clock()
