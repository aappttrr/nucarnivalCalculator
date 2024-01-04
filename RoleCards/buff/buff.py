from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole


class Buff:
    def __init__(self, _buffId, _value, _round, _type):
        # buffId，用于判断同类型buff加成了多少次
        self.buffId = _buffId

        # buff类型
        self.buffType: BuffType = _type

        # 数值
        self.value = _value

        # 持续回合
        self.round = _round

        # 是否为被动
        self.isPassive = False

        # 生效条件
        self.conditionType = None

        # 生效条件的值
        self.conditionValue = 0

        # 是否视为普攻
        self.seeAsAttack = False

        # 是否视为必杀
        self.seeAsSkill = False

        # 是否使用基础攻击力
        self.useBaseAtk = False

        # buff来源
        self.source = None

        # 是否为群伤
        self.isGroup = False

        self.addBuffTurn = 0
        self.targetRole: CardRole = None
        self.targetOccupation: CardOccupation = None

    def nextRound(self):
        if self.round > 0:
            self.round -= 1

    def isOver(self):
        if self.isPassive:
            return False
        if self.round <= 0:
            return True
        return False

    def getBuffType(self):
        return self.buffType

    def getValue(self):
        return self.value
