from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class FrostedVirtue(SSRCard):
    def __init__(self):
        super(FrostedVirtue, self).__init__()
        self.cardId = 'FrostedVirtue'
        self.round = 10
        self.cardName = '祝祷者的霜夜心愿'
        self.nickName = '冬奥'
        self.des = '带增益的治疗，增益和治疗都给的很少，已经比不上新的伞昆和烟狼，实在缺奶可用'
        self.tag = '增伤治疗 / 攻击力增益'
        self.role = CardRole.Olivine
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Defense
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 7649
        self.lv60s5Atk = 2134
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻25%全体治
        self.attackHealMagnification = 0.25

        # 攻100%全体治
        self.skillHealMagnificationLv1 = 1
        self.skillHealMagnificationLv2 = 1
        self.skillHealMagnificationLv3 = 1

    # 攻100%全体治
    # 持续治疗攻22%/34%/45%（3）
    # 基攻13%/15%/17%全体攻+（4）
    def skillHeal(self, enemies, currentAtk):
        ma_atk = self.getMagnification(0.13, 0.15, 0.17)
        ma_hot = self.getMagnification(0.22, 0.34, 0.45)

        heal = super(FrostedVirtue, self).skillHeal(enemies, currentAtk)

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        actualDamageIncrease = self.atk * ma_atk
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('FrostedVirtue_skill', hotHeal, 3, BuffType.Hot)
            role.addBuff(buff, self)

            buff2 = Buff('FrostedVirtue_skill_2', actualDamageIncrease, 4, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff2, self)
        return heal

    # 攻25%全体治
    # 持续治疗攻25%（2）
    def attackHeal(self, enemies, currentAtk):
        heal = super(FrostedVirtue, self).attackHeal(enemies, currentAtk)

        hotHeal = currentAtk * 0.25
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)
        for role in self.teamMate:
            buff = Buff('FrostedVirtue_attack', hotHeal, 2, BuffType.Hot)
            role.addBuff(buff, self)
        return heal

    # 队伍有啖天，攻+14%
    # 队伍有昆西，攻+14%
    def passive_star_3(self):
        if super(FrostedVirtue, self).passive_star_3():
            hasDante = False
            hasQuincy = False
            for role in self.teamMate:
                if role.role == CardRole.Dante:
                    hasDante = True
                elif role.role == CardRole.Quincy:
                    hasQuincy = True

            if hasDante:
                buff = Buff('FrostedVirtue_passive_star_3', 0.14, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)
            if hasQuincy:
                buff = Buff('FrostedVirtue_passive_star_3_2', 0.14, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 全体HP+12%
    def passive_star_5(self):
        if super(FrostedVirtue, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('FrostedVirtue_passive_star_5', 0.12, 0, BuffType.HpIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 攻+10%
    def passive_tier_6(self):
        if super(FrostedVirtue, self).passive_tier_6():
            buff = Buff('FrostedVirtue_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
