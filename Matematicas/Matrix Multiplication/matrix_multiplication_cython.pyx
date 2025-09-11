# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

def matrix_multiplication_cython(list A, list B):
    cdef int i, j, k
    cdef int rows = len(A)
    cdef int inner = len(A[0])
    cdef int cols = len(B[0])

    # Crear matriz resultado con ceros
    result = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i][j] += A[i][k] * B[k][j]

    return result
