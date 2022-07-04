import time


def clock(func):
    def clocked(*args):                          # Takes multiple arguments
        t0 = time.perf_counter()
        result = func(*args)                     # func is a free variable
        elapsed = time.perf_counter() - t0       # timer created with t0
        name = func.__name__                     # function with arguments
        arg_str = ', '.join(repr(arg) for arg in args)  # format args in *args
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
