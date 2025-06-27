# Finding Commonalities in Two Dictionaries

# You have two dictionaries and want to find out what they might have in common (same
# keys, same values, etc.).

spam = {
    'x': 1,
    'y': 2,
    'z': 3
}

eggs = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
print(spam.keys() & eggs.keys())

# Find keys in a that are not in eggs
print(spam.keys() - eggs.keys())

# Find (key,value) pairs in common
print(spam.items() & eggs.items())

# Make a new dictionary with certain keys removed
c = {key: spam[key] for key in spam.keys() - {'z', 'w'}}
print(c)
