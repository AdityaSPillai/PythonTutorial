import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = float(entry.get())
        if var.get() == 1:
            result = (value * 9/5) + 32
            label_result.config(text=f"{result:.2f} °F")
        else:
            result = (value - 32) * 5/9
            label_result.config(text=f"{result:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

var = tk.IntVar(value=1)

tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Radiobutton(frame, text="Celsius to Fahrenheit", variable=var, value=1).pack(side=tk.LEFT)
tk.Radiobutton(frame, text="Fahrenheit to Celsius", variable=var, value=2).pack(side=tk.LEFT)

tk.Button(root, text="Convert", command=convert).pack(pady=5)

label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

root.mainloop()