from montysh import BaseCommand
from pathlib import Path

class CreateCommand(BaseCommand):
    def __init__(self):
        super().__init__("create", self.run)

    def run(self, filename: str, *contents):
        p = Path(filename)
        text = " ".join(contents)
        p.write_text(text)
        return f"Arquivo '{filename}' criado com conteúdo."