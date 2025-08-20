import pandas as pd
# 1. Cargar datos
def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    return df