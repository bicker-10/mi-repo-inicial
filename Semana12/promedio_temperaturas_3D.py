# Lista de ciudades
ciudades = ["Quito", "Portoviejo", "Esmeraldas", "Ambato", "Cuenca", "Sangolquí", "Guayaquil"]

# Matriz 3D: temperaturas[ciudad][semana][día]
# Simulamos temperaturas generadas manualmente (valores de ejemplo)
temperaturas = [
    [  # Quito
        [20, 21, 19, 22, 18, 20, 21],  # Semana 1
        [22, 20, 19, 21, 23, 22, 20],  # Semana 2
    ],
    [  # Portoviejo
        [28, 29, 30, 31, 32, 30, 29],
        [30, 31, 29, 28, 30, 31, 32],
    ],
    [  # Esmeraldas
        [27, 28, 27, 29, 28, 27, 26],
        [28, 29, 28, 30, 29, 28, 27],
    ],
    [  # Ambato
        [18, 17, 19, 18, 17, 18, 19],
        [19, 18, 17, 20, 19, 18, 17],
    ],
    [  # Cuenca
        [15, 16, 17, 15, 16, 17, 16],
        [16, 15, 17, 16, 15, 16, 17],
    ],
    [  # Sangolquí
        [20, 21, 20, 22, 21, 20, 21],
        [22, 21, 20, 21, 22, 23, 22],
    ],
    [  # Guayaquil
        [30, 31, 32, 33, 34, 32, 31],
        [32, 33, 34, 35, 33, 32, 31],
    ]
]

# Calcular promedios semanales por ciudad
for i in range(len(ciudades)):
    print(f"\nCiudad: {ciudades[i]}")
    for semana in range(len(temperaturas[i])):
        suma = 0
        for dia in range(len(temperaturas[i][semana])):
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(temperaturas[i][semana])
        print(f"  Semana {semana + 1}: Promedio = {promedio:.2f}°C")
