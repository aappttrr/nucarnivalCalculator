from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType

class SmokedTimber(SRCard):
    def __init__(self):
        super(SmokedTimber, self).__init__()
        self.cardId = 'SmokedTimber'
        self.cardName = '沉郁的熏灼木'
        self.nickName = '限定SR昆'
        self.role = CardRole.Quincy
