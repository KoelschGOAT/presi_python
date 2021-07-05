import time
def timer(func):
    def time_dec(*args):
        before = time.time()
        func(*args)
        print(f"Function took {round(time.time() - before, 3)} seconds")

    return time_dec

@timer
def while_loop():
    counter = 0
    a = 0
    while counter < 100_000:
        a+=counter
        counter += 1
@timer
def for_loop():
    a = 0
    for i in range(100_000):
        a+=i
while_loop()
for_loop()