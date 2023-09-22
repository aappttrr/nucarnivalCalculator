from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SREdmond(SRCard):
    def __init__(self):
        super(SREdmond, self).__init__()
        self.cardId = 'SREdmond'
        self.cardName = '骑士副团长'
        self.nickName = 'SR团'
        self.des = '万金油输出，SR中表现较好的输出，5星可用'
        self.tag = '万金油输出'
        self.role = CardRole.Edmond
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5977
        self.lv60s5Atk = 1672
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻125%
        self.attackMagnification = 1.25

        # 攻229%/273%/316%
        self.skillMagnificationLv1 = 2.29
        self.skillMagnificationLv2 = 2.73
        self.skillMagnificationLv3 = 3.16

    # 队伍艾德蒙特每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(SREdmond, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Edmond:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SREdmond_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(SREdmond, self).passive_star_5():
            buff = Buff('SREdmond_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(SREdmond, self).passive_tier_6():
            buff = Buff('SREdmond_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
