from montysh.commands import BaseCommand
from .interpreter import Interpreter

class PsyFileReader:
    """Reads a .psy file"""
    def __init__(self, interpreter: Interpreter):
        self.interpreter = interpreter

    def run_file(self, filename: str):
        """Opens a .psy file and run each line"""
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    result = self.interpreter.run_line(line)
                    if result is not None:
                        print(f"{result}")
                except Exception as e:
                    print(f"Erro na linha {line_number}: {e}")
