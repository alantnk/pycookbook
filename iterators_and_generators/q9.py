# Iterating in Sorted Order Over Merged Sorted Iterables

# You have a collection of sorted sequences and you want to iterate over a sorted sequence
# of them all merged together.

# The heapq.merge() function does exactly what you want. For example:

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# !!It’s important to emphasize that heapq.merge() requires that all of the input sequences
# already be sorted. In particular, it does not first read all of the data into a heap or do any
# preliminary sorting. Nor does it perform any kind of validation of the inputs to check
# if they meet the ordering requirements. Instead, it simply examines the set of items from
# the front of each input sequence and emits the smallest one found. A new item from
# the chosen sequence is then read, and the process repeats itself until all input sequences
# have been fully consumed.