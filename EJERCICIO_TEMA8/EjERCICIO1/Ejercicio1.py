f = open('primerFichero.txt', 'w')
animales =['Perro\n', 
            'Gato\n',
            'Loro\n',
            'Leon\n']
f.writelines(animales)
f.close()