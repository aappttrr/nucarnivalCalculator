from PyQt5.QtGui import QIntValidator


class IntValidator(QIntValidator):
    def __init__(self, _bottom: int, _top: int):
        super(IntValidator, self).__init__()
        self.topValue = _top
        self.bottomValue = _bottom

    def validate(self, a0: str, a1: int):
        try:
            if self.bottomValue <= int(a0) <= self.topValue:
                return 2, a0, a1
            else:
                return 0, a0, a1
        except:
            return 0, a0, a1

    def fixup(self, a0: str):
        return str(self.bottomValue)

    def top(self):
        return self.topValue

    def bottom(self):
        return self.bottomValue
