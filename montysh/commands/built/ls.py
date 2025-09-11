from pathlib import Path
from ..base_command import BaseCommand

class LsCommand(BaseCommand):
    def __init__(self):
        super().__init__("ls", self.run)

    def run(self, *args):
        path = Path(args[0]) if args else Path(".")
        if not path.exists() or not path.is_dir():
            return []
        return [p.name for p in path.iterdir()]