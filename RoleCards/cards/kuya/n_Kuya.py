from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType


class NKuya(NCard):
    def __init__(self):
        super(NKuya, self).__init__()
        self.cardId = 'NKuya'
        self.cardName = '妖狐'
        self.nickName = 'N狐'
        self.role = CardRole.Kuya
        self.type = CardType.Wood
        self.occupation = CardOccupation.Saboteur
        self.skillCD = 4

        self.lv60s5Hp = 4660
        self.lv60s5Atk = 1102
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻247%/296%/345%，目标受回复量-100%（2）
    def skill(self, enemy):
        self.skillCount = 0
        magnification = self.getMagnification(2.47, 2.96, 3.45)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    def skillAfter(self, enemy):
        buff = Buff('NKuya_skill', -1, 2, BuffType.BeHealIncrease)
        enemy.addBuff(buff, self)

    # 攻100%，目标受回复量-50%（1）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)
        return damage

    def attackAfter(self, enemy):
        buff = Buff('NKuya_attack', -0.5, 1, BuffType.BeHealIncrease)
        enemy.addBuff(buff, self)

    # 队伍玖夜每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(NKuya, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Kuya:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NKuya_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(NKuya, self).passive_star_5():
            buff = Buff('NKuya_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(NKuya, self).passive_tier_3():
            buff = Buff('NKuya_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)