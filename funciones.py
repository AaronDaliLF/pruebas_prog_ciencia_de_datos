# 1. Sumar dos números
def sumar(a, b):
    return a + b

# 2. Limpiar texto (eliminar espacios y pasar a minúsculas)
def limpiar_texto(texto):
    return texto.strip().lower()

# 3. Calcular promedio de una lista
def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else None

# 4. Contar valores únicos en una lista
def contar_unicos(lista):
    return len(set(lista))

# 5. Leer y filtrar un CSV por columna
import pandas as pd
def filtrar_csv(ruta, columna, valor):
    df = pd.read_csv(ruta)
    return df[df[columna] == valor]


#Llamada a las funciones

# 1. Sumar dos números
print(sumar(5, 3))  # → 8

# 2. Limpiar texto
print(limpiar_texto("  Hola Mundo  "))  # → "hola mundo"

# 3. Calcular promedio
print(calcular_promedio([4.5, 3.8, 5.0]))  # → 4.43...

# 4. Contar valores únicos
print(contar_unicos(["camisa", "pantalón", "camisa", "gorra"]))  # → 3

# 5. Filtrar CSV por columna (requiere archivo CSV)

resultado = filtrar_csv("/workspaces/pruebas_prog_ciencia_de_datos/data/prueba.csv","producto","Camisa")
print(resultado)

print("\nEntendiendo las estructuras de los dataframes")


#Entendiendo los dataframes → estos se pueden comprender como diccionarios de series

df = pd.DataFrame({
    "producto": ["Camisa", "Pantalón", "Gorra"],
    "precio": [35000, 65000, 15000]
})
print("El dataframe es el siguiente : \n")
print(df)

# Extraer la columna 'precio' como Series
serie_precio = df["precio"]

print(f"la serie de precios es :\n {serie_precio}")

total = serie_precio.sum()
media = serie_precio.mean()

print(f"el total calculado de los precios es: {total}")
print(f"la media/promedio de los precios es: {media}")