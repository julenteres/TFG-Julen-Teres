# sum_of_squares_cython.pyx
def sum_of_squares_cython(int n):
    cdef int i, result = 0
    for i in range(n):
        result += i ** 2
    return result

