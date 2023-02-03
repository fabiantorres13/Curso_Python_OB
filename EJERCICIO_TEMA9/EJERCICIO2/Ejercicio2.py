'''
ENUNCIADO:
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares 
de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
'''

from functools import reduce


def impares(lista):
    
    if lista % 2 != 0:
        return lista

def suma(a,b):
    return a +b
    

resultado = list(filter(impares,[4,1,5,6,3,7,8,9]))
print(f'Impares: {resultado}')
resultado = reduce(suma,resultado)
print(f'Suma: {resultado}')

