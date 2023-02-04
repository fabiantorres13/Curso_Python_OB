'''
ENUNCIADO:
En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener 
una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
'''

import tkinter as tk

window = tk.Tk()
window.config(bd=30)


label1 = tk.Label(text='¿Cuáles te gustan más?').grid(row=0,sticky='W')
seleccionado1 = tk.IntVar()
checkbutton1 = tk.Checkbutton(window,text='Frutas',variable=seleccionado1).grid(row=2,sticky='W')

seleccionado2 = tk.IntVar()
checkbutton2 = tk.Checkbutton(window,text='Vagetales',variable=seleccionado2).grid(row=3,sticky='W')

seleccionado3 = tk.IntVar()
checkbutton3 = tk.Checkbutton(window,text='Carbohidratos',variable=seleccionado3).grid(row=4,sticky='W')




window.mainloop()