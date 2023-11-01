from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SilverConfessor(SSRCard):
    def __init__(self):
        super(SilverConfessor, self).__init__()
        self.cardId = 'SilverConfessor'
        self.round = 20
        self.cardName = '银弹的告解者'
        self.nickName = ''
        self.des = ''
        self.role = CardRole.Olivine
        # self.cardType = CardType.Dark
        # self.occupation = CardOccupation.Striker
        # self.tierType = TierType.Attack
        # self.skillCD = 4
        # self.ped = PassiveEffectivenessDifficulty.difficult
        #
        # self.lv60s5Hp = 6724
        # self.lv60s5Atk = 2348
        # self.hp = self.lv60s5Hp
        # self.atk = self.lv60s5Atk
        # # 攻击力50%对1、3、5造成伤害
        # self.attackMagnification = 0.5
        #
        # # 攻击力107%/132%/156%对1、3、5造成伤害
        # self.skillMagnificationLv1 = 1.07
        # self.skillMagnificationLv2 = 1.32
        # self.skillMagnificationLv3 = 1.56