#!/usr/bin/env python3

"""Provide helper to return the total time needed for a function call.

If run as script it compares Python and Cython implementations of a fibonnaci
function (specify the fibonnaci number to calculate via the `N` env variable,
default: 5000).
"""

import cProfile


def time(func, *args, **kwargs):
    pr = cProfile.Profile()
    pr.enable()
    func(*args, **kwargs)
    pr.disable()
    stats = pr.getstats()
    return max([stat.totaltime for stat in stats])


if __name__ == '__main__':
    import pyximport
    pyximport.install()  # NOQA

    import python_fib
    import cython_fib

    from os import getenv
    N = int(getenv('N', 5000))

    python_fib_time = time(python_fib.fib, N)
    print("python fib({}) took {:11f}s".format(N, python_fib_time))
    cython_fib_time = time(cython_fib.fib, N)
    print("cython fib({n}) took {cython_fib_time:11f}s\n"
          "cython fib was {factor:.0f} times faster".format(
              n=N, cython_fib_time=cython_fib_time,
              factor=python_fib_time / cython_fib_time,
              percent=cython_fib_time / python_fib_time))
