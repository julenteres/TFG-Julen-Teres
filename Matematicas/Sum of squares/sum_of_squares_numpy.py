import numpy as np
import time

def sum_of_squares_numpy(n):
    return np.sum(np.arange(n) ** 2)

if __name__ == "__main__":
    start_time = time.time()

    result = sum_of_squares_numpy(100000)

    end_time = time.time()

    print(f"Resultado: {result}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
