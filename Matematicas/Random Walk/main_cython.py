from random_walk_cython import random_walk_cython
import time

if __name__ == "__main__":
    n = 1000000  # Número de pasos

    start_time = time.time()

    x, y = random_walk_cython(n)

    end_time = time.time()

    print(f"Resultado del random walk tras {n} pasos: x={x}, y={y}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")

