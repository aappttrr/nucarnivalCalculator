import enum


class CardOccupation(enum.Enum):
    Healer = '治愈', '善于治疗队友的角色类型'
    Support = '辅助', '善于增强队友的角色类型'
    Striker = '攻击', '善于制造伤害的角色类型'
    Guardian = '守护', '善于守护队友的角色类型'
    Saboteur = '妨碍', '善于削弱敌方的角色类型'

    def __init__(self, occupationName, des):
        self._occupationName = occupationName
        self._des = des

    @property
    def occupationName(self):
        return self._occupationName

    @property
    def des(self):
        return self._des
