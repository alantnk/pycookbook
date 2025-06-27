# Iterating on Items in Separate Containers

# You need to perform the same operation on many objects, but the objects are contained
# in different containers, and you’d like to avoid nested loops without losing the readability
# of your code.

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

# Inefficent
for x in a + b:
    ...

# Better
for x in chain(a, b):
    print(x)

# In the first case, the operation a + b creates an entirely new sequence and additionally
# requires a and b to be of the same type. chain() performs no such operation, so it’s far
# more efficient with memory if the input sequences are large and it can be easily applied
# when the iterables in question are of different types.
