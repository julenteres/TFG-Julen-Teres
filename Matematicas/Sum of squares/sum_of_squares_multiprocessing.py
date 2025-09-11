from multiprocessing import Pool
import time

def worker(i):
    return i ** 2

def sum_of_squares_mp(n):
    with Pool() as pool:
        return sum(pool.map(worker, range(n)))

if __name__ == "__main__":
    start_time = time.time()

    result = sum_of_squares_mp(100000)

    end_time = time.time()
    print(f"Resultado: {result}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
