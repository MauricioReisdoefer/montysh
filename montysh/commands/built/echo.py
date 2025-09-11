from pathlib import Path
from ..base_command import BaseCommand

class EchoCommand(BaseCommand):
    def __init__(self):
        super().__init__("echo", self.run)

    def run(self, *args):
        return " ".join(args)