from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class InfernalTreatymaker(SSRCard):
    def __init__(self):
        super(InfernalTreatymaker, self).__init__()
        self.cardId = 'InfernalTreatymaker'
        self.round = 20
        self.cardName = '烈焰的缔约者'
        self.nickName = ''
        self.des = ''
        self.tag = ''
        self.role = CardRole.Dante
        # self.cardType = CardType.Water
        # self.occupation = CardOccupation.Striker
        # self.tierType = TierType.Attack
        # self.skillCD = 3
        # self.ped = PassiveEffectivenessDifficulty.veryDifficult
        #
        # self.lv60s5Hp = 6511
        # self.lv60s5Atk = 2419
        # self.hp = self.lv60s5Hp
        # self.atk = self.lv60s5Atk
        #
        # # 攻击力125%
        # self.attackMagnification = 1.25
        #
        # # 攻击力204%/238%/273%
        # self.skillMagnificationLv1 = 2.04
        # self.skillMagnificationLv2 = 2.38
        # self.skillMagnificationLv3 = 2.73