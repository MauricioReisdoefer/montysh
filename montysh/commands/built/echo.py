from pathlib import Path
from montysh import BaseCommand

class EchoCommand(BaseCommand):
    def __init__(self):
        super().__init__("echo", self.run)

    def run(self, *args):
        return " ".join(args)