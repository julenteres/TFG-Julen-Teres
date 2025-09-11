# Filtrar_escaleras_multiprocessing.py
import pandas as pd
from urllib.request import urlopen
import io, time, sys, trace
from multiprocessing import Pool, cpu_count

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names=['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def es_escalera(cartas):
    valores = sorted(cartas)
    if all(valores[i]+1 == valores[i+1] for i in range(4)):
        return True
    if valores == [1,2,3,4,5] or valores == [1,10,11,12,13]:
        return True
    return False

def procesar_chunk(chunk):
    resultados = []
    for row in chunk:
        resultados.append(es_escalera(row))
    return resultados

def filtrar_escaleras_mp():
    df = descargar_datos()
    cartas = df[['C1','C2','C3','C4','C5']].values.tolist()

    # Dividir en chunks grandes para reducir overhead
    n = cpu_count()
    chunk_size = len(cartas) // n
    chunks = [cartas[i:i+chunk_size] for i in range(0, len(cartas), chunk_size)]

    with Pool(n) as p:
        resultados = p.map(procesar_chunk, chunks)

    # Aplanar lista de resultados
    resultados = [item for sublist in resultados for item in sublist]

    df['es_escalera'] = resultados
    df_escaleras = df[df['es_escalera']].copy()
    df_escaleras.to_csv("escaleras_poker_mp.csv", index=False)
    return df_escaleras

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    trace_file = "trace_filtrar_escaleras_multiprocessing.txt"
    with open(trace_file,"w") as f:
        old_stdout=sys.stdout
        sys.stdout=f
        start=time.time()
        df_final=tracer.runfunc(filtrar_escaleras_mp)
        end=time.time()
        sys.stdout=old_stdout

    print(df_final.head())
    print(f"\nTiempo de ejecución: {end-start:.2f} s")

