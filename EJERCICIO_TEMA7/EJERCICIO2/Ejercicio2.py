'''
ENUNCIADO:
1.  En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis 
que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

2.  En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para 
calcular el tiempo que queda de trabajo.
'''
import datetime

if datetime.datetime.now().hour > 19:
    print("Es hora de ir a casa...")
else:
    salidaHora = 19 - datetime.datetime.now().hour
    salidaMinutos = 60 - datetime.datetime.now().minute
    print("Aún Faltan", salidaHora,"horas y ",salidaMinutos, "minutos para ir a casa")
    print("Sigue trabajando...")

