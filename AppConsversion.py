import tkinter as tk
from tkinter import ttk #Here, Tk themed widget set

# window project
window = tk.Tk()

# Custom window
window.title('Kauan') #title project
window.geometry('300x150') #width x height

# Title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output / result

output_label = ttk.Label(master = window, text= 'Output', font = 'Calibri 24 bold')
output_label.pack(pady = 5)

# run 
window.mainloop()