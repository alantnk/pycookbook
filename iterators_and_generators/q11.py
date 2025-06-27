# Flattening a Nested Sequence
# You have a nested sequence that you want to flatten into a single list of values.



from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6], 7], 8]
flat_items = list(flatten(items))
print(flat_items)

# In the code, the isinstance(x, Iterable) simply checks to see if an item is iterable.
# If so, yield from is used to emit all of its values as a kind of subroutine. The end result
# is a single sequence of output with no nesting.

# The extra argument ignore_types and the check for not isinstance(x, ignore_types) is there
# to prevent strings and bytes from being interpreted as iterables and expanded
# as individual characters.