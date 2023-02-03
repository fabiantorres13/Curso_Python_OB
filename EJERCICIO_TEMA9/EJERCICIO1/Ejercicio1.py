'''
ENUNCIADO:
Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
'''
valor = input("Ingresa una lista de paises(Sepáralos por comas): ")
listaPaises = valor.split(',')     
print(sorted(set(listaPaises)))