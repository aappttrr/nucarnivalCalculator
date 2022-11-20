from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class KitsuneDream(SSRCard):
    def __init__(self):
        super(KitsuneDream, self).__init__()
        self.cardId = 'KitsuneDream'
        self.cardName = '狐火映追忆'
        self.nickName = '火狐'
        self.role = CardRole.Kuya
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 8076
        self.lv60s5Atk = 1956
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力136%/159%/182%挂dot（3）
    # 目标受dot+10%（max 3）
    # 目标必杀-10%（2）
    def skill(self, enemy):
        self.skillCount = 0
        magnification = self.getMagnification(1.36, 1.59, 1.82)
        currentAtk = self.getCurrentAtk()

        dotDamage = currentAtk * magnification
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('KitsuneDream_skill', dotDamage, 3, BuffType.Dot)
        enemy.addBuff(buff, self)
        return 0

    def skillAfter(self, enemy):
        if enemy.calBuffCount('KitsuneDream_skill_2') < 3:
            buff2 = Buff('KitsuneDream_skill_2', 0.1, 0, BuffType.BeDotIncrease)
            buff2.isPassive = True
            enemy.addBuff(buff2, self)

            buff3 = Buff('KitsuneDream_skill_3', -0.1, 2, BuffType.SkillIncrease)
            enemy.addBuff(buff3, self)
        if self.passive_star_5():
            buff4 = Buff('KitsuneDream_passive_star_5', -0.15, 3, BuffType.AtkIncrease)
            enemy.addBuff(buff4, self)

    # 攻击力50%挂dot（4）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()

        dotDamage = currentAtk * 0.5
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('KitsuneDream_attack', dotDamage, 4, BuffType.Dot)
        enemy.addBuff(buff, self)
        return 0

    # hp>75%,攻击力+27%
    def passive_star_3(self):
        if super(KitsuneDream, self).passive_star_3():
            buff = Buff('KitsuneDream_passive_star_3', 0.27, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            buff.conditionType = ConditionType.WhenHpMoreThan
            buff.conditionValue = 0.75
            self.addBuff(buff)

    # 必杀时，触发使目标攻-15%(3)
    def passive_star_5(self):
        return super(KitsuneDream, self).passive_star_5()

    # 持续伤害+15%
    def passive_tier_6(self):
        if super(KitsuneDream, self).passive_tier_6():
            buff = Buff('KitsuneDream_passive_tier_6', 0.15, 0, BuffType.DotIncrease)
            buff.isPassive = True
            self.addBuff(buff)
