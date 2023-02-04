'''
ENUNCIADO:
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado 
y que contenga un botón de reinicio para que deje todo como al principio. Al principio no tiene que haber una opción seleccionada.
'''

import tkinter as tk

window = tk.Tk()
window.config(bd=15)



# Creando los RadioButtons
seleccionado = tk.IntVar()


radioButton1 = tk.Radiobutton(window, text='JAVA', value='1', variable = seleccionado)
radioButton1.grid(row=0, column=0, sticky='W')
radioButton2 = tk.Radiobutton(window, text='PYTHON', value='2', variable = seleccionado)
radioButton2.grid(row=1, column=0, sticky='W')
radioButton3 = tk.Radiobutton(window, text='C', value='3', variable = seleccionado)
radioButton3.grid(row=2, column=0, sticky='W')

# Creando el Boton de reset
def limpiarRadioButton():
    seleccionado.set(None)

button1 = tk.Button(window, text='Limpiar', command=limpiarRadioButton)
button1.grid(row=3, column=0, sticky='E')
    

window.mainloop()