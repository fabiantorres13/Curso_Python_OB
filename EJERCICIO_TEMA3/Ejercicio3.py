# ENUNCIADO:
# Escribe un programa en la consola de python que pida al usuario su peso (en kg) 
# y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa 
# corporal calculado redondeado con dos decimales.

peso = int(input("Ingresa tu peso(En Kilogramos): "))
estatura = float(input("Ingresa tu estatura(En metros): "))
IMC = round((peso/(estatura)**2),2)
print(f'Tu indice de masa corporal es: {IMC}')