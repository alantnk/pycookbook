# Using a Metaclass to Control Instance Creation

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

Spam.grok(2)
# a = Spam() => raises TypeError

print(Spam.__mro__)