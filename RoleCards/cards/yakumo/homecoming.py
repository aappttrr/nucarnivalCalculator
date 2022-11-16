import math

from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.tierType import TierType


class Homecoming(SSRCard):

    def __init__(self):
        super(Homecoming, self).__init__()
        self.cardId = 'Homecoming'
        self.cardName = '回到故乡的那日'
        self.nickName = '普八/火八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4

        self.lv60s5Hp = 7507
        self.lv60s5Atk = 2099
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力+25%（3）
    # 攻击力247%/296%/345%造成伤害
    def skill(self, enemy):
        self.skillCount = 0

        buff = Buff('Homecoming_skill', 0.25, 3, BuffType.AtkIncrease)
        self.addBuff(buff)

        magnification = self.getMagnification(2.47, 2.96, 3.45)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)

        return damage

    # 攻击力+10%（3）
    # 攻击力100%造成伤害
    def attack(self, enemy):
        buff = Buff('Homecoming_attack', 0.1, 3, BuffType.AtkIncrease)
        self.addBuff(buff)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)
        return damage

    # HP>75%时，攻击力+25%（被动）
    def passive_star_3(self):
        if super(Homecoming, self).passive_star_3():
            hpBuff = Buff('Homecoming_passive_star_3', 0.25, 0, BuffType.AtkIncrease)
            hpBuff.isPassive = True
            hpBuff.conditionType = ConditionType.WhenHpMoreThan
            hpBuff.conditionValue = 0.75
            self.addBuff(hpBuff)

    # 攻击力+25%（被动）
    def passive_star_5(self):
        if super(Homecoming, self).passive_star_5():
            buff = Buff('Homecoming_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%（被动）
    def passive_tier_6(self):
        if super(Homecoming, self).passive_tier_6():
            buff = Buff('Homecoming_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
