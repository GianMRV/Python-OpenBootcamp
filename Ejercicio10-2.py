import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry('300x150')
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=6)

label_title = ttk.Label(window, text = 'Hola! Bienvenido a tu primer programa con tkinter')
label_title.grid(column = 0, row = 1)

label_title = ttk.Label(window, text = 'Cual lenguaje te gustaria aprender?')
label_title.grid(column = 0, row = 2)

val1 = tkinter.IntVar()
val2 = tkinter.IntVar()
val3 = tkinter.IntVar()
val4 = tkinter.IntVar()

radio_button_python = ttk.Checkbutton(window, text = 'Python', variable = val1, onvalue = 1, offvalue = 0)
radio_button_python.grid(column = 0, row = 3)

radio_button_javascript = ttk.Checkbutton(window, text = 'Javascript', variable = val2, onvalue = 1, offvalue = 0)
radio_button_javascript.grid(column = 0, row = 4)

radio_button_php = ttk.Checkbutton(window, text = 'PHP', variable = val3, onvalue = 1, offvalue = 0)
radio_button_php.grid(column = 0, row = 5)

radio_button_c = ttk.Checkbutton(window, text = 'C', variable = val4, onvalue = 1, offvalue = 0)
radio_button_c.grid(column = 0, row = 6)

window.mainloop()