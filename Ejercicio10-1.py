import tkinter
from tkinter import ttk

def reset():
    val.set(None)

window = tkinter.Tk()
window.geometry('300x150')
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=7)

label_title = ttk.Label(window, text = 'Hola! Bienvenido a tu primer programa con tkinter')
label_title.grid(column = 0, row = 1)

label_title = ttk.Label(window, text = 'Cual lenguaje te gustaria aprender?')
label_title.grid(column = 0, row = 2)

val = tkinter.IntVar()

radio_button_python = ttk.Radiobutton(window, text = 'Python', value = 1, variable = val)
radio_button_python.grid(column = 0, row = 3)

radio_button_javascript = ttk.Radiobutton(window, text = 'Javascript', value = 2, variable = val)
radio_button_javascript.grid(column = 0, row = 4)

radio_button_php = ttk.Radiobutton(window, text = 'PHP', value = 3, variable = val)
radio_button_php.grid(column = 0, row = 5)

radio_button_c = ttk.Radiobutton(window, text = 'C', value = 4, variable = val)
radio_button_c.grid(column = 0, row = 6)

button_unselect = ttk.Button(window, text = 'Reset all buttons', command = reset)
button_unselect.grid(column = 0, row = 7)

window.mainloop()