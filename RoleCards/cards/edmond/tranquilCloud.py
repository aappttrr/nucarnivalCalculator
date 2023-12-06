from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class TranquilCloud(SSRCard):
    def __init__(self):
        super(TranquilCloud, self).__init__()
        self.cardId = 'TranquilCloud'
        self.round = 16
        self.cardName = '清音流云'
        self.nickName = '霜团'
        self.tag = ''
        self.role = CardRole.Edmond
        # self.cardType = CardType.Fire
        # self.occupation = CardOccupation.Support
        # self.tierType = TierType.Balance
        # self.skillCD = 3
        # self.ped = PassiveEffectivenessDifficulty.veryEasy

        # self.lv60s5Hp = 7969
        # self.lv60s5Atk = 2063
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力100%
        # self.attackMagnification = 1

        # 攻击力100%
        # self.skillMagnificationLv1 = 1
        # self.skillMagnificationLv2 = 1
        # self.skillMagnificationLv3 = 1