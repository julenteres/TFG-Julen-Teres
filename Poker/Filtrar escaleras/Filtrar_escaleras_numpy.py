# filtrar_escaleras_numpy_max_vectorizado.py
import pandas as pd
import numpy as np
from urllib.request import urlopen
import io
import time

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    columns = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=columns)

def filtrar_escaleras_vectorizado():
    start_time = time.time()
    
    df = descargar_datos()
    cartas = df[['C1','C2','C3','C4','C5']].values.astype(np.int8)

    # Ordenamos todas las filas (vectorizado)
    cartas_ordenadas = np.sort(cartas, axis=1)

    # Escalera normal: diferencias = 1
    diff = np.diff(cartas_ordenadas, axis=1)
    escalera_normal = np.all(diff == 1, axis=1)

    # Escalera 1-5 o 10-J-Q-K-A (broadcasting)
    especiales = np.array([[1,2,3,4,5],[1,10,11,12,13]], dtype=np.int8)
    escalera_especial = np.any(np.all(cartas_ordenadas[:, None, :] == especiales[None, :, :], axis=2), axis=1)

    # Combinamos
    es_escalera = escalera_normal | escalera_especial

    # Guardamos resultados
    df['es_escalera'] = es_escalera
    df_escaleras = df[df['es_escalera']].copy()
    df_escaleras.to_csv("escaleras_poker_vectorizado_max.csv", index=False)
    
    end_time = time.time()
    print(df_escaleras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    filtrar_escaleras_vectorizado()

