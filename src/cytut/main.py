import numpy as np
import pyximport

pyximport.install(setup_args={"include_dirs": np.get_include()})
from cytut import lib  # noqa


def mmult(x: np.ndarray, y: np.ndarray):
    N = x.shape[0]
    M = x.shape[1]
    P = y.shape[1]
    res = np.zeros([N, P], dtype=np.float32)
    for n in range(N):
        for p in range(P):
            value = 0
            for m in range(M):
                value += x[n, m]*y[m, p]
            res[n, p] = value
    return res


def main():
    print(lib.primes(10000))
    N, M, P = 1_000, 1_000, 1_000
    x = np.random.randn(N, M).astype(np.float32)
    y = np.random.randn(M, P).astype(np.float32)
    z = lib.mmult(x, y)
    print(z.shape)


if __name__ == "__main__":
    main()
