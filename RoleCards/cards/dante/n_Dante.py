from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType


class NDante(NCard):
    def __init__(self):
        super(NDante, self).__init__()
        self.cardId = 'NDante'
        self.cardName = '治理者'
        self.nickName = 'N啖'
        self.role = CardRole.Dante
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.skillCD = 3

        self.lv60s5Hp = 4482
        self.lv60s5Atk = 1174
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 目标受伤+12%（2），攻204%/238%/273%
    def skill(self, enemy):
        self.skillCount = 0
        buff = Buff('NDante_skill', 0.12, 2, BuffType.BeDamageIncrease)
        enemy.addBuff(buff, self)

        magnification = self.getMagnification(2.04, 2.38, 2.73)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    # 解除目标防御，攻100%
    def attack(self, enemy):
        enemy.defense = False

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)
        return damage

    # 队伍啖天每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(NDante, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Dante:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NDante_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(NDante, self).passive_star_5():
            buff = Buff('NDante_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(NDante, self).passive_tier_3():
            buff = Buff('NDante_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
