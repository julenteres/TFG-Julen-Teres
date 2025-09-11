import random
import time

def random_walk_python(n):
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy
    return x, y

if __name__ == "__main__":
    start_time = time.time()
    result = random_walk_python(1000000)
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
