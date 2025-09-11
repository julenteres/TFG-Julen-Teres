import time

def sum_of_squares(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

if __name__ == "__main__":
    start_time = time.time()
    sum_of_squares(100000)
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")