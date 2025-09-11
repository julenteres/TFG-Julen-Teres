from numba import njit
import random
import time

@njit
def quicksort_numba(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort_numba(left) + middle + quicksort_numba(right)

if __name__ == "__main__":
    # Generar lista aleatoria sin NumPy
    data = [random.randint(1, 100000) for _ in range(10000)]

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la ordenación rápida optimizada con Numba
    sorted_data = quicksort_numba(data)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
