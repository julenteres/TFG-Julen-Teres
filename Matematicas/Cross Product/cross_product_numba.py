import numpy as np
from numba import jit
import time

@jit(nopython=True)
def cross_product_numba(vectors_a, vectors_b):
    result = np.empty_like(vectors_a)
    for i in range(len(vectors_a)):
        result[i, 0] = vectors_a[i, 1] * vectors_b[i, 2] - vectors_a[i, 2] * vectors_b[i, 1]
        result[i, 1] = vectors_a[i, 2] * vectors_b[i, 0] - vectors_a[i, 0] * vectors_b[i, 2]
        result[i, 2] = vectors_a[i, 0] * vectors_b[i, 1] - vectors_a[i, 1] * vectors_b[i, 0]
    return result

if __name__ == "__main__":
    # Generar datos aleatorios de entrada
    vectors_a = np.random.rand(10000, 3)
    vectors_b = np.random.rand(10000, 3)

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la función optimizada con Numba
    result = cross_product_numba(vectors_a, vectors_b)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
