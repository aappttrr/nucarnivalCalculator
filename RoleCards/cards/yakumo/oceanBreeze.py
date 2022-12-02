from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class OceanBreeze(SSRCard):
    def __init__(self):
        super(OceanBreeze, self).__init__()
        self.cardId = 'OceanBreeze'
        self.cardName = '倾听海风'
        self.nickName = '夏八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7222
        self.lv60s5Atk = 2170
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 自基攻62%/74%/87%，全体攻击力增加（2）
    # 全体护盾+55%/65%/75%(2)，
    # 全体持续治疗+55%/65%/75%(3)
    def skill(self, enemy, printInfo=False):
        ma = self.getMagnification(0.62, 0.74, 0.87)
        ma2 = self.getMagnification(0.55, 0.65, 0.75)

        actualDamageIncrease = self.atk * ma
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('OceanBreeze_skill', actualDamageIncrease, 2, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)

            buff2 = Buff('OceanBreeze_skill_2', ma2, 2, BuffType.BeShieldIncrease)
            role.addBuff(buff2, self)

            buff3 = Buff('OceanBreeze_skill_3', ma2, 3, BuffType.HotIncrease)
            role.addBuff(buff3, self)

        return 0

    def skillAfter(self, enemy):
        for role in self.teamMate:
            # 5星被动
            # 攻击时，我方全体攻+2（max 6)
            if self.passive_star_5() and role.calBuffCount('OceanBreeze_passive_star_5') < 6:
                buff = Buff('OceanBreeze_passive_star_5', 0.02, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 自基攻25%，全体攻击力增加（1）
    # 全体护盾+25%(1)，
    # 全体持续治疗+25%(1)
    def attack(self, enemy, printInfo=False):
        actualDamageIncrease = self.atk * 0.25
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('OceanBreeze_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)

            buff2 = Buff('OceanBreeze_attack_2', 0.25, 1, BuffType.BeShieldIncrease)
            role.addBuff(buff2, self)

            buff3 = Buff('OceanBreeze_attack_3', 0.25, 1, BuffType.HotIncrease)
            role.addBuff(buff3, self)

        return 0

    def attackAfter(self, enemy):
        for role in self.teamMate:
            # 5星被动
            # 攻击时，我方全体攻+2（max 6)
            if self.passive_star_5() and role.calBuffCount('OceanBreeze_passive_star_5') < 6:
                buff = Buff('OceanBreeze_passive_star_5', 0.02, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 我方攻击、守护、治疗攻+12%
    def passive_star_3(self):
        if super(OceanBreeze, self).passive_star_3():
            for role in self.teamMate:
                if role.occupation == CardOccupation.Striker or role.occupation == CardOccupation.Guardian or role.occupation == CardOccupation.Healer:
                    buff = Buff('OceanBreeze_passive_star_3', 0.12, 0, BuffType.AtkIncrease)
                    buff.isPassive = True
                    role.addBuff(buff, self)

    # 攻击时，我方全体攻+2（max 6)
    def passive_star_5(self):
        return super(OceanBreeze, self).passive_star_5()
        
    # 我方全体攻+3%
    def passive_tier_6(self):
        if super(OceanBreeze, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('OceanBreeze_passive_tier_6', 0.03, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
