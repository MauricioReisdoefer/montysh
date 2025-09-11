import time as _time
from montysh import BaseCommand

class TimeCommand(BaseCommand):
    def __init__(self):
        super().__init__("time", self.run)

    def run(self, *args):
        return _time.strftime("%Y-%m-%d %H:%M:%S", _time.localtime())
