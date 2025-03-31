import tkinter as tk
from tkinter import messagebox

def gg():
    global l, h, g, a
    if l <= h:
        g = (l + h) // 2
        lbl_g.config(text=f"Is it {g}?")
    else:
        lbl_g.config(text="Restart game.")

def less():
    global l, a
    l = g + 1
    a += 1
    gg()

def more():
    global h, a
    h = g - 1
    a += 1
    gg()

def Correct():
    messagebox.showinfo("Done!", f"Guessed in {a} attempts!")
    off()

def off():
    btn_sm.config(state=tk.DISABLED)
    btn_lg.config(state=tk.DISABLED)
    btn_corr.config(state=tk.DISABLED)

def new_game():
    global l, h, a
    l, h = 1, 100
    a = 0
    on()
    gg()

def on():
    btn_sm.config(state=tk.NORMAL)
    btn_lg.config(state=tk.NORMAL)
    btn_corr.config(state=tk.NORMAL)

w = tk.Tk()
w.title("Guess the Number")

lbl_g = tk.Label(w, text="Think of a number 1-100.")
lbl_g.grid(row=0, column=0, columnspan=2)
btn_sm = tk.Button(w, text="Too Small", command=less)
btn_sm.grid(row=1, column=0)
btn_lg = tk.Button(w, text="Too Large", command=more)
btn_lg.grid(row=1, column=1)
btn_corr = tk.Button(w, text="Correct!", command=Correct)
btn_corr.grid(row=2, column=0, columnspan=2)
tk.Button(w, text="New Game", command=new_game).grid(row=3, column=0, columnspan=2)

l, h, a = 1, 100, 0
gg()

w.mainloop()