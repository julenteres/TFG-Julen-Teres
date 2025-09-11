# Filtrar_escaleras_cython_main.pyx

import pandas as pd
from urllib.request import urlopen
import io

# ----------------------------------------------------------------------
# Función para descargar datos
# ----------------------------------------------------------------------
def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

# ----------------------------------------------------------------------
# Función para detectar si una mano es escalera
# ----------------------------------------------------------------------
def es_escalera(cartas):
    """
    cartas: lista de 5 enteros con los valores de las cartas
    """
    valores = sorted(cartas)

    # Escalera normal (ej: 5-6-7-8-9)
    cdef int i
    if all(valores[i] + 1 == valores[i+1] for i in range(4)):
        return True

    # Escalera con As bajo (A-2-3-4-5)
    if valores == [1,2,3,4,5]:
        return True

    # Escalera con As alto (10-J-Q-K-A)
    if set(valores) == {1,10,11,12,13}:
        return True

    return False

# ----------------------------------------------------------------------
# Función principal para filtrar escaleras
# ----------------------------------------------------------------------
def Filtrar_escaleras():
    df = descargar_datos()
    columnas_cartas = ['C1','C2','C3','C4','C5']

    # Aplicar la función es_escalera a cada fila
    df['es_escalera'] = df[columnas_cartas].apply(lambda row: es_escalera(row.values.tolist()), axis=1)

    # Filtrar solo las filas con escaleras
    df_escaleras = df[df['es_escalera']].copy()

    # Guardar a CSV
    df_escaleras.to_csv('escaleras_poker_cython.csv', index=False)

    return df_escaleras

