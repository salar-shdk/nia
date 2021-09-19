from functools import wraps
import inspect

class Selection():
    def __init__(self):
        pass

    def select(self, population, fitness):
        pass

    @classmethod
    def initializer(self, func):
        """
        Automatically assigns the parameters.
        """
        names, varargs, keywords, defaults = inspect.getargspec(func)

        @wraps(func)
        def wrapper(self, *args, **kargs):
            for name, arg in list(zip(names[1:], args)) + list(kargs.items()):
                setattr(self, name, arg)

            if defaults and names:
                for name, default in zip(reversed(names), reversed(defaults)):
                    if not hasattr(self, name):
                        setattr(self, name, default)

            func(self, *args, **kargs)

        return wrapper