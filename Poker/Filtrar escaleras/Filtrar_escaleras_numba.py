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
    data = response.read().decode("utf-8")
    column_names = ["S1","C1","S2","C2","S3","C3","S4","C4","S5","C5","CLASS"]
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

@njit
def es_escalera(cartas):
    # Ordenar (burbuja para Numba)
    for i in range(4):
        for j in range(0, 4-i):
            if cartas[j] > cartas[j+1]:
                cartas[j], cartas[j+1] = cartas[j+1], cartas[j]

    # Caso normal
    consecutiva = True
    for i in range(4):
        if cartas[i] + 1 != cartas[i+1]:
            consecutiva = False
            break
    if consecutiva:
        return True

    # As bajo
    if cartas[0]==1 and cartas[1]==2 and cartas[2]==3 and cartas[3]==4 and cartas[4]==5:
        return True

    # As alto
    if set(cartas) == {1,10,11,12,13}:
        return True

    return False

def filtrar_escaleras():
    start_time = time.time()
    df = descargar_datos()
    columnas_cartas = ["C1","C2","C3","C4","C5"]
    manos = df[columnas_cartas].values.tolist()
    resultados = [es_escalera(mano) for mano in manos]
    df["es_escalera"] = resultados
    df_escaleras = df[df["es_escalera"]].copy()
    df_escaleras.to_csv("escaleras_poker_numba.csv", index=False)
    end_time = time.time()

    print(df_escaleras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    with open("trace_filtrar_escaleras_numba.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer = trace.Trace(trace=True, count=False)
        tracer.runfunc(filtrar_escaleras)
        sys.stdout = old_stdout

    filtrar_escaleras()

