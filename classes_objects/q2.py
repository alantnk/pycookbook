# Creating a New Kind of Class or Instance Attribute
#
# You want to create a new kind of instance attribute type with some extra functionality,
# such as type checking.

# Descriptor attribute for an integer type-checked attribute
class Integer:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):

        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):

        del instance.__dict__[self.name]


# A descriptor is a class that implements the three core attribute access operations (get,
# set, and delete) in the form of __get__(), __set__(), and __delete__() special meth‐
# ods. These methods work by receiving an instance as input. The underlying dictionary
# of the instance is then manipulated as appropriate.
# To use a descriptor, instances of the descriptor are placed into a class definition as class
# variables. For example:

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 3)
print(p.x)
print(p.y)
p.x = 8
print(p.x)

# p.y = 2.3 => Raise an exception
