# Delegating Iteration

# You have built a custom container object that internally holds a list, tuple, or some other
# iterable. You would like to make iteration work with your new container.



# Typically, all you need to do is define an __iter__() method that delegates iteration to
# the internally held container. For example:
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return f'Node {self._value}'

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

