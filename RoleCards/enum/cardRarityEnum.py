import enum


class CardRarity(enum.Enum):
    N = 'N', 1
    R = 'R', 2
    SR = 'SR', 3
    SSR = 'SSR', 4

    def __init__(self, rarityName, index):
        self._rarityName = rarityName
        self._rarityIndex = index

    @property
    def rarityName(self):
        return self._rarityName

    @property
    def rarityIndex(self):
        return self._rarityIndex

    def __lt__(self, other):
        return self.rarityIndex > other.rarityIndex