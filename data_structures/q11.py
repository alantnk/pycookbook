# Mapping Names to Sequence Elements

# You have code that accesses list or tuple elements by position, but this makes the code
# somewhat difficult to read at times. You’d also like to be less dependent on position in
# the structure, by accessing the elements by name.

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['username', 'email'])

sub = Subscriber('john34','john@doe.com')

print(sub)
print(sub.username)
print(sub.email)

print(len(sub))

# collections.namedtuple() provides these benefits, while adding minimal overhead
# over using a normal tuple object. collections.namedtuple() is actually a factory
# method that returns a subclass of the standard Python tuple type. You feed it a type
# name, and the fields it should have, and it returns a class that you can instantiate, passing
# in values for the fields you’ve defined, and so on.