from typing import Callable

class BaseCommand:
    """Base class for commands in .psy files"""
    def __init__(self, name: str, func: Callable):
        if not isinstance(name, str):
            raise TypeError("name deve ser uma string")
        if not callable(func):
            raise TypeError("func deve ser chamável (callable)")
        
        self.name = name
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def call(self, *args, **kwargs):
        """Calls the function stored in the instance"""
        return self.func(*args, **kwargs)