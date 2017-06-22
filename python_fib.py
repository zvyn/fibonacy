"""Python implementation of fibonnaci."""

from functools import lru_cache

@lru_cache(None)
def fib(n):
    """Return n_th fibonnaci number."""
    if number < 3:
        return 1
    for i in range(number - 3):  # Needed to work around MaxRecursionDepth
      fib(i)
    return fib(number - 2) + fib(number - 1)
