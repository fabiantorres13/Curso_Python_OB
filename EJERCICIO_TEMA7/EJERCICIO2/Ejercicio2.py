'''
ENUNCIADO:
1.  En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis 
que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

2.  En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para 
calcular el tiempo que queda de trabajo.
'''
import datetime

salida = 10

if datetime.datetime.now().hour >= salida:
    print("Es hora de ir a casa...")
else:
    salidaHora = salida - datetime.datetime.now().hour
    salidaMinutos = 60 - datetime.datetime.now().minute
    if salidaHora == 1:
        print("Aún Faltan",salidaMinutos, "minutos para ir a casa")
        print("Sigue trabajando...")
    else:
        print("Aún Faltan", salidaHora - 1,"horas y ",salidaMinutos, "minutos para ir a casa")
        print("Sigue trabajando...")


