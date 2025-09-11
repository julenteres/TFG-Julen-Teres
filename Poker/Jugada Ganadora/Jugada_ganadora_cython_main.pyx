# cython: language_level=3
import pandas as pd
from urllib.request import urlopen
import io

def descargar_datos():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
    response = urlopen(url)
    data = response.read().decode('utf-8')
    column_names = ['S1','C1','S2','C2','S3','C3','S4','C4','S5','C5','CLASS']
    return pd.read_csv(io.StringIO(data), header=None, names=column_names)

def Jugada_ganadora_cy():
    import time
    start_time = time.time()
    df = descargar_datos()
    ventana_size = 20
    jugadas_ganadoras = []
    indices_ventanas = []

    for i in range(0, len(df), ventana_size):
        ventana = df.iloc[i:i+ventana_size]
        if len(ventana) > 0:
            mejor_jugada_idx = ventana['CLASS'].idxmax()
            jugada_ganadora = df.loc[mejor_jugada_idx]
            jugadas_ganadoras.append(jugada_ganadora)
            indices_ventanas.append(f"Ventana {i//ventana_size + 1} (filas {i}-{i+len(ventana)-1})")

    df_ganadoras = pd.DataFrame(jugadas_ganadoras)
    df_ganadoras['ventana'] = indices_ventanas
    df_ganadoras = df_ganadoras[['ventana','C1','C2','C3','C4','C5','CLASS']]
    df_ganadoras.to_csv('jugadas_ganadoras_cy.csv', index=False)

    end_time = time.time()
    print(df_ganadoras.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

