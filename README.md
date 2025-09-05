# TFG-Julen-Teres
Este proyecto analiza y compara distintas técnicas de optimización en Python —NumPy, Numba JIT, Cython y Multiprocessing— aplicadas a algoritmos numéricos y problemas basados en el Poker Hand Dataset. Se evalúan tiempos de ejecución, eficiencia y escalabilidad mediante métricas de rendimiento.

Proyecto: Optimización de Código en Python: Comparativa de Técnicas de Alto Rendimiento

------------------------------------------------------------------------------------------------------------------

1.-Descripción:

Este proyecto analiza y compara distintas técnicas de optimización en Python para problemas que requieren alto poder de cálculo. Se evalúan cinco enfoques: Python puro, Cython, Multiprocesamiento, Numba (JIT) y NumPy, aplicados a dos tipos de problemas:

1. Procesamiento de datos de póker: filtrado de escaleras, determinación de la jugada ganadora en bloques de manos y conteo de cartas con figuras (J, Q, K, A).
2. Algoritmos matemáticos y computacionales: suma de cuadrados, caminata aleatoria, quicksort, multiplicación de matrices y producto cruzado.

El objetivo es estudiar el impacto de cada técnica sobre la eficiencia estructural, número de llamadas a funciones y tiempos de ejecución, y proporcionar una guía sobre cuándo usar cada enfoque.

------------------------------------------------------------------------------------------------------------------

2.-Requisitos e Instalación:

Se recomienda crear un entorno virtual e instalar las dependencias necesarias:
- numpy >= 1.25.0
- pandas >= 2.1.0
- cython >= 0.30.0
- numba >= 0.57.0
- matplotlib >= 3.7.0

----------------------------------------------------------------------------------------------------------------

3.-Ejecución de las pruebas del proyecto:

3.1. Python puro
---------------
Ejecuta directamente el script Python sin optimización adicional:

    python3 nombre_del_programa.py

3.2. NumPy
---------
Los scripts optimizados con NumPy se ejecutan igual que Python puro, pero usan estructuras vectorizadas:

    python3 nombre_del_programa_numpy.py

3.3. Numba (JIT)
---------------
Scripts que usan Numba deben importar los decoradores @jit o @njit. Se ejecutan directamente:

    python3 nombre_del_programa_numba.py

Numba compila funciones al vuelo (Just-In-Time) la primera vez que se llaman.

3.4. Multiprocessing
------------------
Scripts que utilizan multiprocesamiento dividen el trabajo en varios núcleos. Ejecución estándar:

    python3 nombre_del_programa_multiprocessing.py

Nota: No se necesita configuración adicional. Ajusta el número de procesos en el propio script si se desea.

3.5. Cython
---------
Pasos para compilar y ejecutar:

1. Crear archivo .pyx (por ejemplo, programa_cython.pyx)
2. Crear setup.py para compilar:
       from setuptools import setup
       from Cython.Build import cythonize
       setup(
           ext_modules = cythonize("programa_cython.pyx")
       )
3. Compilar:
       python3 setup.py build_ext --inplace
4. Ejecutar el módulo compilado:
       python3 rograma_cython.py

Genera un archivo .so (Linux) o .pyd (Windows) que se importa directamente en Python.

3.6. Generación y análisis de traces (comparativas)
-------------------------------------------------
Se utilizó ftrace y el módulo `trace` de Python para analizar llamadas y funciones más invocadas.

- Para generar traces en Python puro:
       python3 -m trace --trace nombre_del_programa.py > trace_output.txt

- Para analizar los traces y extraer llamadas totales y funciones más costosas, se pueden usar scripts adicionales, por ejemplo:
       python3 comparar_traces.py trace_*.txt

Los traces permiten:
    - Contabilizar el número total de llamadas a funciones
    - Identificar funciones más invocadas
    - Analizar la estructura de ejecución y overhead interno
Nota: El número de llamadas no indica directamente el tiempo de ejecución; se combina con mediciones de tiempo para evaluar eficiencia.

------------------------------------------------------------------------------------------------------------------

4.1. Resultados del Poker (resumen de llamadas y funciones más costosas):

Comparativa de llamadas y funciones más invocadas en distintas implementaciones (Poker)

Filtrado de escaleras
Tecnología       | Llamadas totales | Función más costosa
------------------------------------------------------------
Numba            | 1,979,302       | weakref.__getitem__ (152,333)
NumPy            | 629,617         | blocks.external_values (50,020)
Python puro      | 400,703         | Filtrar_escaleras.<genexpr> (60,081)
Cython           | 279,991         | blocks.external_values (50,020)
Multiprocessing  | 90,288          | Filtrar_escaleras_multiprocessing.<genexpr> (60,081)

Jugada ganadora
Tecnología       | Llamadas totales | Función más costosa
------------------------------------------------------------
Numba            | 628,332         | weakref.__getitem__ (26,603)
Multiprocessing  | 591,979         | generic._check (39,211)
Python puro      | 220,527         | generic.__setattr__ (10,078)
Cython           | 220,525         | generic.__setattr__ (10,078)
NumPy            | 11,436          | printing.len (488)

Conteo de cartas
Tecnología       | Llamadas totales | Función más costosa
------------------------------------------------------------
Python puro      | 2,309,525       | generic._instancecheck (155,467)
Numba            | 1,182,791       | generic._instancecheck (70,433)
Multiprocessing  | 1,046,026       | generic._check (77,979)
NumPy            | 891,519         | generic._instancecheck (70,433)
Cython           | 638,876         | generic.__setattr__ (52,598)


4.2. Resultados programas matematicos:

Tiempos Promedio:

| Prueba                     | Python | Cython  | Multiprocessing | Numba   | NumPy  |
|-----------------------------|--------|---------|----------------|---------|--------|
| Suma de cuadrados           | 0.0448 | 0.00004 | 0.1786         | 0.4348  | 0.0081 |
| Caminata aleatoria          | 0.9253 | 0.0231  | 1.6741         | 0.4991  | 0.1719 |
| Quicksort                   | 0.0670 | 0.0293  | 0.6822         | 0.8240  | 0.0008 |
| Multiplicación de matrices  | 0.2956 | 0.0814  | 2.4822         | 0.7103  | 0.0014 |
| Producto cruzado            | 0.0125 | 0.0092  | 3.6442         | 0.5563  | 0.0047 |
| Media general               | 0.2698 | 0.0282 | 1.7323         | 0.6041  | 0.0378 |

Notas sobre optimización:
- Python puro: interpretado, overhead alto en bucles y estructuras dinámicas.
- Cython: compilación a C con tipado opcional, reducción de llamadas y mejora de tiempos.
- Multiprocesamiento: permite paralelizar tareas independientes, introduce llamadas de comunicación.
- Numba: compilación JIT para funciones numéricas, mejora rendimiento CPU-bound.
- NumPy: vectorización y operaciones internas optimizadas en C, reduce overhead de Python.

Comparativa de resultados extraídos de las trazas con ftrace según tecnología utilizada

Tecnología       | Funciones | Tiempo total (ms) | Función más costosa               | Tiempo (us)
-----------------------------------------------------------------------------------------------
Python           | 17640     | 8.30             | get_page_from_freelist            | -
Cython           | 17591     | 8.29             | get_page_from_freelist            | -
NumPy            | 17933     | 6.58             | smaps_account                     | -
Multiprocessing  | 17012     | 9.67             | tlb_finish_mmu                    | -
Numba            | 17576     | 8.27             | get_page_from_freelist            | -
-----------------------------------------------------------------------------------------------
Python           | 17659     | 8.76             | swp_swapcount                     | -
Cython           | 17828     | 8.75             | smaps_account                     | -
NumPy            | 17749     | 10.86            | folio_migrate_flags               | -
Multiprocessing  | 17492     | 9.54             | get_page_from_freelist            | -
Numba            | 17665     | 10.74            | obj_cgroup_uncharge               | -
-----------------------------------------------------------------------------------------------
Python           | 17661     | 11.43            | memtype_lookup                    | -
Cython           | 17587     | 11.19            | memtype_lookup                    | -
NumPy            | 17754     | 12.61            | find_next_iomem_res               | -
Multiprocessing  | 17399     | 10.43            | memtype_lookup                    | -
Numba            | 17915     | 13.91            | find_next_iomem_res               | -
-----------------------------------------------------------------------------------------------
Python           | 17915     | 14.41            | find_next_iomem_res               | -
Cython           | 17962     | 15.12            | find_next_iomem_res               | -
NumPy            | 17745     | 13.56            | find_next_iomem_res               | -
Multiprocessing  | 18122     | 8.52             | find_next_iomem_res               | -
Numba            | 17587     | 11.32            | find_next_iomem_res               | -
-----------------------------------------------------------------------------------------------
Python           | 18000     | 13.43            | find_next_iomem_res               | -
Cython           | 17649     | 11.39            | memtype_lookup                    | -
NumPy            | 17920     | 14.72            | find_next_iomem_res               | -
Multiprocessing  | 17641     | 11.68            | memtype_lookup                    | -
Numba            | 17775     | 13.50            | find_next_iomem_res               | -

------------------------------------------------------------------------------------------------------------------

5.- Estructura del repositorio:

/Proyecto_Optimizacion_Python
│
├─ Poker/
│   ├─ Filtrar_escaleras.py
│   ├─ Jugada_ganadora.py
│   ├─ Cantidad_de_figuras.py
│   └─ data/ (datasets CSV)
│
├─ Matematicas/
│   ├─ sum_of_squares.py
│   ├─ random_walk.py
│   ├─ quicksort.py
│   ├─ matrix_multiplication.py
│   └─ cross_product.py
│
└─ README.txt

---------------------------------------------------------------------------------------------------------------

6.- Autor:
Jueln Terés Lerchundi, Trabajo Fin de Grado, UPV/EHU, jteres002@ikasle.ehu.eus

---------------------------------------------------------------------------------------------------------------

7.- Licencia:
MIT


