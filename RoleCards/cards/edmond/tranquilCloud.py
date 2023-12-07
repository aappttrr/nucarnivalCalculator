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
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7258
        self.lv60s5Atk = 2277
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力75%
        self.attackHealMagnification = 0.75

        # 攻击力100%
        self.skillHealMagnificationLv1 = 1
        self.skillHealMagnificationLv3 = 1
        self.skillHealMagnificationLv2 = 1
        self.roundCount = 0

    def skillBefore(self, enemies):
        if self.star >= 2:
            buff = Buff('TranquilCloud_skill', 0.135, 3, BuffType.AtkIncrease)
            self.addBuff(buff)

    def skillHeal(self, enemies, currentAtk):
        heal = super(TranquilCloud, self).skillHeal(enemies, currentAtk)
        ma_hot = self.getMagnification(0.29, 0.4, 0.51)

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('TranquilCloud_skill', hotHeal, 4, BuffType.Hot)
            role.addBuff(buff, self)

        dotDamage = currentAtk * 0.67
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff2 = Buff('TranquilCloud_skill2', dotDamage, 3, BuffType.Dot)
        enemies.addBuff(buff2, self)
        return heal

    def passive_star_3(self):
        if super(TranquilCloud, self).passive_star_3():
            buff = Buff('TranquilCloud_passive_star_3', 0.18, 50, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def nextRound(self):
        super(TranquilCloud, self).nextRound()
        self.roundCount += 1
        if self.roundCount == 5:
            buff = Buff('TranquilCloud_passive_star_32', 0.39, 50, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def passive_star_5(self):
        if super(TranquilCloud, self).passive_star_5():
            buff = Buff('TranquilCloud_passive_star_5', 0.27, 50, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def passive_tier_6(self):
        if super(TranquilCloud, self).passive_tier_6():
            buff = Buff('TranquilCloud_passive_tier_6', 0.1, 50, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)


