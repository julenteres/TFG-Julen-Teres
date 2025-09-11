import pandas as pd
from urllib.request import urlopen
import io
import time
import trace
import sys
from multiprocessing import Pool, cpu_count

def descargar_datos():
    """Descarga los datos de poker hand desde UCI"""
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def procesar_ventana(args):
    """Procesa una ventana y devuelve la jugada ganadora con ventana"""
    df, i, ventana_size = args
    ventana = df.iloc[i:i+ventana_size]
    if len(ventana) == 0:
        return None
    # Solo seleccionamos columnas necesarias
    idx = ventana['CLASS'].idxmax()
    jugada = df.loc[idx, ['C1','C2','C3','C4','C5','CLASS']]
    ventana_str = f"Ventana {i//ventana_size + 1} (filas {i}-{i+len(ventana)-1})"
    return jugada.tolist() + [ventana_str]

def Jugada_ganadora_mp():
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 20

    # Preparar argumentos para cada ventana
    args_list = [(df, i, ventana_size) for i in range(0, len(df), ventana_size)]

    # Ejecutar en paralelo
    with Pool(processes=cpu_count()) as pool:
        resultados = pool.map(procesar_ventana, args_list)

    # Filtrar posibles None
    resultados = [r for r in resultados if r is not None]

    # Crear DataFrame final con columnas correctas
    df_ganadoras = pd.DataFrame(resultados, columns=['C1','C2','C3','C4','C5','CLASS','ventana'])
    df_ganadoras.to_csv('jugadas_ganadoras_multiprocessing.csv', index=False)

    end_time = time.time()

    # Mostrar resultados finales
    print(df_ganadoras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

if __name__ == "__main__":
    # Crear trace en archivo sin mostrar en pantalla
    tracer = trace.Trace(trace=True, count=False)
    with open("trace_jugada_ganadora_multiprocessing.txt", "w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(Jugada_ganadora_mp)
        sys.stdout = old_stdout

    # Ejecutar otra vez para mostrar resultados finales
    Jugada_ganadora_mp()

