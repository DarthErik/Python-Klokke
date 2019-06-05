#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime
import threading
from datetime import date

def quit(*args):
    root.destroy()


def show_time():
    txt.set(time.strftime("%H:%M:%S"))
    dmy.set(datetime.date.today().strftime("%d.%m.%Y"))
    uke.set(datetime.date.today().strftime("Uke %U"))
    root.after(1000, show_time)


root = Tk()
root.attributes("-fullscreen", False)
root.title("Klokke")
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
root.after(1000, show_time)
root.after(1000, )

fnt = font.Font(family='Helvetica', size=230, weight='bold')
fnt2 = font.Font(family='Helvetica', size=120, weight='bold')

txt = StringVar()
txt.set(time.strftime("%H:%M:%S"))
dmy = StringVar()
dmy.set(time.strftime("%d.%m.%Y"))
uke = StringVar()
uke.set(time.strftime(" Uke%U"))

def CheckTimeAndDisplayClock() :
    if date.today().isoweekday() == 6 | 7 :
        print('if 1')
        timelbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
        dmylbl = ttk.Label(root, textvariable=dmy, font=fnt2, foreground="green", background="black")
        ukelbl = ttk.Label(root, textvariable=uke, font=fnt2, foreground="green", background="black")
    elif '0000' <= time.strftime('%H%M') <= '0759' or '0845' <= time.strftime('%H%M') < '0855' or '0940' <= time.strftime('%H%M') < '0950' or '1035' <= time.strftime('%H%M') < '1045' or '1130' <= time.strftime('%H%M') < '1155' or '1240' <= time.strftime('%H%M') < '1250' or '1335' <= time.strftime('%H%M') < '1345' or '1430' <= time.strftime('%H%M')<'1440' or '1525' <= time.strftime('%H%M') <='2300':
        print('if 2')
        timelbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="green", background="black")
        dmylbl = ttk.Label(root, textvariable=dmy, font=fnt2, foreground="green", background="black")
        ukelbl = ttk.Label(root, textvariable=uke, font=fnt2, foreground="green", background="black")
    else:
        print('if 3')
        timelbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
        dmylbl = ttk.Label(root, textvariable=dmy, font=fnt2, foreground="white", background="black")
        ukelbl = ttk.Label(root, textvariable=uke, font=fnt2, foreground="white", background="black")

    timelbl.place(relx=0.5, anchor=CENTER, rely=0.4)
    dmylbl.place(relx=0.5, anchor=CENTER, rely=0.6)
    ukelbl.place(relx=0.5, anchor=CENTER, rely=0.75)

def printit():
    threading.Timer(5.0, printit).start()
    CheckTimeAndDisplayClock()
    root.mainloop()

printit()
