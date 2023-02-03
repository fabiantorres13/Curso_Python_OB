# ENUNCIADO -> En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, 
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open('primerFichero.txt', 'w')
animales =['Perro\n', 
            'Gato\n',
            'Loro\n',
            'Leon\n']
f.writelines(animales)
f.close()