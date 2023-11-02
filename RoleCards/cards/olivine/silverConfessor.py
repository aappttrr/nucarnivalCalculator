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


class SilverConfessor(SSRCard):
    def __init__(self):
        super(SilverConfessor, self).__init__()
        self.cardId = 'SilverConfessor'
        self.round = 20
        self.cardName = '银弹的告解者'
        self.nickName = '枪奥'
        self.des = ''
        self.role = CardRole.Olivine
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7471
        self.lv60s5Atk = 2205
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 以攻击力125%对目标造成伤害
        self.attackMagnification = 1.25

        # 攻击力348%/430%/513%对目标造成伤害
        self.skillMagnificationLv1 = 3.48
        self.skillMagnificationLv2 = 4.3
        self.skillMagnificationLv3 = 5.13

    # 以攻击力27%/36%/44%对我方全体进行持续治疗(4回合)
    # 再使目标受到必杀技伤害增加20%(3回合)
    # 再以攻击力348%/430%/513%对目标造成伤害
    def skillBefore(self, enemies):
        currentAtk = self.getCurrentAtk()
        ma2 = self.getMagnification(0.27, 0.36, 0.44)

        hotHeal = currentAtk * ma2
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('SilverConfessor_skill', hotHeal, 4, BuffType.Hot)
            role.addBuff(buff, self)

        if self.star >= 2:
            buff2 = Buff('SilverConfessor_skill2', 0.2, 3, BuffType.BeSkillIncrease)
            enemies.addBuff(buff2, self)

    # 队伍中每存在1名定位为攻击的角色，发动必杀技伤害增加18%(最多3次)
    def passive_star_3(self):
        if super(SilverConfessor, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SilverConfessor_passive_star_3', 0.18 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻击力增加27%
    def passive_star_5(self):
        if super(SilverConfessor, self).passive_star_5():
            buff = Buff('SilverConfessor_passive_star_5', 0.27, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%
    def passive_tier_6(self):
        if super(SilverConfessor, self).passive_tier_6():
            buff = Buff('SilverConfessor_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
