from pathlib import Path
from montysh import BaseCommand

class TouchCommand(BaseCommand):
    def __init__(self):
        super().__init__("touch", self.run)

    def run(self, *args):
        created = []
        for filename in args:
            Path(filename).touch(exist_ok=True)
            created.append(filename)
        return f"Criou arquivos {', '.join(created)}"