# Putting a Wrapper Around a Function

# If you ever need to wrap a function with extra code, define a decorator function. For example:

import time
from functools import wraps


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n: int):
    """
    Counts down
    """
    while n > 0:
        n -= 1


countdown(9999)
countdown(999999)

# Also @wraps decorator preserves metadata
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
