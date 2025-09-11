import numpy as np
import time

if __name__ == "__main__":
    # Generar datos aleatorios
    data = np.random.randint(1, 100000, 10000)

    # Iniciar el cronómetro
    start_time = time.time()

    # Ordenar el array usando NumPy
    sorted_data = np.sort(data)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
