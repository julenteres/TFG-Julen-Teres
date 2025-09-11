import random
import time
from matrix_multiplication_cython import matrix_multiplication_cython

def generar_matriz(filas, columnas):
    return [[random.random() for _ in range(columnas)] for _ in range(filas)]

if __name__ == "__main__":
    A = generar_matriz(100, 100)
    B = generar_matriz(100, 100)

    start_time = time.time()

    result = matrix_multiplication_cython(A, B)

    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
