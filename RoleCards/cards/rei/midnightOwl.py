from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class MidnightOwl(SSRCard):
    def __init__(self):
        super(MidnightOwl, self).__init__()
        self.cardId = 'MidnightOwl'
        self.cardName = '黑街潜行的夜鸮'
        self.nickName = '普敛'
        self.role = CardRole.Rei
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 7115
        self.lv60s5Atk = 2205
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻229%/273%/316%
        self.skillMagnificationLv1 = 2.29
        self.skillMagnificationLv2 = 2.73
        self.skillMagnificationLv3 = 3.16

        # 攻125%
        self.attackMagnification = 1.25

    # 受伤+10%（1）
    # 伤+25%（2）
    # 攻229%/273%/316%
    def skillBefore(self, enemies):
        buff1 = Buff("MidnightOwl_skill", 0.1, 1, BuffType.BeDamageIncrease)
        self.addBuff(buff1)

        buff2 = Buff("MidnightOwl_skill", 0.25, 2, BuffType.DamageIncrease)
        self.addBuff(buff2)

    # 队伍敛每1位，攻+8%(max 3)
    def passive_star_3(self):
        if super(MidnightOwl, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Rei:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('MidnightOwl_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(MidnightOwl, self).passive_star_5():
            buff = Buff('MidnightOwl_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(MidnightOwl, self).passive_tier_6():
            buff = Buff('MidnightOwl_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
