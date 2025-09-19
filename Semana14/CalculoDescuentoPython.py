# CalculoDescuentoPython.py
# Autor: Bicker
# Descripción: Programa que calcula el descuento en compras utilizando funciones con parámetros,
#              valores predeterminados y retorno de valores.

# -------------------------
# Definición de la función
# -------------------------
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre una compra.

    Parámetros:
        monto_total (float): El valor total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto = 10%).

    Retorna:
        float: El valor del descuento aplicado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# -------------------------
# Programa principal
# -------------------------
# Primera llamada: usando solo el monto (se aplica el 10% por defecto)
monto1 = 200.0
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada: usando monto y un porcentaje personalizado
monto2 = 350.0
descuento2 = calcular_descuento(monto2, 20)  # aquí usamos 20% de descuento
monto_final2 = monto2 - descuento2

# -------------------------
# Salida de resultados
# -------------------------
print("------ Cálculo de Descuentos ------")
print(f"Compra 1 -> Monto: ${monto1:.2f} | Descuento: ${descuento1:.2f} | Monto final: ${monto_final1:.2f}")
print(f"Compra 2 -> Monto: ${monto2:.2f} | Descuento: ${descuento2:.2f} | Monto final: ${monto_final2:.2f}")
