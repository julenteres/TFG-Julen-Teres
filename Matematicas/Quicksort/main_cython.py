import time
import random
from quicksort_cython import quicksort_cython

if __name__ == "__main__":
    # Generar una lista aleatoria de enteros
    data = [random.randint(1, 100000) for _ in range(10000)]

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar el quicksort en Cython
    sorted_data = quicksort_cython(data)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")



