# cross_product_cython.pyx

def cross_product_cython(list vectors_a, list vectors_b):
    cdef int i
    cdef int n = len(vectors_a)
    cdef double ax, ay, az, bx, by, bz
    cdef list result = []

    for i in range(n):
        ax, ay, az = vectors_a[i]
        bx, by, bz = vectors_b[i]
        result.append([
            ay * bz - az * by,
            az * bx - ax * bz,
            ax * by - ay * bx
        ])

    return result
