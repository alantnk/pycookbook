# Enforcing Type Checking on a Function Using a Decorator

from functools import wraps
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # Disable type checking in optimized mode
        if not __debug__:
            return func

        # Map func argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wraper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across suplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(f'Argument {name} must be {bound_types[name]}')
            return func(*args, **kwargs)

        return wraper

    return decorate

@typeassert(int, z=int)
def spam(x, y, z):
    pass

spam(1, "b", 3)
# spam(1, 2, "b") => raises TypeError


"""
A tricky part of writing this decorator is that it involves examining and working
with the argument signature of the function being wrapped. Your tool of choice here
should be the inspect.signature() function. Simply stated, it allows you to extract
signature information from a callable. For example:

>>> from inspect import signature
>>> def spam(x, y, z=42):
...
 pass
...
>>> sig = signature(spam)
>>> print(sig)
(x, y, z=42)
>>> sig.parameters
mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>), ('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
>>> sig.parameters['z'].name
'z'
>>> sig.parameters['z'].default
42
>>> sig.parameters['z'].kind
<_ParameterKind: 'POSITIONAL_OR_KEYWORD'>
>>>

"""