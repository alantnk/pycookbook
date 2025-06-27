# Skipping the First Part of an Iterable

# You want to iterate over items in an iterable, but the first few items aren’t of interest and
# you just want to discard them.


# The itertools module has a few functions that can be used to address this task. The
# first is the itertools.dropwhile() function. To use it, you supply a function and an
# iterable. The returned iterator discards the first items in the sequence as long as the
# supplied function returns True. Afterward, the entirety of the sequence is produced.
# To illustrate, suppose you are reading a file that starts with a series of comment lines.
# For example:

from itertools import dropwhile

with open('xfile.txt') as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line)
