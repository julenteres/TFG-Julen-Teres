# random_walk_cython.pyx

from libc.stdlib cimport rand, srand
from libc.time cimport time
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def random_walk_cython(int n):
    cdef int i
    cdef int x = 0
    cdef int y = 0
    cdef int dx, dy

    srand(<unsigned int> time(NULL))

    for i in range(n):
        dx = 1 if rand() % 2 == 0 else -1
        dy = 1 if rand() % 2 == 0 else -1
        x += dx
        y += dy

    return x, y
