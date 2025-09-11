from montysh import BaseCommand

class ExitCommand(BaseCommand):
    def __init__(self):
        super().__init__("exit", self.run)

    def run(self, *args):
        print("Saindo do Monty-SH...")
        raise SystemExit()