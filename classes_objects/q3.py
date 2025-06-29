# Using Lazily Computed Properties
#
# You’d like to define a read-only attribute as a property that only gets computed on access.
# However, once accessed, you’d like the value to be cached and not recomputed on each
# access.

import math


class lazyproperty:

    def __init__(self, func):

        self.func = func

    def __get__(self, instance, cls):

        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(4.0)
print(c.area)
print(c.perimeter)

print(c.area)
print(c.area)

print(c.perimeter)
print(c.perimeter)

# 'Computing area' and 'Computing perimeter' are printed once after the computed value
# are cached for better performance