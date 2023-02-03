# ENUNCIADO -> En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    tipo = ""
    recorrido = 0.0
    velocidad = 0
    
    def __init__(self,tipo,recorrido,velocidad):
        self.tipo = tipo
        self.recorrido = recorrido
        self.velocidad = velocidad
    
    def andar(self):
        print (f'El vehiculo de tipo {self.tipo} ha comenzado a andar, debe recorrer {self.recorrido} kilometros a una velocidad de {self.velocidad} km/h')
    

vehiculo = Vehiculo("Carro",100,80)

# Serializando...
f = open('Vehiculo.picl', 'wb')
pickle.dump(vehiculo,f)
f.close()

# Deserializando...
f = open('Vehiculo.picl', 'rb')
reconstrucionObjeto = pickle.load(f)
reconstrucionObjeto.andar()