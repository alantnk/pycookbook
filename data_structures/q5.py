#  Calculating with Dictionaries

# You want to perform various calculations (e.g., minimum value, maximum value, sort‐
# ing, etc.) on a dictionary of data.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

multi_array = zip(prices.values(), prices.keys())

print(min(multi_array))

