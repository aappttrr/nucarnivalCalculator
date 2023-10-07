from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ApatheticOutsider(SRCard):
    def __init__(self):
        super(ApatheticOutsider, self).__init__()
        self.cardId = 'ApatheticOutsider'
        self.round = 19
        self.cardName = '冷眼异客'
        self.nickName = '锖狐'
        self.des = ''
        self.tag = '必杀增益'
        self.role = CardRole.Kuya
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 6653
        self.lv60s5Atk = 1921
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 基础攻击力112%/133%/154%，提升全体攻击力（1）
    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(1.12, 1.33, 1.54)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('ApatheticOutsider_skill', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 基础攻击力30%，提升全体攻击力（1）
    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('SROlivine_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 全体必杀+27%
    def passive_star_3(self):
        if super(ApatheticOutsider, self).passive_star_3():
            for role in self.teamMate:
                buff = Buff('ApatheticOutsider_passive_star_3', 0.27, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体必杀+20%
    def passive_star_5(self):
        if super(ApatheticOutsider, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('ApatheticOutsider_passive_star_5', 0.20, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体必杀+5%
    def passive_tier_6(self):
        if super(ApatheticOutsider, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('ApatheticOutsider_passive_tier_6', 0.05, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
