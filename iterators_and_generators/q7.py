# Iterating Over Multiple Sequences Simultaneously

# You want to iterate over the items contained in more than one sequence at a time.


# To iterate over more than one sequence simultaneously, use the zip() function.

from itertools import zip_longest

xlist = ["x1", "x2", "x3"]
ylist = ["y1", "y2", "y3", "y4"]

for x, y in zip(xlist, ylist):
    print(x, y)

print("-" * 20)
for x, y in zip_longest(xlist, ylist):
    print(x, y)

# Using zip(), you can pair the values together to make a dictionary like this:
print("-" * 20)
my_dict = dict(zip(xlist, ylist))
print(my_dict)
