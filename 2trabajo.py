"""
*Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
En una dimensión, puedes tener diferentes ciudades,
en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.),
y en la tercera dimensión, semanas.

*Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
*Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla"""

control = [
    [  # guayaquil
        [  # Semana 1
            {"día": "Lunes", "temp": 26},
            {"día": "Martes", "temp": 25},
            {"día": "Miércoles", "temp": 25},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 24},
            {"día": "Sábado", "temp": 26},
            {"día": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"día": "Lunes", "temp": 25},
            {"día": "Martes", "temp": 32},
            {"día": "Miércoles", "temp": 31},
            {"día": "Jueves", "temp": 30},
            {"día": "Viernes", "temp": 25},
            {"día": "Sábado", "temp": 30},
            {"día": "Domingo", "temp": 28}
        ],
        [  # Semana 3
            {"día": "Lunes", "temp": 25},
            {"día": "Martes", "temp": 32},
            {"día": "Miércoles", "temp": 28},
            {"día": "Jueves", "temp": 28},
            {"día": "Viernes", "temp": 28},
            {"día": "Sábado", "temp": 32},
            {"día": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"día": "Lunes", "temp": 28},
            {"día": "Martes", "temp": 29},
            {"día": "Miércoles", "temp": 30},
            {"día": "Jueves", "temp": 25},
            {"día": "Viernes", "temp": 28},
            {"día": "Sábado", "temp": 30},
            {"día": "Domingo", "temp": 29}
        ],
    ],
    [  # Quito
        [  # Semana 1
            {"día": "Lunes", "temp": 18},
            {"día": "Martes", "temp": 20},
            {"día": "Miércoles", "temp": 15},
            {"día": "Jueves", "temp": 16},
            {"día": "Viernes", "temp": 20},
            {"día": "Sábado", "temp": 19},
            {"día": "Domingo", "temp": 18}
        ],
        [  # Semana 2
            {"día": "Lunes", "temp": 15},
            {"día": "Martes", "temp": 18},
            {"día": "Miércoles", "temp": 19},
            {"día": "Jueves", "temp": 18},
            {"día": "Viernes", "temp": 19},
            {"día": "Sábado", "temp": 15},
            {"día": "Domingo", "temp": 21}
        ],
        [  # Semana 3
            {"día": "Lunes", "temp": 18},
            {"día": "Martes", "temp": 19},
            {"día": "Miércoles", "temp": 16},
            {"día": "Jueves", "temp": 20},
            {"día": "Viernes", "temp": 18},
            {"día": "Sábado", "temp": 19},
            {"día": "Domingo", "temp": 20}
        ],
        [  # Semana 4
            {"día": "Lunes", "temp": 15},
            {"día": "Martes", "temp": 16},
            {"día": "Miércoles", "temp": 20},
            {"día": "Jueves", "temp": 19},
            {"día": "Viernes", "temp": 18},
            {"día": "Sábado", "temp": 19},
            {"día": "Domingo", "temp": 18}
        ]
    ],
    [  # Cuenca
        [  # Semana 1
            {"día": "Lunes", "temp": 21},
            {"día": "Martes", "temp": 15},
            {"día": "Miércoles", "temp": 20},
            {"día": "Jueves", "temp": 19},
            {"día": "Viernes", "temp": 19},
            {"día": "Sábado", "temp": 18},
            {"día": "Domingo", "temp": 13}
        ],
        [  # Semana 2
            {"día": "Lunes", "temp": 15},
            {"día": "Martes", "temp": 19},
            {"día": "Miércoles", "temp": 20},
            {"día": "Jueves", "temp": 15},
            {"día": "Viernes", "temp": 15},
            {"día": "Sábado", "temp": 14},
            {"día": "Domingo", "temp": 18}
        ],
        [  # Semana 3
            {"día": "Lunes", "temp": 19},
            {"día": "Martes", "temp": 15},
            {"día": "Miércoles", "temp": 18},
            {"día": "Jueves", "temp": 19},
            {"día": "Viernes", "temp": 18},
            {"día": "Sábado", "temp": 20},
            {"día": "Domingo", "temp": 19}
        ],
        [  # Semana 4
            {"día": "Lunes", "temp": 18},
            {"día": "Martes", "temp": 19},
            {"día": "Miércoles", "temp": 17},
            {"día": "Jueves", "temp": 18},
            {"día": "Viernes", "temp": 19},
            {"día": "Sábado", "temp": 18},
            {"día": "Domingo", "temp": 18}
        ]
    ]
]

# inicializamos una lista de cadena  con tres nombres de ciudades.
ciudades = ["Guayaquil", "Quito", "Cuenca"]

# iniciamos un for que itera sobre la temperaturaslista. tiliza para obtener tanto el índice ( ciudad_idx) como el valor ( ciudad) de cada elemento de la lista.

for ciudad_idx, ciudad in enumerate(
        control):  # Utilizamos enumerate para obtener tanto el índice ( ciudad_idx) como el valor ( ciudad) de cada elemento de la lista.
    print("""
                PROMEDIOS DE TEMPERATURAS 
    """)
    #  inicia un for que itera sobre la lista "ciudad"
    for semana_idx, semana in enumerate(
            ciudad):  # enumerate para obtener tanto el índice ( semana_idx) como el valor ( semana) de cada elemento de la lista.
        # calculamos la suma de temperaturas de la semana actual."temp"valor de cada diccionario en la semanalista y luego aplica la sumfunción a la lista resultante.
        suma_control = sum([dia["temp"] for dia in semana])
        # calculamos  la temperatura promedio de la semana actual dividiendo la suma de temperaturas por el número de días de la semana.
        promedio = suma_control / len(semana)
        # imprime la temperatura promedio de la semana actual, junto con el nombre de la ciudad y el número de semana.
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")