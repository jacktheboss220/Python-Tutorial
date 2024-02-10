from tkinter import Tk
from tkinter import Label
import time
master = Tk()
master.title("Digital Clock")
clock = Label(master, font=("time", 90), bg=("black"), fg=("white"))
clock.pack()


def timeCall():
    time1 = time.strftime("%H:%M:%S %p")
    clock.config(text=time1)
    clock.after(200, timeCall)


timeCall()
master.mainloop()
