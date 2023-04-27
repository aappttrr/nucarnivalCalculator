from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RRei(RCard):
    def __init__(self):
        super(RRei, self).__init__()
        self.cardId = 'RRei'
        self.cardName = '组织学士'
        self.nickName = 'R敛'
        self.role = CardRole.Rei
        self.occupation = CardOccupation.Saboteur
        self.cardType = CardType.Water
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5479
        self.lv60s5Atk = 1316
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

        # 攻125%
        self.attackMagnification = 1.25

    # 队伍敛每1位，攻+8%(max 3)
    def passive_star_3(self):
        if super(RRei, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Rei:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RRei_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(RRei, self).passive_star_5():
            buff = Buff('RRei_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(RRei, self).passive_tier_6():
            buff = Buff('RRei_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
