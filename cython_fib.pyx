"""Cython implementation of fibonnaci."""

# Using _cache dict instead of functools.lru_cache allows using a cdef function.
_cache = dict()

cdef int _fib(int number):
    if number in _cache:  # 'not in' would  require defining result in each run
        return _cache[number]
    if number < 3:
        return 1
    cdef int result = _fib(number - 2) + _fib(number - 1)
    _cache[number] = result
    return result

def fib(n):
    """Return n_th fibonnaci number."""
    return _fib(n)
