from numba import njit
import random
import time

@njit
def random_walk_numba(n):
    x, y = 0, 0
    for _ in range(n):
        dx = 1 if random.random() < 0.5 else -1
        dy = 1 if random.random() < 0.5 else -1
        x += dx
        y += dy
    return x, y

if __name__ == "__main__":
    start_time = time.time()

    result = random_walk_numba(1000000)

    end_time = time.time()

    print(f"Resultado: x={result[0]}, y={result[1]}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
