# usando import para buscar e importar un texto.

import os
#pedimos al usuario que ingrese el nombre del txt.
file_name = input("Ingrese el nombre del txt a buscar: ")
# Si el archivo es encontrado, lee el contenido.
if os.path.isfile(file_name):

    with open(file_name, 'r') as f:
        for line in f:
            print(line.strip())
else:
    # Si el archivo no esta, mensaje de error
    print("Archivo no encontrado")