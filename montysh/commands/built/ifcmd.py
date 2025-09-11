from ..base_command import BaseCommand

class IfCommand(BaseCommand):
    def __init__(self):
        super().__init__("if", self.run)

    def run(self, condition: str):
        try:
            return bool(eval(condition))
        except Exception:
            raise ValueError(f"Condição inválida: {condition}")