# ==============================================
# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Bicker Ariel Rodríguez Heredia
# Descripción:
#   Este programa crea un archivo de texto, escribe notas,
#   luego lo lee línea por línea y muestra el contenido.
# ==============================================

# Escritura de Archivo de Texto
# ------------------------------
# Creamos un nuevo archivo llamado "my_notes.txt"
# El modo "w" permite escribir en el archivo (creándolo si no existe o sobrescribiéndolo si ya existe).
file = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales
file.write("Primera nota: Hoy estoy practicando Python.\n")
file.write("Segunda nota: Aprender a manejar archivos es importante.\n")
file.write("Tercera nota: GitHub me ayuda a guardar mis proyectos.\n")

# Cerramos el archivo después de escribir
file.close()

# Lectura de Archivo de Texto
# ------------------------------
# Abrimos el archivo en modo lectura con "r"
file = open("my_notes.txt", "r")

print("Contenido del archivo 'my_notes.txt':\n")

# Leemos línea por línea usando readline()
linea = file.readline()
while linea:  # Se repite mientras exista contenido
    print(linea.strip())  # .strip() elimina los saltos de línea al mostrar en consola
    linea = file.readline()

# Cierre de Archivos
# ------------------------------
# Cerramos el archivo después de leer
file.close()
