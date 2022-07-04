# colck_demo.py
import time
from simpleDeco import clock


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
    # factorial(1) is 1, so return 1. Else, return
    # multiple number of times with *. This function
    # holds multiple arguments.


factorial(6)
if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
