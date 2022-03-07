from functools import wraps
import inspect

class NiaInterface:
    def __init__(self):
        pass

    def run(self):
        pass

    def get_best(self):
        pass
    
    def get_iteration_info():
        pass

    def run_iteration_function(self):
        data = self.get_iteration_info()
        if self.iteration_function:
            self.iteration_function(data)

    def finilize(self, success:bool):
        data = self.get_best()
        if success:
            self.message = 'quit criteria reached best answer is: ' + str(data['result']) \
                + ' and best fitness is: ' + str(data['fitness']) + ' iteration : ' + str(self.iteration)
        else:
            self.message = 'max iteration reached best answer so far: ' + str(data['result']) \
                + ' with best fitness: ' + str(data['fitness']) + ' iteration : ' + str(self.iteration)
        
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