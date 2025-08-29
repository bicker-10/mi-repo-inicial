# ordenacion.py

# Matriz 3x3
matriz = [
    [9, 4, 6],
    [1, 7, 3],
    [5, 2, 8]
]

# Función para ordenar una fila con Bubble Sort
def bubble_sort(fila):
    for i in range(len(fila)):
        for j in range(0, len(fila)-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegimos la fila 1 (por ejemplo)
fila_ordenar = 1
matriz[fila_ordenar] = bubble_sort(matriz[fila_ordenar])

# Mostrar matriz resultante
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
