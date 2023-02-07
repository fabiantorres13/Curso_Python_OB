import sqlite3


def main():
    n = input("Nombre Alumno: ")
    a = input("Apellido Alumno: ")

    if consultarAlumno(n,a) == False:
        print("El alumno no existe...")

        

def consultarAlumno(nombre,apellido):
    conn = sqlite3.connect('estudiantes.db')
    cursor = conn.cursor()

    # Crea la tabla alumnos si no existe
    cursor.execute(""" CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL
    )""")

    # Inserta los estudiantes a la tabla
    # cursor.execute("INSERT INTO alumnos VALUES (8,'Lucía','Manchego')")

    # Consulta el estudiantes ingresado por el usuario
    query = f"SELECT id, nombre, apellido FROM alumnos WHERE nombre ='{nombre}' AND apellido='{apellido}'"
    cursor.execute(query)
    alumno = cursor.fetchone()
    print(f'Datos del Alumno: {alumno}')
    

    conn.commit()
    cursor.close()
    conn.close()

    if alumno == None:
        return False
    else:
        return True

if __name__ == '__main__':
    main()


    



