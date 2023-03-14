#cython: language_level=3
from math import sqrt
import cython

import numpy as np
cimport numpy as np
np.import_array()


DTYPE = np.float32
ctypedef np.float32_t DTYPE_t


cpdef isprime(long n):
    if n < 2:
        return False
    if n in {2, 3, 5, 7, 11}:
        return True
    cdef long upper 
    upper = long(sqrt(n))
    cdef long i
    i = 2
    while i <= upper:
        if n % i == 0:
            return False
        i += 1
    return True


def primes(long num_primes):
    cdef long n, num_primes_so_far
    cdef long[100000] primes
    num_primes_so_far = 0
    n = 2
    while num_primes_so_far < num_primes:
        if isprime(n):
            primes[num_primes_so_far]  = n
            num_primes_so_far += 1
        n += 1

    res = [p for p in primes[:num_primes]]
    return res


@cython.boundscheck(False)
@cython.wraparound(False)
def mmult(np.ndarray[DTYPE_t, ndim=2] x, np.ndarray[DTYPE_t, ndim=2] y):
    cdef int N = x.shape[0]
    cdef int M = x.shape[1]
    cdef int P = y.shape[1]
    cdef np.ndarray[DTYPE_t, ndim=2] res = np.zeros([N, P], dtype=DTYPE)
    cdef int n, m, p
    
    cdef DTYPE_t value
    for n in range(N):
        for p in range(P):
            value = 0
            for m in range(M):
                value += x[n, m]*y[m, p]
            res[n, p] = value
    return res
