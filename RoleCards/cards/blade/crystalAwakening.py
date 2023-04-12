from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType

class CrystalAwakening(SSRCard):
    def __init__(self):
        super(CrystalAwakening, self).__init__()
        self.cardId = 'CrystalAwakening'
        self.cardName = '觉醒的晶莹花'
        self.nickName = '花布？'
        self.role = CardRole.Blade
