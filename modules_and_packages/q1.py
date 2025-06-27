# Making a Hierarchical Package of Modules


# Making a package structure is simple. Just organize your code as you wish on the
# file-system and make sure that every directory defines an __init__.py file.
from q1_package.primitive import fill, line
from q1_package.format.png import png_

print(fill.fill_)
print(line.line_)
print(png_)