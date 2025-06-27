# Creating Managed Attributes
#
# You want to add extra processing (e.g., type checking or validation) to the getting or
# setting of an instance attribute.

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Pedro')  # Calls the getter
a.first_name = 42 # Calls the setter (TyperError)