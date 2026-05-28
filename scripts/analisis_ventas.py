import pandas as pd
import matplotlib.pyplot as plt

# Lectura del dataset utilizando rutas relativas
# para asegurar compatibilidad con Google Colab y GitHub.

df = pd.read_csv("datos/ventas2026.csv")

# Conversión de fechas
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Crear columna de mes
df["month"] = df["sales_date"].dt.to_period("M")

# =========================
# ANALISIS ESTADISTICO
# =========================

# Ventas totales
ventas_totales = df["sales_amount"].sum()

# Promedio de ventas
promedio_ventas = df["sales_amount"].mean()

# Ventas por mes
ventas_por_mes = df.groupby("month")["sales_amount"].sum()

# =========================
# RESULTADOS
# =========================

print("===== ANALISIS DE VENTAS =====")

print(f"\nVentas totales: {ventas_totales}")

print(f"\nPromedio de ventas: {promedio_ventas:.2f}")

print("\nVentas por mes:")
print(ventas_por_mes)

# =========================
# GRAFICO
# =========================

ventas_por_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")

# Guardar grafico en carpeta resultados
plt.savefig("resultados/grafico_ventas.png")

print("\nGrafico guardado en /resultados")
