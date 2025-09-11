import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Inicia el cronómetro
    start_time = time.time()

    # Genera datos aleatorios
    data = [random.randint(1, 100000) for _ in range(10000)]

    # Ejecuta la ordenación con quicksort
    sorted_data = quicksort(data)

    # Finaliza el cronómetro
    end_time = time.time()

    # Muestra el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
