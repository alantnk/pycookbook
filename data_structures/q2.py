# Keeping the Last N Items

# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing.

from collections import deque


def search(lines, pattern, history=4):
    previous_lines = deque(maxlen=history)
    for l in lines:
        if pattern in l:
            yield l, previous_lines
        previous_lines.append(l)


# Keeping a limited history is a perfect use for a collections.deque. For example, the
# code above performs a simple text match on a sequence of lines and yields the
# matching line along with the previous N lines of context when found

# Example use on a file
if __name__ == '__main__':
    with open('xfile.txt') as f:
        for line, prevlines in search(f, 'python'):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
