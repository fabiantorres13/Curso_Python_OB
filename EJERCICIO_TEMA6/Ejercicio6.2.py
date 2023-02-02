'''
ENUNCIADO:
En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''


class Alumno:
    nombre = ""
    nota = 0

    def AsignarDatos(self,estudiante,calificacion):
        global nombre
        nombre = estudiante

        global nota
        nota = calificacion
        

        if nota < 3:
            print("Alumno: ", nombre)
            print("Nota: ",nota," -> ","No Aprobado")
        else:
            print("Alumno: ", nombre)
            print("Nota: ",nota," -> ","Aprobado")


alumno = Alumno()
alumno.AsignarDatos("Fabián", 2)



            
        
            



