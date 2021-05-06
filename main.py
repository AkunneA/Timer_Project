from datetime import *
import time
import tkinter
from tkinter import *
from playsound import playsound
import random
import os
""" Credit to wobbleboxx.com for Rise03.aif(Converted to Rise03.mp3 by Aspen Akunne)"""
"""Aspen Akunne, Python Programming  """

def time_set():
    clear_time = datetime.now().replace(minute=0, second=10) #sets the time to countdown
    return clear_time #sends that to main

def window(): #creates tkinter window
    window = Tk()
    screen_width = window.winfo_screenwidth()  # screen width of user's screen
    screen_height = window.winfo_screenheight()  # screen height of user's screen
    tkinter_width = window.winfo_width()  # tkinter width
    tkinter_height = window.winfo_height()  # tkinter height
    window.resizable(0, 0) #makes screen unable to be resized
    window.geometry(str(int((screen_width-tkinter_width)/4))+"x"+str(int((screen_height - tkinter_height) / 4))) #on my 1980x1030 screen
                                                                                                               # moves it slightly up and
                                                                                                                  # to the left
                                                                                                                #unsure if this is
                                                                                                                #the same on other pcs
    return window #returns window


def timer(): #the main event of the program the timer itself
    global curr_time #makes curr_time global variable
    if curr_time.strftime("%M:%S") != to_Zero: #if not 00:00 do this
        curr_time = curr_time + d #subtract 1 second from the time
        word.config(text=curr_time.strftime("%M:%S")) #updates the text in the tkinter window
        redo() #recursively starts again
    else:
        frame.attributes('-alpha',1) #used to attempt to fix a problem with black box and flash on screen
        frame.geometry(str(int(screen_width - tkinter_width)) + "x" + str(int(screen_height - tkinter_height))) #moves to middle
        playsound('Rise03.mp3') #plays a sound to inform you the timer is done
        word.config(text="HOPE YOU GOT WORK DONE") #updates text to "Hope You Got Work Done"
        thingsToDo.config(text=finished)
        frame.after(2000,clickMe)


def redo():
    frame.after(1000, timer)  # testy) #starts again

def clickMe():
    frame.bind('<Button-1>', end)  # closes when you click "Hope you got work done"

def end(event):
    frame.after(1000, frame.destroy()) #closes the window

def taskLister(tasks,num,filename):
    stuff=""
    f = open(filename, "r")
    ta = f.read().splitlines()
    f.close()
    f = open(filename, "w")
    for i in range(len(tasks)):
        if i==num:
            for i in range(len(ta)):
                if ta[i] != tasks[num]:
                    f.write(ta[i] + "\n")
        else:
            stuff += str(i + 1) + "." + tasks[i] + " \n"
    f.close()
    return stuff

def main(tasks,filename):#if __name__ == "__main__":
    global to_Zero
    global curr_time
    global screen_width
    global screen_height
    global frame
    global tkinter_height
    global tkinter_width
    global word
    global thingsToDo
    global finished
    global d

    frame=window() #gets the window info from window
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    tkinter_width = frame.winfo_width()
    tkinter_height = frame.winfo_height()
    frame.overrideredirect(True) #gets rid of top title bar of the tkinter
    curr_time=time_set() #gets curr_time's value
    d=timedelta(seconds=-1) #subtraction of 1 second
    print(tasks)


    num=random.randint(0,len(tasks)-1)
    doing=tasks[num]#"CURRENT TASK:"+tasks[num]
    finished=taskLister(tasks,num,filename)

    #to_Zero formats the time to be compared
    to_Zero=str(datetime.min.minute)+str(datetime.min.minute)+":"+str(datetime.min.second)+str(datetime.min.second)

    word = Label(frame,text=curr_time.strftime("%M:%S"),font=("Palantino",50),bg="grey",fg="red") #sets attributes of the label
    thingsToDo= Label(frame,text=doing,font=("Palantino",30),bg="grey",fg="white")                 # and general format
    frame.wm_attributes('-transparentcolor','grey') #to make the window transparent
    frame.attributes('-topmost', 'true') #makes the window ALWAYS on top
    word.pack(expand=True, fill=BOTH) #puts the words on screen, filling it and expanding to fit
    thingsToDo.pack(expand=True, fill=BOTH)
    frame.after(1000,timer) #after 1 second initiates the timer

    frame.mainloop() #continues the loop of the window



