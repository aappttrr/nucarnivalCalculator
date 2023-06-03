import enum


class CardRole(enum.Enum):
    Aster = '艾斯特', 1
    Morvay = '墨菲', 2
    Yakumo = '八云', 3
    Edmond = '艾德蒙特', 4
    Olivine = '奥利文', 5
    Quincy = '昆西', 6
    Kuya = '玖夜', 7
    Garu = '可尔', 8
    Blade = '布儡', 9
    Dante = '啖天', 10
    Rei = '敛', 11
    Eiden = '伊得', 20

    def __init__(self, roleName, index):
        self._roleName = roleName
        self._roleIndex = index

    @property
    def roleName(self):
        return self._roleName

    @property
    def value(self):
        return self._roleName

    @property
    def roleIndex(self):
        return self._roleIndex

    def __lt__(self, other):
        return self.roleIndex < other.roleIndex
