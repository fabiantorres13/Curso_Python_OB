import pickle

class Vehiculo:
    
    def __init__(self,tipo,recorrido,velocidad):
        print (f'El vehiculo de tipo {tipo} ha comenzado a andar, debe recorrer {recorrido} kilometros a una velocidad de {velocidad} km/h')
    


f = open('Vehiculo.dat', 'rb')
vehiculo = pickle.load(f)
f.close()
