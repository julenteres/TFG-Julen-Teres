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
def contar_cartas_especiales_rolling_numba(flat_cartas):
    J=Q=K=A=0
    for c in flat_cartas:
        if c==11: J+=1
        elif c==12: Q+=1
        elif c==13: K+=1
        elif c==1: A+=1
    return J,Q,K,A,len(flat_cartas)

def contar_cartas_especiales_numba():
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 10
    columnas_cartas = ['C1','C2','C3','C4','C5']
    resultados = []

    for i in range(0,len(df),ventana_size):
        ventana = df.iloc[i:i+ventana_size]
        if len(ventana) > 0:
            todas_cartas = ventana[columnas_cartas].to_numpy().flatten()
            J,Q,K,A,total = contar_cartas_especiales_rolling_numba(todas_cartas)
            resultados.append({
                'ventana_id': i//ventana_size+1,
                'inicio_fila': i,
                'fin_fila': i+len(ventana)-1,
                'J': J,
                'Q': Q,
                'K': K,
                'A': A,
                'total_cartas': total
            })

    df_conteo = pd.DataFrame(resultados)
    df_conteo.to_csv('conteo_cartas_numba.csv', index=False)
    end_time = time.time()
    print(df_conteo.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    with open("trace_conteo_cartas_numba.txt","w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(contar_cartas_especiales_numba)
        sys.stdout = old_stdout
    contar_cartas_especiales_numba()

