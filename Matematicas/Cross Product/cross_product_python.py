import time

def cross_product_python(vectors_a, vectors_b):
    result = []
    for a, b in zip(vectors_a, vectors_b):
        result.append([
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        ])
    return result

if __name__ == "__main__":
    vectors_a = [[i, i + 1, i + 2] for i in range(10000)]
    vectors_b = [[i + 3, i + 4, i + 5] for i in range(10000)]
    start_time = time.time()
    result = cross_product_python(vectors_a, vectors_b)
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
