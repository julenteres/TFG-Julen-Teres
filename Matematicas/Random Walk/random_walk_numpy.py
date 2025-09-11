import numpy as np
import time

def random_walk_numpy(n):
    steps = np.random.choice([-1, 1], size=(n, 2))
    return steps.sum(axis=0)

if __name__ == "__main__":
    # Iniciar el cronómetro
    start_time = time.time()

    # Ejecutar la función directamente
    result = random_walk_numpy(1000000)

    # Finalizar el cronómetro
    end_time = time.time()

    # Mostrar el tiempo de ejecución
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
