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


class AromaticExotica(SSRCard):
    def __init__(self):
        super(AromaticExotica, self).__init__()
        self.cardId = 'AromaticExotica'
        self.round = 16
        self.cardName = '异域蜜香的艳闻'
        self.nickName = '沙狐'
        self.des = 'dot混伤输出，带常驻通用易伤，伤害很高，吃拐能力较低，适合搭配通用辅助和拐，2星可用'
        self.tag = 'dot混伤输出 / 通用易伤'
        self.role = CardRole.Kuya
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 6831
        self.lv60s5Atk = 2419
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力63%
        self.attackMagnification = 0.63

        # 攻247%/296%/345%
        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    def skillBefore(self, enemies):
        if self.star >= 2:
            buff = Buff('AromaticExotica_skill', 0.135, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            if enemies.calBuffCount('AromaticExotica_skill') < 2:
                enemies.addBuff(buff, self)

    def skillAfter(self, enemies):
        magnification = self.getMagnification(0.62, 0.74, 0.86)
        dotDamage = self.getCurrentAtk() * magnification
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('AromaticExotica_skill2', dotDamage, 4, BuffType.Dot)
        enemies.addBuff(buff, self)

    def attackAfter(self, enemies):
        dotDamage = self.getCurrentAtk() * 0.5
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('AromaticExotica_attack', dotDamage, 2, BuffType.Dot)
        enemies.addBuff(buff, self)

    def passive_star_3(self):
        if super(AromaticExotica, self).passive_star_3():
            buff = Buff('AromaticExotica_passive_star_3', 0.18, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
            buff2 = Buff('AromaticExotica_passive_star_32', 0.36, 0, BuffType.DotIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)

    def passive_star_5(self):
        if super(AromaticExotica, self).passive_star_5():
            buff = Buff('AromaticExotica_passive_star_5', 0.37, 0, BuffType.AtkIncrease)
            buff.conditionType = ConditionType.WhenHpLessThan
            buff.conditionValue = 0.99
            buff.isPassive = True
            self.addBuff(buff)

    def passive_tier_6(self):
        if super(AromaticExotica, self).passive_tier_6():
            buff = Buff('AromaticExotica_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
