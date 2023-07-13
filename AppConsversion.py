import tkinter as tk
from tkinter import ttk

def toggle_theme():
    current_theme = window.tk.call('ttk::style', 'theme', 'use')
    if current_theme == 'default':
        window.tk.call('ttk::style', 'theme', 'use', 'clam')
    else:
        window.tk.call('ttk::style', 'theme', 'use', 'default')

def convert():
    number = int(entry.get())
    numberVsnumber = number * 2
    output_string.set(numberVsnumber)

# window project
window = tk.Tk()

# Custom window
window.title('Kauan')
window.geometry('320x170')

# Title
title_label = ttk.Label(master=window, text='Double of The number', font='Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Double', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# Output / Result
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font='Calibri 24 bold',
    textvariable=output_string)
output_label.pack(pady=5)

# Toggle theme button
toggle_button = ttk.Button(master=window, text='Toggle Theme', command=toggle_theme)
toggle_button.pack(pady=10)

# Run
window.mainloop()
