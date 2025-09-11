import random
import time
import multiprocessing

def random_walk_worker(num_steps, queue):
    x, y = 0, 0
    for _ in range(num_steps):
        x += random.choice([-1, 1])
        y += random.choice([-1, 1])
    queue.put((x, y))

def random_walk_multiprocessing(n):
    num_workers = 4
    steps_per_worker = n // num_workers
    queue = multiprocessing.Queue()
    processes = []

    for _ in range(num_workers):
        p = multiprocessing.Process(target=random_walk_worker, args=(steps_per_worker, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Sumar los resultados de cada proceso
    total_x, total_y = 0, 0
    while not queue.empty():
        x, y = queue.get()
        total_x += x
        total_y += y

    return total_x, total_y

if __name__ == "__main__":
    start_time = time.time()

    result = random_walk_multiprocessing(1000000)

    end_time = time.time()

    print(f"Resultado: x={result[0]}, y={result[1]}")
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
