import time
import random
import multiprocessing

def generate_matrix(rows, cols):
    return [[random.random() for _ in range(cols)] for _ in range(rows)]

def matrix_multiplication_worker(A, B, start, end, result):
    for i in range(start, end):
        for j in range(len(B[0])):
            total = 0.0
            for k in range(len(A[0])):
                total += A[i][k] * B[k][j]
            result[i][j] = total

def matrix_multiplication_multiprocessing(A, B):
    num_workers = 4
    chunk_size = len(A) // num_workers
    manager = multiprocessing.Manager()
    result = manager.list([[0.0 for _ in range(len(B[0]))] for _ in range(len(A))])
    processes = []

    for i in range(num_workers):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_workers - 1 else len(A)
        p = multiprocessing.Process(target=matrix_multiplication_worker, args=(A, B, start, end, result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(result)

if __name__ == "__main__":
    # Generar matrices aleatorias sin NumPy
    A = generate_matrix(100, 100)
    B = generate_matrix(100, 100)

    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la multiplicación de matrices con multiprocessing
    result = matrix_multiplication_multiprocessing(A, B)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
