# --- Importar librerías ---

import auxiliar as aux


# 2. Limpiar nombres de columnas
def limpiar_columnas(df):
    df.columns = [col.strip().lower() for col in df.columns]
    return df

# 3. Eliminar filas con valores NA
def eliminar_na(df):
    return df.dropna()

# 4. Crear una nueva columna calculada
def crear_total(df, col_precio, col_cantidad):
    df["total"] = df[col_precio] * df[col_cantidad]
    return df

# 5. Guardar resultados
def guardar_datos(df, ruta_salida):
    df.to_csv(ruta_salida, index=False)
    print(f"Archivo guardado en: {ruta_salida}")

# --- Uso de las funciones en conjunto ---

# Cambia estas rutas a la ubicación real de tus archivos
ruta_entrada = r"/workspaces/pruebas_prog_ciencia_de_datos/data/ventas.csv"
ruta_salida  = r"/workspaces/pruebas_prog_ciencia_de_datos/data/ventas_procesadas_python.csv"

# Flujo de procesamiento

df = aux.cargar_datos(ruta_entrada)
df = limpiar_columnas(df)
df = eliminar_na(df)
df = crear_total(df, "precio", "cantidad")
guardar_datos(df, ruta_salida)

# Resumen de resultados
print(df.describe())
print(df.head())
