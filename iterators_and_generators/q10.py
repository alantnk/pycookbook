# Replacing Infinite while Loops with an Iterator
# You have code that uses a while loop to iteratively process data because it involves a function
# or some kind of unusual test condition that doesn’t fall into the usual iteration pattern.

import sys

f = open('logs.txt')
for chunk in iter(lambda: f.read(10), ""):
    # print(chunk)
    n = sys.stdout.write(f"{chunk}XXX")
