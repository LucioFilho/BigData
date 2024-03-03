# The code snippet defines a simple framework for creating abstract base classes (ABCs) in Python, 
# similar to the abc module in the standard library but implemented manually.

   
# abstractmethod Decorator:
# This decorator marks methods as abstract by adding an `__isabstract__` attribute to them.
# When applied to a method, it signals that the method is intended to be overridden by subclasses, 
# and does not provide any implementation.
def abstractmethod(f):
    f.__isabstract__ = True
    return f


# abstractmethods Function:
# This function collects all abstract methods from a class and its base classes.
# It traverses the method resolution order (MRO) of a class looking for methods marked as abstract 
# using `abstractmethod`.
# It accumulates the names of these methods in the `abstract` list, which is then returned.
def abstractmethods(cls):
    seen = set()
    abstract = []
    while isinstance(cls, ABCMeta):
        for key, val in vars(cls).items():
            if key in seen:
                continue
            seen.add(key)
            if getattr(val, '__isabstract__', False):
                abstract.append(key)
        # object is not ABCMeta so mro will have at least 2 entries
        cls = cls.__mro__[1]
    return abstract


# ABCMeta Metaclass:
# A custom metaclass that uses the `abstractmethods` function to check if a class has implemented 
# all of its abstract methods when an attempt is made to instantiate it.
# If there are unimplemented abstract methods, it raises a `TypeError`, preventing instantiation.
class ABCMeta(type):
    def __call__(abccls, *args, **kwargs): # called when you A()
        print("call", abccls, args, kwargs)
        abstract = abstractmethods(abccls)
        if abstract:
            raise TypeError('no implementation for: ' + ', '.join(abstract))
        return super().__call__(*args, **kwargs)


# ABC Class:
# This is a base class for creating abstract classes.
# It uses `ABCMeta` as its metaclass, which means any subclass of `ABC` will be subject to the 
# abstract method checks when instantiated.
class ABC(metaclass=ABCMeta):
    pass


# `A` Class:
# A subclass of `ABC` that defines two abstract methods: `f` and `g`.
# Since it inherits from `ABC`, it cannot be instantiated until these methods are implemented.
class A(ABC):
    def __init__(self, *args, **kwargs):
        print("init", self, args, kwargs)

    @abstractmethod
    def f(self):
        pass

    @abstractmethod
    def g(self):
        pass


# `B` Class:
# A subclass of `A` that provides concrete implementations of the abstract methods `f` and `g`.
# Since all abstract methods are implemented, `B` can be instantiated without error.
class B(A):
    def f(self):
        pass

    def g(self):
        pass


# `main` Function:
# The commented out line `A()` would raise a `TypeError` if uncommented because `A` has unimplemented 
# abstract methods.
# It then creates an instance of `B`, which is allowed because `B` has implemented all of its abstract methods.
# The function prints the types of the instance `b` and the class `B` for demonstration.
def main():
    # A()  # Error: abstract f,g
    b = B()
    print(f'{type(b)=}')
    print(f'{type(B)=}')


# `if __name__ == '__main__':` Block:
# This is the entry point of the program. If the script is run directly, it calls the `main` function.
if __name__ == '__main__':
    main()


# In summary, this code is a custom implementation of an abstract base class framework in Python. 
# It defines how to declare abstract methods, checks that they are implemented in non-abstract subclasses, 
# and prevents instantiation of classes that don't fulfill these abstract method requirements.
    

#Example:
def abstractmethod(f):
    f.__isabstract__ = True
    return f

class ABCMeta(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        abstract_methods = [name for name, value in vars(cls).items() if getattr(value, '__isabstract__', False)]
        if abstract_methods:
            raise TypeError(f"Can't instantiate abstract class {cls.__name__} with abstract methods: {', '.join(abstract_methods)}")
        return obj

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def emitir_som(self):
        return "O leão rugiu"

    def mover(self):
        return "O leão está andando"

class Cobra(Animal):
    def emitir_som(self):
        return "A cobra sibilou"

    def mover(self):
        return "A cobra está rastejando"

def main():
    leao = Leao()
    print(leao.emitir_som())
    print(leao.mover())

    cobra = Cobra()
    print(cobra.emitir_som())
    print(cobra.mover())

if __name__ == '__main__':
    main()
