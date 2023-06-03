from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class GalacticMist(SSRCard):
    def __init__(self):
        super(GalacticMist, self).__init__()
        self.cardId = 'GalacticMist'
        self.round = 11
        self.cardName = '夜雾银星'
        self.nickName = '火伊'
        self.role = CardRole.Eiden
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 5
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7898
        self.lv60s5Atk = 2063
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 基攻22%/27%/32%自身以外全体攻击力增加（5）
    # 全体受到伤害减少5%（5）
    # 自身以外全体必杀冷却-1
    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(0.22, 0.27, 0.32)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            if role.cardId != self.cardId:
                buff = Buff('GalacticMist_skill', actualDamageIncrease, 5, BuffType.AtkIncreaseByActualValue)
                role.addBuff(buff, self)
                role.skillCount += 1

            buff2 = Buff('GalacticMist_skill_2', -0.05, 5, BuffType.BeDamageIncrease)
            role.addBuff(buff2, self)
        return 0

    # 基攻30%自身以外全体攻击力增加（1）
    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            if role.cardId == self.cardId:
                continue
            buff = Buff('GalacticMist_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 自身以外全体攻击力+10%
    def passive_star_3(self):
        if super(GalacticMist, self).passive_star_3():
            for role in self.teamMate:
                if role.cardId == self.cardId:
                    continue
                buff = Buff('GalacticMist_passive_star_3', 0.1, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体伤+9%
    def passive_star_5(self):
        if super(GalacticMist, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('GalacticMist_passive_star_5', 0.09, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体伤+2%
    # 受治疗+5%
    # 受伤-2%
    def passive_tier_6(self):
        if super(GalacticMist, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('GalacticMist_passive_tier_6', 0.02, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

                buff2 = Buff('GalacticMist_passive_tier_6_2', 0.05, 0, BuffType.BeHealIncrease)
                buff2.isPassive = True
                role.addBuff(buff2, self)

                buff3 = Buff('GalacticMist_passive_tier_6_3', -0.02, 0, BuffType.BeDamageIncrease)
                buff3.isPassive = True
                role.addBuff(buff3, self)
