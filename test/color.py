from tkinter import Tk
from random import randint
color_changer = Tk()

color_changer.geometry("400x400")
color_changer.title('color')

def update():
    color = "%05x" % randint(0, 0xFFFFFF)
    color_changer.config(bg='#fcba03' + color)
    color_changer.after(1000, update)


update()


color_changer.mainloop()
