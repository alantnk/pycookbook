# Defining a Decorator That Takes Arguments
import logging
from functools import wraps


def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''

    def decorate(func):
        # print(name)
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# Example use
@logged(logging.WARNING, message="add_op")
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'spam_log', 'spam_op')
def spam():
    pass


add(3, 2)
spam()
