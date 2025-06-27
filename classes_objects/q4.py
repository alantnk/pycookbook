# Defining an Interface or Abstract Base Class
#
# You want to define a class that serves as an interface or abstract base class from which
# you can perform type checking and ensure that certain methods are implemented in
# subclasses.
import io
from abc import abstractmethod, ABCMeta


class IStream(metaclass=ABCMeta):

    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


s = SocketStream()
print(s)
print(SocketStream.__mro__)

IStream.register(io.IOBase)
f = open('xfile.bin')
is_ = isinstance(f, IStream)
print(is_)
