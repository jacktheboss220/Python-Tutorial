import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("ScrolledText Widget")

# Title Label
ttk.Label(
    win, text="ScrolledText Widget Example",
    font=("Times New Roman", 15),
    background='green', foreground="white").grid(column=0, row=0)

# Creating scrolled text
# area widget
text_area = scrolledtext.ScrolledText(
    win, wrap=tk.WORD, width=40, height=10)

text_area.grid(column=0, pady=10, padx=10)

# Placing cursor in the text area
text_area.focus()
win.mainloop()
