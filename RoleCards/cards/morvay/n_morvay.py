from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType


class NMorvay(NCard):
    def __init__(self):
        super(NMorvay, self).__init__()
        self.cardId = 'NMorvay'
        self.cardName = '情报专家'
        self.nickName = 'N墨'
        self.role = CardRole.Morvay
        self.type = CardType.Water
        self.occupation = CardOccupation.Guardian
        self.skillCD = 3

        self.lv60s5Hp = 6937
        self.lv60s5Atk = 747
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻100%
    # 最大HP20%/30%/40%护盾（1），防御减伤+10%（1），嘲讽（1），转防御
    def skill(self, enemy):
        self.skillCount = 0

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, False, True)

        ma = self.getMagnification(0.2, 0.3, 0.4)
        shield = self.maxHp * ma
        shield = roundDown(shield)
        shield = self.increaseShield(shield)

        buff = Buff('NMorvay_skill', shield, 1, BuffType.Shield)
        self.addBuff(buff)

        buff2 = Buff('NMorvay_skill_2', 0.1, 1, BuffType.DefenseDamageReduction)
        self.addBuff(buff2)

        buff3 = Buff('NMorvay_skill_3', 0, 1, BuffType.Taunt)
        self.addBuff(buff3)

        self.defense = True

        return damage

    # 攻100%，转防御
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)

        self.defense = True

        return damage

    # 有艾斯特，最大HP+13%
    # 守护<=1，受伤-10%
    def passive_star_3(self):
        if super(NMorvay, self).passive_star_3():
            count = 0
            hasAster = False
            for role in self.teamMate:
                if role.role == CardRole.Aster:
                    hasAster = True
                if role.occupation == CardOccupation.Guardian:
                    count += 1

            if hasAster:
                buff = Buff('NMorvay_passive_star_3', 0.13, 0, BuffType.HpIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if count <= 1:
                buff = Buff('NMorvay_passive_star_3_2', -0.1, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 受伤-10%
    def passive_star_5(self):
        if super(NMorvay, self).passive_star_5():
            buff = Buff('NMorvay_passive_star_5', -0.1, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 受回复量+20%
    def passive_tier_3(self):
        if super(NMorvay, self).passive_tier_3():
            buff = Buff('NMorvay_passive_tier_3', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
