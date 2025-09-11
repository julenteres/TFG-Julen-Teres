import pandas as pd
from urllib.request import urlopen
import io
import time
import trace
import sys

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode("utf-8")
    column_names = ["S1","C1","S2","C2","S3","C3","S4","C4","S5","C5","CLASS"]
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def es_escalera(cartas):
    valores = sorted(cartas)

    # Caso normal
    if all(valores[i] + 1 == valores[i+1] for i in range(4)):
        return True

    # As bajo
    if valores == [1,2,3,4,5]:
        return True

    # As alto
    if valores == [1,10,11,12,13]:
        return True

    return False

def filtrar_escaleras():
    start_time = time.time()
    df = descargar_datos()
    columnas_cartas = ["C1","C2","C3","C4","C5"]
    df["es_escalera"] = df[columnas_cartas].apply(lambda row: es_escalera(row.values), axis=1)
    df_escaleras = df[df["es_escalera"]].copy()
    df_escaleras.to_csv("escaleras_poker.csv", index=False)
    end_time = time.time()

    print(df_escaleras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    with open("trace_filtrar_escaleras.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(filtrar_escaleras)
        sys.stdout = old_stdout
    filtrar_escaleras()

