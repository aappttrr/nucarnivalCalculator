from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RainyRebirth(SSRCard):
    def __init__(self):
        super(RainyRebirth, self).__init__()
        self.cardId = 'RainyRebirth'
        self.round = 15
        self.cardName = '雨季终时的新生'
        self.nickName = '伞敛'
