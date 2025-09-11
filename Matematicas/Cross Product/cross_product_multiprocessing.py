import random
import time
import multiprocessing

def cross_product_worker(vectors_a, vectors_b, start, end, result):
    for i in range(start, end):
        ax, ay, az = vectors_a[i]
        bx, by, bz = vectors_b[i]
        result[i] = [
            ay * bz - az * by,
            az * bx - ax * bz,
            ax * by - ay * bx
        ]

def cross_product_multiprocessing(vectors_a, vectors_b):
    num_workers = 4
    chunk_size = len(vectors_a) // num_workers
    manager = multiprocessing.Manager()
    result = manager.list([None] * len(vectors_a))
    processes = []

    for i in range(num_workers):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_workers - 1 else len(vectors_a)
        p = multiprocessing.Process(target=cross_product_worker, args=(vectors_a, vectors_b, start, end, result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(result)

if __name__ == "__main__":
    # Generar datos aleatorios
    vectors_a = [[random.random() for _ in range(3)] for _ in range(10000)]
    vectors_b = [[random.random() for _ in range(3)] for _ in range(10000)]

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar el cálculo con multiprocessing
    result = cross_product_multiprocessing(vectors_a, vectors_b)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
