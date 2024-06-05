# creamos el archivo my_notes.txt file
with open('my_notes.txt', 'w') as f:
    # Write 5 lines of personal notes to the file
    ("Nombre : Eddison Teran.\n")
    f.write("Edad : 35 años.\n")
    f.write("Cedula : 1205458756.\n")
    f.write("Estado civil: Casado.\n")
    f.write("hijos : 1.\n")


# abrimos el archivo
file=open("my_notes.txt","r")
print(file)
lineas = file.readlines()
print(lineas)
# creaos un for para imprimir el lineas
for l in lineas:
    print(l.replace("\n",""))
# contamos los caracteres
with open("my_notes.txt","r") as archivo:
    contenido = archivo.read()
    lineas = contenido.split("\n")
    pos=archivo.tell()
# imprimimos cuantos caracteres tenemos
    print("el archivo tiene {0} caracteres de longitud".format(pos))