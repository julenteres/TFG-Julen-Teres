import pandas as pd
from urllib.request import urlopen
import io
import time
import trace
import sys
from numba import njit

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

@njit
def idxmax(arr):
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_idx

def Jugada_ganadora_nb():
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 20
    jugadas_ganadoras = []
    indices_ventanas = []

    for i in range(0, len(df), ventana_size):
        ventana = df.iloc[i:i+ventana_size]
        if len(ventana) > 0:
            clase_arr = ventana['CLASS'].to_list()
            mejor_idx = idxmax(clase_arr)
            jugada = ventana.iloc[mejor_idx]
            jugadas_ganadoras.append(jugada)
            indices_ventanas.append(f"Ventana {i//ventana_size + 1} (filas {i}-{i+len(ventana)-1})")

    df_ganadoras = pd.DataFrame(jugadas_ganadoras)
    df_ganadoras['ventana'] = indices_ventanas
    df_ganadoras = df_ganadoras[['ventana','C1','C2','C3','C4','C5','CLASS']]
    df_ganadoras.to_csv('jugadas_ganadoras_numba.csv', index=False)

    end_time = time.time()
    print(df_ganadoras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    with open("trace_jugada_ganadora_numba.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer = trace.Trace(trace=True, count=False)
        tracer.runfunc(Jugada_ganadora_nb)
        sys.stdout = old_stdout

    Jugada_ganadora_nb()

