# Creating New Iteration Patterns with Generators

# You want to implement a custom iteration pattern that’s different than the usual built-
# in functions (e.g., range(), reversed(), etc.).


# If you want to implement a new kind of iteration pattern, define it using a generator
# function. Here’s a generator that produces a range of floating-point numbers:
def f_range(start, stop, increment=0.1):
    x = start
    while x < stop:
        yield x
        x += increment


# To use such a function, you iterate over it using a for loop or use it with some other
# function that consumes an iterable (e.g., sum(), list(), etc.). For example:
if __name__ == "__main__":
    for n in f_range(0.2, 1.5):
        print(n)

    print(
        sum(f_range(0.2, 1.5))
    )
