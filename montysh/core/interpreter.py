from montysh.commands import BaseCommand

class Interpreter:
    def __init__(self):
        # Registred commands
        self.commands: dict[str, BaseCommand] = {}

    def register(self, command: BaseCommand):
        """Register a new command line in the Interpreter"""
        self.commands[command.name] = command

    def run_line(self, line: str):
        """Interpret a single line of code"""
        parts = line.strip().split()
        if not parts:
            return None
        
        name, *args = parts
        cmd = self.commands.get(name)

        if not cmd:
            raise ValueError(f"Comando não encontrado: {name}")

        return cmd(*args)
