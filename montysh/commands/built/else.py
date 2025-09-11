from montysh import BaseCommand

class ElseCommand(BaseCommand):
    def __init__(self):
        super().__init__("else", self.run)

    def run(self, *args):
        return True