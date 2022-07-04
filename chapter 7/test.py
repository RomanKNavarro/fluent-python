import time


def num(func):
    def quant(*args):
        result = func(*args)
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('%s(%s) -> %r' % (name, arg_str, result))
        return result
    return quant


# @num
# def snooze(seconds):
#     time.sleep(seconds)


@num
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


factorial(6)
