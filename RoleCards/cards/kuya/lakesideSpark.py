from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class LakesideSpark(SSRCard):
    def __init__(self):
        super(LakesideSpark, self).__init__()
        self.cardId = 'LakesideSpark'
        self.round = 7
        self.cardName = '穿梭盘月之煦'
        self.nickName = '月狐'
        self.des = '吸血治疗，吸血看队友本身伤害能力，急救能力较差，需要防御的时候治疗也不够，不建议使用'
        self.role = CardRole.Kuya
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Defense
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 8218
        self.lv60s5Atk = 1921
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力68%治疗
        self.attackHealMagnification = 0.68

        # 攻击力133%/157%/182%治疗
        self.skillHealMagnificationLv1 = 1.33
        self.skillHealMagnificationLv2 = 1.57
        self.skillHealMagnificationLv3 = 1.82

    # 攻击力133%/157%/182%治疗
    # 我方全体吸血效果15%（4）
    def skillAfter(self, enemies):
        for role in self.teamMate:
            buff = Buff('LakesideSpark_skill', 0.15, 4, BuffType.BloodSucking)
            role.addBuff(buff, self)

    # 攻击力68%治疗
    # 我方全体吸血效果15%（1）
    def attackAfter(self, enemies):
        for role in self.teamMate:
            buff = Buff('LakesideSpark_attack', 0.15, 1, BuffType.BloodSucking)
            role.addBuff(buff, self)

    # 攻击力+25%
    # 妨碍角色攻击力+12%
    def passive_star_3(self):
        if super(LakesideSpark, self).passive_star_3():
            buff = Buff('LakesideSpark_passive_star_3', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

            for role in self.teamMate:
                if role.occupation == CardOccupation.Saboteur:
                    buff2 = Buff('LakesideSpark_passive_star_3_2', 0.12, 0, BuffType.AtkIncrease)
                    buff2.isPassive = True
                    role.addBuff(buff2, self)

    # 最大hp+6%
    # 全体治疗攻击力+25%
    def passive_star_5(self):
        if super(LakesideSpark, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('LakesideSpark_passive_star_5', 0.06, 0, BuffType.HpIncrease)
                buff.isPassive = True
                self.addBuff(buff)

                if role.occupation == CardOccupation.Healer:
                    buff2 = Buff('LakesideSpark_passive_star_5_2', 0.25, 0, BuffType.AtkIncrease)
                    buff2.isPassive = True
                    role.addBuff(buff2, self)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(LakesideSpark, self).passive_tier_6():
            buff = Buff('LakesideSpark_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
