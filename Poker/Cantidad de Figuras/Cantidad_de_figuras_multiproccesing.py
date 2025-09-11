import pandas as pd
from urllib.request import urlopen
import io
import time
import trace
import sys
from multiprocessing import Pool, cpu_count
from itertools import chain

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def procesar_ventana(args):
    ventana, i, ventana_size = args
    columnas_cartas = ['C1','C2','C3','C4','C5']
    if len(ventana) == 0: 
        return None
    todas_cartas = list(chain.from_iterable(ventana[columnas_cartas].values))
    conteo = {
        'ventana_id': i//ventana_size+1,
        'inicio_fila': i,
        'fin_fila': i+len(ventana)-1,
        'J': sum(1 for x in todas_cartas if x==11),
        'Q': sum(1 for x in todas_cartas if x==12),
        'K': sum(1 for x in todas_cartas if x==13),
        'A': sum(1 for x in todas_cartas if x==1),
        'total_cartas': len(todas_cartas)
    }
    return conteo

def contar_cartas_especiales_mp():
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 10
    args_list = [(df.iloc[i:i+ventana_size], i, ventana_size) for i in range(0, len(df), ventana_size)]

    with Pool(cpu_count()) as pool:
        resultados = pool.map(procesar_ventana, args_list)

    resultados = [r for r in resultados if r is not None]
    df_conteo = pd.DataFrame(resultados)
    df_conteo.to_csv('conteo_cartas_multiprocessing.csv', index=False)
    end_time = time.time()
    print(df_conteo.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    with open("trace_conteo_cartas_multiprocessing.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(contar_cartas_especiales_mp)
        sys.stdout = old_stdout
    contar_cartas_especiales_mp()

