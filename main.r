
# --- Definimos funciones reutilizables ---

# 1. Cargar datos
cargar_datos <- function(ruta_csv) {
  df <- read.csv(ruta_csv, stringsAsFactors = FALSE)
  return(df)
}

# 2. Limpiar nombres de columnas
limpiar_columnas <- function(df) {
  names(df) <- tolower(trimws(names(df)))
  return(df)
}

# 3. Eliminar filas con valores NA
eliminar_na <- function(df) {
  df <- na.omit(df)
  return(df)
}

# 4. Crear una nueva columna calculada
crear_total <- function(df, col_precio, col_cantidad) {
  df$total <- df[[col_precio]] * df[[col_cantidad]]
  return(df)
}

# 5. Guardar resultados
guardar_datos <- function(df, ruta_salida) {
  write.csv(df, ruta_salida, row.names = FALSE)
  message("Archivo guardado en: ", ruta_salida)
}

# --- Uso de las funciones en conjunto ---

# Cambia esta ruta a la ubicación real de tu archivo
ruta_entrada <- "/workspaces/pruebas_prog_ciencia_de_datos/data/ventas.csv"
ruta_salida <- "/workspaces/pruebas_prog_ciencia_de_datos/data/ventas_procesadas_r.csv"

# Flujo de procesamiento
df <- cargar_datos(ruta_entrada)
df <- limpiar_columnas(df)
df <- eliminar_na(df)
df <- crear_total(df, "precio", "cantidad")
guardar_datos(df, ruta_salida)

# Resumen de resultados
print(summary(df))

