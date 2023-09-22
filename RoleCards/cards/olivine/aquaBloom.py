from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class AquaBloom(SSRCard):
    def __init__(self):
        super(AquaBloom, self).__init__()
        self.cardId = 'AquaBloom'
        self.round = 3
        self.cardName = '翠灿之水的花使'
        self.nickName = '花奥'
        self.des = '必杀辅助，数值给的比较少，目前全方位被晚奥代替，不建议使用'
        self.tag = '必杀辅助，必杀增益'
        self.role = CardRole.Olivine
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 9321
        self.lv60s5Atk = 1672
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 基础攻击力107%/129%/152%，提升全体攻击力（1）
    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(1.07, 1.29, 1.52)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('AquaBloom_skill', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 基础攻击力30%，提升全体攻击力（1）
    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('AquaBloom_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 全体必杀+12%
    def passive_star_3(self):
        if super(AquaBloom, self).passive_star_3():
            for role in self.teamMate:
                buff = Buff('AquaBloom_passive_star_3', 0.12, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体攻击、守护、妨碍必杀+18%
    def passive_star_5(self):
        if super(AquaBloom, self).passive_star_5():
            for role in self.teamMate:
                if role.occupation == CardOccupation.Striker or role.occupation == CardOccupation.Guardian or role.occupation == CardOccupation.Saboteur:
                    buff = Buff('AquaBloom_passive_star_5', 0.18, 0, BuffType.SkillIncrease)
                    buff.isPassive = True
                    role.addBuff(buff, self)

    # 全体必杀+5%
    def passive_tier_6(self):
        if super(AquaBloom, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('AquaBloom_passive_tier_6', 0.05, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
