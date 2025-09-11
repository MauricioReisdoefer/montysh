from pathlib import Path
from montysh import BaseCommand

class HereCommand(BaseCommand):
    def __init__(self):
        super().__init__("here", self.run)

    def run(self, *args):
        return Path(".").resolve()
