from datetime import *
import time
import tkinter
from tkinter import *
import random
import os  # os is used for listing items in directory
import main  # main is imported for use by tasker

"""Aspen Akunne, Python Programming  """


def makeMe(taskWin):  # makes new files
    g = 0  # a number to list all the tasksLists currently made
    thing = os.listdir()  # gets a list of files in this current directory
    for i in thing:
        if i.find("taskList") != -1:  # finds all the tasks lists
            g += 1

    for i in taskWin.winfo_children():  # destroys all original buttons, avoids need to call specific buttons
        if ".!button" in str(i):  # winfo has a tuple of buttons, so using .!button lets them get removed
            i.destroy()  # destorys buttons

    f = open("taskList{}.txt".format(g), "w")  # creates a new task list g

    enter = Label(taskWin, text="Enter a task")  # creates a label to prompt to enter text
    input = Entry(taskWin)  # for user input
    whenDone = Button(taskWin, text="Done", fg="Black", command=lambda: [handler(taskWin)])  # creates a button
    # that will also activate handler
    test = Label(taskWin, text="Entered!")  # a label to confirm entry
    input.bind("<Return>", lambda g=f: [f.write(input.get() + "\n"), test.pack()])  # enter key writes input to file
    # also shows Entered!
    input.bind("<Key>", lambda g=f: test.pack_forget())  # press any other key and Enter disappers

    enter.pack()  # shows enter
    input.pack()  # shows input
    whenDone.pack()  # shows whenDone


def handler(taskWin):  # this is to show the file is created
    finalWin = Tk()  # new confirmation window
    word = Label(finalWin, text="File Created!", font=("Palantino", 30), bg="white",
                 fg="Black")  # shows a new window with file created
    word.pack()

    finalWin.after(2000, lambda: [finalWin.destroy(), taskWin.destroy(), window()])  # destroys confirmation window,
    # destroys taskWin, then starts over
    finalWin.mainloop()


def useMe(taskWin):  # if one does not exist, then force MakeMe
    whichFile = Label(taskWin, text="Which file do you want to Use?")  # allows you to pick a certain file to use
    thing = os.listdir()  # lists files in directory

    names = []  # to save taskLists
    for i in thing:
        if (i.find("taskList") != -1):  # goes through and finds all tasklists
            names.append(i)

    if (len(names) == 0):  # if names is empty=> no taskLists then go to makeMe
        nonefound = Label(taskWin,
                          text="No files Found: Redirecting to Make File")  # shows a new label for creating new file
        nonefound.pack()  # shows nonefound
        taskWin.after(1000, lambda: nonefound.destroy())  # destroys noneFound
        makeMe(taskWin)  # activates makeMe and passes taskWin into it

    for i in taskWin.winfo_children():  # destroys all original buttons, avoids need to call specific button
        if ".!button" in str(i):  # winfo has a tuple of buttons, so using .!button lets them get removed
            i.destroy()  # destorys buttons

    buttons = []  # a list of buttons

    buttonNum = 0
    for s in names:
        buttons.append(Button(taskWin, text=s, fg="Black",
                              command=lambda n=s: [reallyUsing(s, taskWin)]))
        buttons[buttonNum].pack()
        buttonNum += 1


def reallyUsing(txt, taskWin):  # if a button is pressed then use the txt file listed
    finalWin = Tk()  # a disposeable window to confirm
    word = Label(finalWin, text="List Set: Saving Selection....", font=("Palantino", 30), bg="white",
                 fg="Black")  # shows "List Set: Saving Selection.../
    word.pack()  # shows word

    selection = open("default.txt", "w")  # default text file to write/make
    selection.write(txt.replace('taskList', "").replace(".txt", ""))  # writes the number of tasklist to it
    selection.close()  # closes

    finalWin.after(2000, lambda: [finalWin.destroy(), taskWin.destroy(), window()])  # destroys confirmation window,
    # destroys taskWin, then starts over
    finalWin.mainloop()


def going(taskWin):  # sends the tasklist and file name to main for the main process
    tasknum = open("default.txt", "r")  # the current task number in default
    i = tasknum.readline()  # the task number
    tasknum.close()
    tasks = open("taskList{}.txt".format(i), "r")  # uses default.txt number to create the filename and open it
    tasklist = tasks.read().splitlines()  # splits the tasks into a list

    if len(tasklist) == 0:
        finalWin = Tk()  # a disposeable window to confirm
        word = Label(finalWin, text="File Empty. You are Done with your Tasks!", font=("Palantino", 30), bg="white",
                     fg="Black")  #
        word.pack()  # shows word
        finalWin.after(1000, lambda: [finalWin.destroy(), taskWin.destroy()])
        finalWin.mainloop()

        exit(0)

    try:
        for g in range(len(tasklist)):
            tasklist.remove('')
        tasks.close()
        taskWin.destroy()
        main.main(tasklist, "taskList{}.txt".format(i))  # sends taskList and taskslist name to main

    except:
        main.main(tasklist, "taskList{}.txt".format(i))  # sends taskList and taskslist name to main


def window():  # window creates a new window to be used by the program, used also for resetting
    taskWin = Tk()  # the new tkinter window
    taskWin.resizable(0, 0)  # it cannot be resized
    current = ""
    start = open("default.txt", "w+")  # open default.txt
    g = 0  # g is the number of task lists

    thing = os.listdir()  # list of items in folder
    for i in thing:  # iterates through list to find taskslists
        if i.find("taskList") != -1:
            g += 1

    rand = (random.randint(0, g))
    if g > 0 and g != 1:
        for i in thing:
            if i.find("taskList{}".format(rand)) != -1:
                start.write(str(rand))
                start.close()
        else:
            rand = (random.randint(0, g))
            if i.find("taskList{}".format(rand)) != -1:
                start.write(str(rand))
                start.close()

    if g == 1:
        start.write(str(0))
        start.close()

    if g == 0:
        intro = ['Get Grocery', 'Clean table', 'Pick Garden', 'Drive Truck']
        firstText = open("taskList0.txt", "w+")
        for val in range(len(intro)):
            firstText.write(intro[val] + "\n")
        firstText.close()

        start.write(str(0))
        start.close()

    start = open("default.txt", "r")
    current = (str(start.readline()))
    start.close()

    currentName = "taskList{}.txt".format(
        current)  # set the tasklist number=> ex: current=2 then it'll be "tasklist2.txt"

    while currentName == "taskList.txt":
        rand = (random.randint(0, g))
        for i in thing:
            if i.find("taskList{}".format(rand)) != -1:
                currentName = "taskList{}.txt".format(rand)

    # the internals of the window, text, buttons,etc
    word = Label(taskWin, text="What do you Want to Do?", font=("Palantino", 30), bg="white", fg="Black")
    curr_List = Label(taskWin, text=currentName, fg="Black")
    makeFile = Button(taskWin, text="Make a New Task List", fg="Black", command=lambda: makeMe(taskWin))
    useFile = Button(taskWin, text="Set a Task List To Use", fg="Black", command=lambda: useMe(taskWin))
    doNothing = Button(taskWin, text="Start the Program", fg="Black", command=lambda: going(taskWin))
    word.pack()
    curr_List.pack()
    makeFile.pack()
    useFile.pack()
    doNothing.pack()
    taskWin.mainloop()


if __name__ == "__main__":
    window()  # creates the window
