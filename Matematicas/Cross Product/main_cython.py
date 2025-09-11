# main.py

import time
import random
from cross_product_cython import cross_product_cython

def generate_vectors(n):
    return [[random.random(), random.random(), random.random()] for _ in range(n)]

if __name__ == "__main__":
    # Generar datos aleatorios
    vectors_a = generate_vectors(10000)
    vectors_b = generate_vectors(10000)

    # Iniciar el cronómetro
    start_time = time.time()

    # Calcular el producto cruzado con Cython
    result = cross_product_cython(vectors_a, vectors_b)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
