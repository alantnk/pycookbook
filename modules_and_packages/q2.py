#  Controlling the Import of Everything

# Define a variable __all__ in your module that explicitly lists the exported names.
from q2_package.index import *

spam()
grok()
# blah() => raise NameError