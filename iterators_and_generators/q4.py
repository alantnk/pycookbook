# Defining Generator Functions with Extra State
# You would like to define a generator function, but it involves extra state that you would
# like to expose to the user somehow.
from collections import deque


class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for line_id, line in enumerate(self.lines, 1):
            self.history.append((line_id, line))
            yield line

    def clear(self):
        self.history.clear()

# To use this class, you would treat it like a normal generator function. However, since it
# creates an instance, you can access internal attributes, such as the history attribute or
# the clear() method. For example:
with open('xfile.txt') as f:
    lines = LineHistory(f)
    for line in lines:
        if 'python' in line:
            for line_id, hline in lines.history:
                print(f"{line_id}:{hline}")

