# ENUNCIADO -> Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def añoBisiesto (año):
    if año % 4 == 0:
        return True
    else:
        return False

if añoBisiesto(2023):
    print("Año Bisiesto")
else:
    print("Año No Bisiesto")