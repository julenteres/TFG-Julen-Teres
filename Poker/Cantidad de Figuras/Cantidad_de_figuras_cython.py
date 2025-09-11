# Cantidad_de_figuras_cython.py
import sys
import trace
import time
from Cantidad_de_figuras_cython_main import contar_cartas_especiales_rolling

if __name__ == "__main__":
    tracer = trace.Trace(trace=True, count=False)
    trace_file = "trace_Cantidad_de_figuras_cython.txt"
    
    with open(trace_file, "w") as f:
        old_stdout = sys.stdout
        sys.stdout = f
        tracer.runfunc(contar_cartas_especiales_rolling)
        sys.stdout = old_stdout

    # Ejecutar la función normalmente para mostrar resultados en pantalla
    contar_cartas_especiales_rolling()

