# jugada_ganadora_numpy.py
import pandas as pd
import numpy as np
from urllib.request import urlopen
import io
import time
import trace
import sys

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    data = urlopen(url).read().decode("utf-8")
    columns = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=columns)

def jugada_ganadora_np_vectorizado(ventana_size=20):
    start_time = time.time()
    
    # Cargar datos
    df = descargar_datos()
    clase_arr = df['CLASS'].to_numpy()
    n_filas = len(clase_arr)
    
    # Número de ventanas
    n_ventanas = (n_filas + ventana_size - 1) // ventana_size
    
    # Rellenar clase_arr para que sea múltiplo de ventana_size
    padding = n_ventanas * ventana_size - n_filas
    if padding > 0:
        clase_arr_padded = np.concatenate([clase_arr, -np.inf*np.ones(padding)])
    else:
        clase_arr_padded = clase_arr

    # Reshape en ventanas
    clase_reshaped = clase_arr_padded.reshape(n_ventanas, ventana_size)
    
    # Índices del máximo por ventana
    max_indices = np.argmax(clase_reshaped, axis=1)
    
    # Índices globales en el DataFrame original
    global_indices = np.arange(0, n_ventanas*ventana_size, ventana_size) + max_indices
    global_indices = global_indices[global_indices < n_filas]  # eliminar padding si existe

    # Crear DataFrame final
    df_ganadoras = df.iloc[global_indices].copy()
    ventana_labels = [
        f"Ventana {i+1} (filas {i*ventana_size}-{min((i+1)*ventana_size-1, n_filas-1)})"
        for i in range(len(global_indices))
    ]
    df_ganadoras['ventana'] = ventana_labels
    df_ganadoras = df_ganadoras[['ventana','C1','C2','C3','C4','C5','CLASS']]
    
    # Guardar CSV
    df_ganadoras.to_csv('jugadas_ganadoras_numpy.csv', index=False)
    
    end_time = time.time()
    print(df_ganadoras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    # Trace opcional
    with open("trace_jugada_ganadora_numpy.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer = trace.Trace(trace=True, count=False)
        tracer.runfunc(jugada_ganadora_np_vectorizado)
        sys.stdout = old_stdout

    jugada_ganadora_np_vectorizado()

