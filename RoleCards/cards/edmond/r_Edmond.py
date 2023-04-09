from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class REdmond(RCard):
    def __init__(self):
        super(REdmond, self).__init__()
        self.cardId = 'REdmond'
        self.cardName = '骑士'
        self.nickName = 'R团'
        self.role = CardRole.Edmond
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5052
        self.lv60s5Atk = 1423
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
        if super(REdmond, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Edmond:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('REdmond_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(REdmond, self).passive_star_5():
            buff = Buff('REdmond_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(REdmond, self).passive_tier_3():
            buff = Buff('REdmond_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
