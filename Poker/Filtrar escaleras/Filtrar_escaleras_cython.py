import time
import trace
import sys
from Filtrar_escaleras_cython_main import Filtrar_escaleras  # import de la librería compilada

if __name__ == "__main__":
    # Guardar trace en un txt
    with open("trace_filtrar_escaleras_cython.txt", "w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer = trace.Trace(trace=True, count=False)
        tracer.runfunc(Filtrar_escaleras)
        sys.stdout = old_stdout

    # Ejecutar función y medir tiempo
    start_time = time.time()
    df_resultado = Filtrar_escaleras()
    end_time = time.time()

    # Mostrar dataframe final y tiempo de ejecución
    print(df_resultado.head())
    print(f"\nTiempo de ejecución: {end_time - start_time:.2f} s")

