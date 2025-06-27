# Iterating in Reverse

# You want to iterate in reverse over a sequence.

# arr = ["a", "b", "c", "d", "e"]
# for x in reversed(arr):
#     print(x)


# Reversed iteration only works if the object in question has a size that can be determined
# or if the object implements a __reversed__() special method. If neither of these can
# be satisfied, you’ll have to convert the object into a list first.


# Reversed iteration can be customized on user-defined classes if they implement
# the __reversed__() method. For example:

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for c in reversed(Countdown(5)):
    print(c)