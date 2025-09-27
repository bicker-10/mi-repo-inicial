# ============================
# Trabajo con diccionarios - Semana 15
# Autor: Bicker
# ============================

# 1) Crear el diccionario base con información personal
informacion_personal = {
    "nombre": "Bicker",
    "edad": 19,
    "ciudad": "Quito",
    "profesion": "Estudiante"   # Profesión inicial incluida
}

# 2) Acceder y MODIFICAR el valor de la clave "ciudad" -> Portoviejo
informacion_personal["ciudad"] = "Portoviejo"

# 3) Agregar nuevamente la clave-valor "profesion"
#    (como ya existe, aquí la reasignamos con otro valor)
informacion_personal["profesion"] = "Programador"

# 4) Verificar existencia de "telefono"; si no existe, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991008488"

# 5) Eliminar la clave "edad" porque no es necesaria
informacion_personal.pop("edad", None)   # None evita error si no existiera

# 6) Imprimir el diccionario final
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"  {clave}: {valor}")
