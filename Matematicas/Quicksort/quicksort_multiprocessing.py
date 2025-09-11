import multiprocessing
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_worker(sublist, conn):
    sorted_sublist = quicksort(sublist)
    conn.send(sorted_sublist)
    conn.close()

def quicksort_multiprocessing(arr, num_workers=4):
    # Dividir la lista en partes iguales
    chunk_size = len(arr) // num_workers
    chunks = [arr[i*chunk_size : (i+1)*chunk_size] for i in range(num_workers - 1)]
    chunks.append(arr[(num_workers - 1)*chunk_size:])  # Resto de elementos

    processes = []
    parent_conns = []

    for chunk in chunks:
        parent_conn, child_conn = multiprocessing.Pipe()
        p = multiprocessing.Process(target=quicksort_worker, args=(chunk, child_conn))
        processes.append(p)
        parent_conns.append(parent_conn)
        p.start()

    sorted_chunks = [conn.recv() for conn in parent_conns]

    for p in processes:
        p.join()

    # Combinar los trozos ordenados
    merged = []
    for chunk in sorted_chunks:
        merged.extend(chunk)

    # Ordenado final de la lista completa
    return quicksort(merged)

if __name__ == "__main__":
    # Generar datos aleatorios sin NumPy
    data = [random.randint(1, 100000) for _ in range(10000)]

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la ordenación con multiprocessing
    sorted_data = quicksort_multiprocessing(data)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
