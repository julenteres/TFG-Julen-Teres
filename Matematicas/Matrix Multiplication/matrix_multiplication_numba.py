import numpy as np
from numba import njit
import time

# Crear matrices con NumPy (random)
def create_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Multiplicación manual con Numba
@njit
def matrix_multiplication_numba(A, B):
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    result = np.zeros((rows_A, cols_B))

    for i in range(rows_A):
        for j in range(cols_B):
            suma = 0.0
            for k in range(cols_A):
                suma += A[i, k] * B[k, j]
            result[i, j] = suma

    return result

if __name__ == "__main__":
    A = create_random_matrix(100, 100)
    B = create_random_matrix(100, 100)

    start = time.time()
    result = matrix_multiplication_numba(A, B)
    end = time.time()

    print(f"Tiempo de ejecución: {end - start:.6f} segundos")

