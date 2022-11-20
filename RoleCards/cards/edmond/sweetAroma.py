from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SweetAroma(SSRCard):
    def __init__(self):
        super(SweetAroma, self).__init__()
        self.cardId = 'SweetAroma'
        self.cardName = '初露芬芳的甜味'
        self.nickName = '火团'
        self.role = CardRole.Edmond
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7649
        self.lv60s5Atk = 2063
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力204%/238%/273%
    # 目标受普攻伤害+27%（3）
    def skill(self, enemy):
        self.skillCount = 0

        magnification = self.getMagnification(2.04, 2.38, 2.73)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    def skillAfter(self, enemy):
        buff = Buff('SweetAroma_skill', 0.27, 3, BuffType.BeAttackIncrease)
        enemy.addBuff(buff, self)

    # 攻击力125%
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1.25, True, False)
        return damage

    def beHealed(self, heal, seeAsHeal):
        super(SweetAroma, self).beHealed(heal, seeAsHeal)
        if seeAsHeal and self.passive_star_3() and self.calBuffCount('SweetAroma_passive_star_3') < 5:
            buff = Buff('SweetAroma_passive_star_3', 0.05, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 被治疗时，攻击力+5%（max 5
    def passive_star_3(self):
        return super(SweetAroma, self).passive_star_3()

    # hp>85%，攻击力+30%
    def passive_star_5(self):
        if super(SweetAroma, self).passive_star_5():
            buff = Buff('SweetAroma_passive_star_5', 0.3, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            buff.conditionType = ConditionType.WhenHpMoreThan
            buff.conditionValue = 0.85
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(SweetAroma, self).passive_tier_6():
            buff = Buff('SweetAroma_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
