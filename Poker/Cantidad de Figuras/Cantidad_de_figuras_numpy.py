import pandas as pd
import numpy as np
from urllib.request import urlopen
import io
import time
import trace
import sys

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def contar_cartas_especiales_numpy():
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 10
    columnas_cartas = ['C1','C2','C3','C4','C5']
    resultados = []

    for i in range(0, len(df), ventana_size):
        ventana = df.iloc[i:i+ventana_size]
        if len(ventana) > 0:
            todas_cartas = ventana[columnas_cartas].to_numpy().flatten()
            counts = np.bincount(todas_cartas, minlength=14)  # cuenta todas las cartas de 1 a 13
            resultados.append({
                'ventana_id': i//ventana_size + 1,
                'inicio_fila': i,
                'fin_fila': i + len(ventana) - 1,
                'J': counts[11],
                'Q': counts[12],
                'K': counts[13],
                'A': counts[1],
                'total_cartas': len(todas_cartas)
            })

    df_conteo = pd.DataFrame(resultados)
    df_conteo.to_csv('conteo_cartas_numpy.csv', index=False)
    end_time = time.time()
    print(df_conteo.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    with open("trace_conteo_cartas_numpy.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(contar_cartas_especiales_numpy)
        sys.stdout = old_stdout
    contar_cartas_especiales_numpy()

