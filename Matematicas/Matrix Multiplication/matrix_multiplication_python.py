import random
import time

def matrix_multiplication_python(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

if __name__ == "__main__":
    A = [[random.random() for _ in range(100)] for _ in range(100)]
    B = [[random.random() for _ in range(100)] for _ in range(100)]
    start_time = time.time()
    result = matrix_multiplication_python(A, B)
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
