# comparar_traces_mejorado.py
import re
import pandas as pd
from collections import Counter

def analizar_trace(trace_file):
    total_llamadas = 0
    funciones_counter = Counter()

    with open(trace_file, 'r') as f:
        for line in f:
            line = line.strip()
            match = re.match(r'--- modulename: ([^,]+), funcname: ([^\s]+)', line)
            if match:
                modulename, funcname = match.groups()
                total_llamadas += 1
                funciones_counter[(modulename, funcname)] += 1

    # función más llamada
    mas_costosa = "N/A (0)"
    if funciones_counter:
        mas_costosa_global = max(funciones_counter.items(), key=lambda x: x[1])
        mas_costosa = f"{mas_costosa_global[0][0]}.{mas_costosa_global[0][1]} ({mas_costosa_global[1]})"

    return {
        "trace": trace_file,
        "total_llamadas": total_llamadas,
        "mas_costosa": mas_costosa
    }

def comparar_traces(lista_traces):
    resultados = [analizar_trace(trace) for trace in lista_traces]
    df_resultados = pd.DataFrame(resultados)
    df_resultados = df_resultados.sort_values(by='total_llamadas', ascending=False)
    return df_resultados

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python3 comparar_traces_mejorado.py trace1.txt trace2.txt ...")
        sys.exit(1)

    traces = sys.argv[1:]
    df_comparativa = comparar_traces(traces)

    print("\nComparativa de programas (basado en traces):")
    print(df_comparativa.to_string(index=False))

    df_comparativa.to_csv("comparativa_traces.csv", index=False)
    print("\nTabla guardada en 'comparativa_traces.csv'")

