# Creamos el diccionario informacion_personal
informacion_personal = {
    "nombre": "Alex Yepez",
    "edad": "25" ,
    "ciudad": "puyo",
    "profesion": "Ingeniero en tic",
    "clave iess": "23452"
}


# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["segunda profesion"]="Veterinario"

# Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985412574"

# Elimina la clave "edad" del diccionario.
del informacion_personal["edad"]

# Accede al valor asociado con la clave "clave iess"
informacion_personal["clave iess"] = "12458"


# Imprimir el Diccionario
print(informacion_personal,)