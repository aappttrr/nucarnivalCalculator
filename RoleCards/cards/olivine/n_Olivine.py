from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.nCard import NCard
from RoleCards.common.rCard import RCard
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class NOlivine(NCard):
    def __init__(self):
        super(NOlivine, self).__init__()
        self.cardId = 'NOlivine'
        self.cardName = '圣职者'
        self.nickName = 'N奥'
        self.role = CardRole.Olivine
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Support
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 5657
        self.lv60s5Atk = 925
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 基础攻击力71%/86%/102%，提升全体攻击力（2）
    def skill(self, enemy):
        self.skillCount = 0
        magnification = self.getMagnification(0.71, 0.86, 1.02)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('NOlivine_skill', actualDamageIncrease, 2, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 基础攻击力30%，提升全体攻击力（1）
    def attack(self, enemy):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('NOlivine_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 全体攻击力+8%
    def passive_star_3(self):
        if super(NOlivine, self).passive_star_3():
            for role in self.teamMate:
                buff = Buff('NOlivine_passive_star_3', 0.08, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体攻击者攻击力+12%
    def passive_star_5(self):
        if super(NOlivine, self).passive_star_5():
            for role in self.teamMate:
                if role.occupation == CardOccupation.Striker:
                    buff = Buff('NOlivine_passive_star_5', 0.12, 0, BuffType.AtkIncrease)
                    buff.isPassive = True
                    role.addBuff(buff, self)

    # 全体攻击力+3%
    def passive_tier_3(self):
        if super(NOlivine, self).passive_tier_3():
            for role in self.teamMate:
                buff = Buff('NOlivine_passive_tier_3', 0.03, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
