from pathlib import Path
from montysh import BaseCommand

class RmCommand(BaseCommand):
    def __init__(self):
        super().__init__("rm", self.run)

    def run(self, *args):
        removed = []
        for filename in args:
            p = Path(filename)
            if p.exists():
                p.unlink()
                removed.append(filename)
        return f"Arquivos removidos: {', '.join(removed)}"