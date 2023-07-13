import tkinter as tk
from tkinter import ttk #Here, Tk themed widget set

def convert():
    # Obtém o valor digitado pelo usuário no campo de entrada e converte para um número inteiro
    number = int(entry.get())
    
    # Multiplica o número por 2
    numberVsnumber = number * 2
    
    # Define o valor da variável output_string como o resultado da multiplicação
    output_string.set(numberVsnumber)



# window project
window = tk.Tk()

# Custom window
window.title('Kauan') #title project
window.geometry('320x170') #width x height

# Title
title_label = ttk.Label(master = window, text = 'Double of The number', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Double', command=convert) #like "Function of others languages"
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output / result

output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text= 'Output', 
    font = 'Calibri 24 bold', 
    textvariable= output_string)
output_label.pack(pady = 5)

# run 
window.mainloop()