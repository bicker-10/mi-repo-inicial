# busqueda.py

# Creamos una matriz 3x3
matriz = [
    [1, 5, 9],
    [2, 6, 8],
    [3, 7, 4]
]

# Valor a buscar
valor = int(input("Ingresa el valor a buscar: "))

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Buscar y mostrar resultado
pos = buscar_valor(matriz, valor)
if pos:
    print(f"Valor encontrado en la posición fila {pos[0]}, columna {pos[1]}")
else:
    print("Valor no encontrado.")
    