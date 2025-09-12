# funcion_promedio_temperaturas.py
# Autor: Bicker
# Descripción: Programa que define una función para calcular
#              la temperatura promedio de varias ciudades durante varias semanas.

# Definimos nuestra función
def calcular_promedios(temperaturas, ciudades):
    """
    Calcula el promedio semanal de temperaturas para cada ciudad.
    
    Parámetros:
        temperaturas: lista 3D con datos de temperaturas [ciudad][semana][día]
        ciudades: lista con los nombres de las ciudades
    
    Retorna:
        Un diccionario con los promedios de cada ciudad por semana.
    """
    resultados = {}

    for i in range(len(ciudades)):
        ciudad = ciudades[i]
        resultados[ciudad] = []
        
        # recorremos las semanas
        for semana in range(len(temperaturas[i])):
            suma = 0
            for dia in range(len(temperaturas[i][semana])):
                suma += temperaturas[i][semana][dia]
            promedio = suma / len(temperaturas[i][semana])
            resultados[ciudad].append(promedio)
    
    return resultados


# -----------------------
# Datos de ejemplo: 3 ciudades, 4 semanas, 7 días
# -----------------------

ciudades = ["Quito", "Portoviejo", "Esmeraldas"]

temperaturas = [
    [  # Quito
        [20, 21, 19, 22, 18, 20, 21],  # Semana 1
        [22, 20, 19, 21, 23, 22, 20],  # Semana 2
        [19, 21, 20, 22, 21, 20, 19],  # Semana 3
        [20, 22, 21, 23, 20, 21, 22]   # Semana 4
    ],
    [  # Portoviejo
        [28, 29, 30, 31, 32, 30, 29],
        [30, 31, 29, 28, 30, 31, 32],
        [29, 30, 28, 29, 31, 32, 30],
        [30, 31, 30, 29, 28, 30, 31]
    ],
    [  # Esmeraldas
        [27, 28, 27, 29, 28, 27, 26],
        [28, 29, 28, 30, 29, 28, 27],
        [27, 28, 29, 27, 28, 29, 28],
        [28, 29, 30, 28, 27, 29, 28]
    ]
]

# -----------------------
# Llamada a la función
# -----------------------

resultados = calcular_promedios(temperaturas, ciudades)

# Mostrar los promedios
for ciudad, promedios in resultados.items():
    print(f"\nCiudad: {ciudad}")
    for i, promedio in enumerate(promedios, start=1):
        print(f"  Semana {i}: Promedio = {promedio:.2f}°C")
