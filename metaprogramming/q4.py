# Writing Decorators That Add Arguments to Wrapped Functions

from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print(f"Calling {func.__name__} func . . .")
        return func(*args, **kwargs)

    return wrapper

@optional_debug
def spam(x, y):
    pass


spam(2, 3)
spam(2, 3, debug=True)

"""
Adding arguments to the signature of wrapped functions is not the most common example
of using decorators. However, it might be a useful technique in avoiding certain
kinds of code replication patterns.

The implementation of this recipe relies on the fact that keyword-only arguments are
easy to add to functions that also accept *args and **kwargs parameters. By using a
keyword-only argument, it gets singled out as a special case and removed from subsequent
calls that only use the remaining positional and keyword arguments.
"""
