import turtle as Screen
def clickme():
    global count
    count +=1
    labeltext.set("你按我" + str(count) + "次了")
    if(btntext.get()=="按我"):
        btntext.set("回復")
    else:
        btntext.set("按我")

import tkinter as tk

win = tk.Tk()
labeltext = tk.StringVar()
btntext = tk.StringVar()
count = 0
label1 = tk.Label(win, fg="red", textvariable=labeltext)
labeltext.set("歡迎")
label1.pack()
button1 = tk.Button(win,textvariable=btntext, command=clickme)
btntext.set("按這")
button1.pack()
win.mainloop()