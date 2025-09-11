# quicksort_cython.pyx

cpdef list quicksort_cython(list arr):
    cdef int n = len(arr)
    if n <= 1:
        return arr

    cdef int pivot = arr[n // 2]
    cdef list left = [x for x in arr if x < pivot]
    cdef list middle = [x for x in arr if x == pivot]
    cdef list right = [x for x in arr if x > pivot]

    return quicksort_cython(left) + middle + quicksort_cython(right)

