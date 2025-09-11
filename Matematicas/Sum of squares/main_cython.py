import time
from sum_of_squares_cython import sum_of_squares_cython

if __name__ == "__main__":
    start = time.time()
    sum_of_squares_cython(100000)
    end = time.time()

    print(f"Tiempo de ejecución: {end - start:.6f} segundos")

