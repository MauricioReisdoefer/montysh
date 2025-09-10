from typing import Callable

class BaseCommand():
    """Base class for commands in the interpreter"""
    
    def __init__(self, symbol : str, func : Callable):
        if isinstance(symbol, str):
            raise ValueError("")
        if not callable(func):
            raise ValueError("")
        
        self.symbol : str = symbol
        self.func : Callable = func
    
    def call(self, *args, **kwargs):
        """Execute the command with arguments and keyword arguments."""
        return self.func(*args, **kwargs)