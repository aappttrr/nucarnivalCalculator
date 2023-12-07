from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SnowPatrol(SSRCard):
    def __init__(self):
        super(SnowPatrol, self).__init__()
        self.cardId = 'SnowPatrol'
        self.round = 16
        self.cardName = '踏雪巡行'
        self.nickName = '霜昆'
        self.des = ''
        self.tag = ''
        self.role = CardRole.Quincy
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7187
        self.lv60s5Atk = 2277
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(1.24, 1.48, 1.73)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('SnowPatrol_skill', -0.125, 2, BuffType.BeDamageIncrease)
            role.addBuff(buff, self)
            if self.star >= 2:
                buff2 = Buff('SnowPatrol_skill2', 0.27, 4, BuffType.BeHotIncrease)
                role.addBuff(buff2, self)
            buff3 = Buff('SnowPatrol_skill3', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff3, self)
        return 0

    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('SnowPatrol_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    def passive_star_3(self):
        if super(SnowPatrol, self).passive_star_3():
            for role in self.teamMate:
                if role.occupation == CardOccupation.Healer:
                    buff = Buff('SnowPatrol_passive_star_3', 0.18, 50, BuffType.AtkIncrease)
                    buff.isPassive = True
                    role.addBuff(buff, self)
                buff2 = Buff('SnowPatrol_passive_star_32', 0.09, 50, BuffType.AtkIncrease)
                buff2.isPassive = True
                role.addBuff(buff2, self)

    def passive_star_5(self):
        if super(SnowPatrol, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('SnowPatrol_passive_star_5', 0.14, 50, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    def passive_tier_6(self):
        if super(SnowPatrol, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('SnowPatrol_passive_tier_6', 0.03, 50, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
