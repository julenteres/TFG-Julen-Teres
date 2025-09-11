# Cantidad_de_figuras_cython_main.pyx
import pandas as pd
from urllib.request import urlopen
import io
import http.client
import time

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data_bytes = b''
    while True:
        try:
            chunk = response.read(1024*1024)
            if not chunk:
                break
            data_bytes += chunk
        except http.client.IncompleteRead as e:
            data_bytes += e.partial
            break
    data = data_bytes.decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def contar_cartas_especiales_rolling(ventana_size=10):
    """
    Cuenta cartas J, Q, K, A en ventanas del dataset.
    """
    start_time = time.time()
    df = descargar_datos()
    cartas_array = df[['C1','C2','C3','C4','C5']].to_numpy()
    n_ventanas = (len(df) + ventana_size - 1) // ventana_size

    resultados = []
    for i in range(0, len(df), ventana_size):
        ventana = cartas_array[i:i+ventana_size]
        J = ((ventana == 11).sum())
        Q = ((ventana == 12).sum())
        K = ((ventana == 13).sum())
        A = ((ventana == 1).sum())
        resultados.append({
            'ventana_id': i//ventana_size + 1,
            'inicio_fila': i,
            'fin_fila': i + len(ventana) - 1,
            'J': J,
            'Q': Q,
            'K': K,
            'A': A,
            'total_cartas': ventana.size
        })

    df_result = pd.DataFrame(resultados)
    df_result.to_csv("Cantidad_de_figuras_cython.csv", index=False)
    end_time = time.time()
    print(df_result.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")
    return df_result

