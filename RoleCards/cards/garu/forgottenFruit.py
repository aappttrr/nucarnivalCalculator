from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType

class ForgottenFruit(SSRCard):
    def __init__(self):
        super(ForgottenFruit, self).__init__()
        self.cardId = 'ForgottenFruit'
        self.cardName = '遗忘的甜蜜果'
        self.nickName = '果狼？'
        self.role = CardRole.Garu
