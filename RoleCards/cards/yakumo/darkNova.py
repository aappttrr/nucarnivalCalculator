from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class DarkNova(SSRCard):
    def __init__(self):
        super(DarkNova, self).__init__()
        self.cardId = 'DarkNova'
        self.cardName = '幽暧新星的祷词'
        self.nickName = '早八'
        self.role = CardRole.Yakumo
        # self.cardType = CardType.Dark
        # self.occupation = CardOccupation.Striker
        # self.tierType = TierType.Attack
        # self.skillCD = 3
        # self.ped = PassiveEffectivenessDifficulty.medium
        #
        # self.lv60s5Hp = 7044
        # self.lv60s5Atk = 2241
        # self.hp = self.lv60s5Hp
        # self.atk = self.lv60s5Atk
        # # 攻100 %
        # self.attackMagnification = 1
        #
        # # 攻击力204%/238%/273%
        # self.skillMagnificationLv1 = 2.04
        # self.skillMagnificationLv2 = 2.38
        # self.skillMagnificationLv3 = 2.73