import shlex
from montysh.commands import (
    BaseCommand, RmCommand, EchoCommand, CreateCommand, TimeCommand,
    TouchCommand, IfCommand, ElseCommand, LsCommand, ExitCommand,
    HereCommand, InputCommand
)

class Interpreter:
    def __init__(self):
        # Registred commands
        self.commands: dict[str, BaseCommand] = {}
        self._register_builtins()

    def _register_builtins(self):
        """Registers all built-in commands"""
        for cmd_class in [
            RmCommand, EchoCommand, CreateCommand, TimeCommand, TouchCommand,
            IfCommand, ElseCommand, LsCommand, ExitCommand, HereCommand, InputCommand
        ]:
            self.register(cmd_class())

    def register(self, command: BaseCommand):
        """Register a new command line in the Interpreter"""
        self.commands[command.name] = command

    def run_line(self, line: str):
        """Interpret a single line of code"""
        # Usa shlex para preservar strings entre aspas
        parts = shlex.split(line)
        if not parts:
            return None

        name, *args = parts
        cmd = self.commands.get(name)

        if not cmd:
            raise ValueError(f"Command not found: {name}")

        return cmd(*args)
