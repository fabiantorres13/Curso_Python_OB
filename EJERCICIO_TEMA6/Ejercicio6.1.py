'''ENUNCIADO
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    Color
    Ruedas
    Puertas
Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
    Velocidad
    Cilindrada
Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.'''

class Vehiculo:
    Color = ""
    Ruedas = 0
    Puertas = 0

class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 0

coche = Coche()
coche.Color = "Rojo"
coche.Puertas = 4
coche.Velocidad = 120
coche.Cilindrada = 1500

print("El coche tiene: ")
print("Color: ",coche.Color)
print("Puertas: ",coche.Puertas)
print("Velocidad: ",coche.Velocidad, " KM/H")
print("Cilindrada: ",coche.Cilindrada, "cc")



