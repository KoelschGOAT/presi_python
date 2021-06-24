from timer import timer


@timer
def forloop():
    a = 0
    for i in range(1, 100001):
        a += i
    return a


forloop()


@timer
def whileloop():
    c = 0
    a = 0
    while c < 100001:
        a += c
        c += 1
    return a


whileloop()
