Playing around with cython and cProfile.

Example usage:

    $ N=100000 ./profile_time.py
    python fib(100000) took 1626.805989s
    cython fib(100000) took    0.043696s
    cython fib was 37230 times faster
