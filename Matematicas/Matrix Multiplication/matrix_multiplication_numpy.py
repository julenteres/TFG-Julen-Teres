import numpy as np
import time

def matrix_multiplication_numpy(A, B):
    return np.dot(A, B)

if __name__ == "__main__":
    # Generar matrices aleatorias
    A = np.random.rand(100, 100)
    B = np.random.rand(100, 100)

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la multiplicación de matrices con NumPy
    result = matrix_multiplication_numpy(A, B)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
