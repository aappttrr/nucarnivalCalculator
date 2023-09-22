from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class CaptiveStar(SSRCard):
    def __init__(self):
        super(CaptiveStar, self).__init__()
        self.cardId = 'CaptiveStar'
        self.round = 14
        self.cardName = '囹圄之星的秘闻'
        self.nickName = '秘奥/晚奥'
        self.des = '必杀辅助，数值给的超多，很优秀的辅助，即使不是必杀队伍也可以用，建议2星'
        self.tag = '必杀辅助 / 必杀增益 / 通用增益 / 自残'
        self.role = CardRole.Olivine
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7791
        self.lv60s5Atk = 2099
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 以当前HP 20%对自身造成真实伤害
    # lv2后增加，使我方全体必杀伤害增加20%（1）
    def skillBefore(self, enemies):
        damage = self.hpCurrent * 0.2
        damage = roundDown(damage)
        self.hpCurrent -= damage

        self.doBloodSuck(damage)

        if self.star >= 2:
            for mate in self.teamMate:
                buff = Buff('CaptiveStar_skill', 0.2, 1, BuffType.SkillIncrease)
                mate.addBuff(buff, self)

    # 基础攻击力120%/143%/167%，提升全体攻击力（1）
    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(1.2, 1.43, 1.67)

        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('CaptiveStar_skill_2', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 3星被动，必杀时，全体伤+15%（3）
    def skillAfter(self, enemies):
        if self.passive_star_3():
            for role in self.teamMate:
                buff = Buff('CaptiveStar_skill_3', 0.15, 3, BuffType.DamageIncrease)
                role.addBuff(buff, self)

    # 以当前HP 5%对自身造成真实伤害
    def attackBefore(self, enemies):
        damage = self.hpCurrent * 0.05
        damage = roundDown(damage)
        self.hpCurrent -= damage

        self.doBloodSuck(damage)

    # 基础攻击力35%，提升全体攻击力（1）
    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.35
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('CaptiveStar_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 全体攻击者攻击力+14%
    def passive_star_5(self):
        if super(CaptiveStar, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('CaptiveStar_passive_star_5', 0.14, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体攻击力+3%
    def passive_tier_6(self):
        if super(CaptiveStar, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('CaptiveStar_passive_tier_6', 0.03, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
