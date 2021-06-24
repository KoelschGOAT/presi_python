import time


def timer(func):
    def time_dec(*args):
        before = time.time()
        func(*args)
        print(f"Function took {round(time.time() - before, 3)} seconds")

    return time_dec
