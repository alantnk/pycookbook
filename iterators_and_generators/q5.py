# Taking a Slice of an Iterator

# You want to take a slice of data produced by an iterator, but the normal slicing operator
# doesn’t work.
import itertools
def count(n):
    while True:
        yield n
        n+= 1


counter = count(0)
# counter[10:20] => TypeError: 'generator' object is not subscriptable

# The itertools.islice() function is perfectly suited for taking slices of iterators and
# generators. For example:
for c in itertools.islice(counter,10,20):
    print(c)

# !! It’s important to emphasize that islice() will consume data on the supplied iterator.
# Since iterators can’t be rewound, that is something to consider. If it’s important to go
# back, you should probably just turn the data into a list first.