"""Python implementation of fibonnaci."""

from functools import lru_cache


@lru_cache(None)
def fib(n):
    """Return n_th fibonnaci number."""
    if n < 3:
        return 1
    for i in range(n - 3):  # Needed to work around MaxRecursionDepth
        fib(i)
    return fib(n - 2) + fib(n - 1)
