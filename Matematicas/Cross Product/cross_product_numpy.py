import numpy as np
import time

def cross_product_numpy(vectors_a, vectors_b):
    return np.cross(vectors_a, vectors_b)

if __name__ == "__main__":
    # Generar datos aleatorios
    vectors_a = np.random.rand(10000, 3)
    vectors_b = np.random.rand(10000, 3)

    # Iniciar el cronómetro
    start_time = time.time()

    # Calcular el producto cruzado con NumPy
    result = cross_product_numpy(vectors_a, vectors_b)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
