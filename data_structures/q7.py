# Removing Duplicates from a Sequence while Maintaining Order

# You want to eliminate the duplicate values in a sequence, but preserve the order of the
# remaining items


# If the values in the sequence are hashable, the problem can be easily solved using a set
# and a generator. For example:
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


eggs = [1, 5, 2, 1, 9, 1, 5, 10]

result = list(dedupe(eggs))

print(result)
