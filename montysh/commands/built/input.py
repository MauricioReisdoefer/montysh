from montysh import BaseCommand

class InputCommand(BaseCommand):
    def __init__(self):
        super().__init__("input", self.run)

    def run(self, prompt="> "):
        return input(prompt)