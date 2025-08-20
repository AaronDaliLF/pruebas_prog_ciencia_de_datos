# 1. Sumar dos números
sumar <- function(a, b) {
  return(a + b)
}

# 2. Limpiar texto (trim y lowercase)
limpiar_texto <- function(texto) {
  return(tolower(trimws(texto)))
}

# 3. Calcular promedio de un vector
calcular_promedio <- function(vec) {
  if (length(vec) == 0) return(NA)
  return(mean(vec))
}

# 4. Contar valores únicos
contar_unicos <- function(vec) {
  return(length(unique(vec)))
}

# 5. Leer y filtrar un CSV por columna
filtrar_csv <- function(ruta, columna, valor) {
  df <- read.csv(ruta)
  return(subset(df, df[[columna]] == valor))
}

#LLamada a las funciones

# 1. Sumar dos números
print(sumar(5, 3))  # → 8

# 2. Limpiar texto
print(limpiar_texto("  Hola Mundo  "))  # → "hola mundo"

# 3. Calcular promedio
print(calcular_promedio(c(4.5, 3.8, 5.0)))  # → 4.43...

# 4. Contar valores únicos
print(contar_unicos(c("camisa", "pantalón", "camisa", "gorra")))  # → 3

# 5. Filtrar CSV por columna (requiere archivo CSV)
# Supongamos que el archivo tiene una columna "producto"
resultado <- filtrar_csv("/workspaces/pruebas_prog_ciencia_de_datos/data/prueba.csv","producto","Camisa")
print(resultado)