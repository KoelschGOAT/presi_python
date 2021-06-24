from timer import timer
import timeit
from fib_dec import memory

@memory
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


t1 = timeit.Timer("fib(35)", "from __main__ import fib")
print(t1.timeit(1))
print(fib(35))