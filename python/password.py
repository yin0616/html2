import tkinter as tk
from tkinter import messagebox

def checkPW():
    if(PW.get() == "1234"):
        msg.set("歡迎登陸")
        win.withdraw()  # 隱藏第一個窗口
        choose_sport()
    else:
        msg.set("密碼不正確")

def choose_sport():
    def choose():
        str = "你喜歡的運動: "
        for i in range(0, len(choise)):
            if(choise[i].get() == 1):
                str = str + ball[i] + " "
        messagebox.showinfo("選擇結果", str)
        win.destroy()  # 關閉第一個窗口

    choise = []
    ball = ["足球","籃球","棒球"]
    win2 = tk.Toplevel(win)
    for i in range(0, len(ball)):
        choise.append(tk.IntVar())
        tk.Checkbutton(win2, text=ball[i], variable=choise[i]).pack()
    tk.Button(win2, text="確認", command=choose).pack()

win = tk.Tk()
PW = tk.StringVar()
msg = tk.StringVar()
label = tk.Label(win, text="請輸入密碼")
label.pack()
entry = tk.Entry(win, textvariable=PW)
entry.pack() 
buttom = tk.Button(win, text="登入", command=checkPW)
buttom.pack()
lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.pack()
win.mainloop()





