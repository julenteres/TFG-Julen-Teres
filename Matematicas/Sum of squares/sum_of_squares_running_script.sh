#!/bin/bash

# Asegurar que se pase un archivo como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <programa_python.py>"
    exit 1
fi

PROGRAM=$1

if [ ! -f "$PROGRAM" ]; then
    echo "Archivo '$PROGRAM' no encontrado."
    exit 2
fi

# Sacar nombre base y timestamp para guardar
BASE_NAME=$(basename "$PROGRAM" .py)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTPUT_FILE="/home/pochomen/Escritorio/ftrace_${BASE_NAME}_${TIMESTAMP}.txt"

# Ir al directorio de ftrace
cd /sys/kernel/debug/tracing || { echo "No se puede acceder a /sys/kernel/debug/tracing (¿tienes root?)"; exit 3; }

# Configurar ftrace para ver llamadas al sistema
sudo bash -c "
echo > trace
echo function_graph > current_tracer
#echo syscalls > current_tracer
echo 0 > tracing_on
echo 1 > options/trace_children
echo 1 > tracing_on
"

# Ejecutar el programa
python3 "$PROGRAM"

# Parar ftrace
sudo bash -c "echo 0 > tracing_on"

# Guardar la traza completa
sudo cp trace "$OUTPUT_FILE"
sudo chown $USER:$USER "$OUTPUT_FILE"

# Mostrar resultado
echo "? Syscalls guardadas en: $OUTPUT_FILE"
less "$OUTPUT_FILE"

