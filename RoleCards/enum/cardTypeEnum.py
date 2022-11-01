import enum


class CardType(enum.Enum):
    Light = '光', '克制暗属性，被暗属性克制'
    Dark = '暗', '克制光属性，被光属性克制'
    Fire = '火', '克制木属性，被水属性克制'
    Water = '水', '克制火属性，被木属性克制'
    Wood = '木', '克制水属性，被火属性克制'

    def __init__(self, typeName, des):
        self._typeName = typeName
        self._des = des

    @property
    def typeName(self):
        return self._typeName

    @property
    def des(self):
        return self._des

    def isRestrained(self, para):
        if self == CardType.Light and para == CardType.Dark:
            return True

        if self == CardType.Dark and para == CardType.Light:
            return True

        if self == CardType.Fire and para == CardType.Wood:
            return True

        if self == CardType.Water and para == CardType.Fire:
            return True

        if self == CardType.Wood and para == CardType.Water:
            return True

        return False
