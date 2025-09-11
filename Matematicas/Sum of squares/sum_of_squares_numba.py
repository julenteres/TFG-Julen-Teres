import numba
import time

@numba.jit(nopython=True)
def sum_of_squares_numba(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

if __name__ == "__main__":
    start_time = time.time()

    result = sum_of_squares_numba(100000)

    end_time = time.time()
    print(f"Resultado: {result}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

