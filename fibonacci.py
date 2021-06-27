from timer import timer
import timeit
from fib_dec import memory

@memory
def fib(n):
    if n < 2:
        return n
    else:
        val = fib(n-1) + fib(n-2)
        print(val)
    return val

def fibb(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


t1 = timeit.Timer("fib(35)", "from __main__ import fib")
print(f"Exec_Time: {t1.timeit(1)}")
print(fib(35))


t2 = timeit.Timer("fibb(35)", "from __main__ import fibb")
print(t2.timeit(1))
print(fibb(35))