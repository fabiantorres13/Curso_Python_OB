# ENUNCIADO -> Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
lista = []
contador = 100
for i in range(contador):
    if contador > 0 and contador < 101:
        lista.append(contador)
        contador -= 1

print(lista)