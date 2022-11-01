from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.tierType import TierType


class WildWolf(SRCard):
    def __init__(self):
        super(WildWolf, self).__init__()
        self.cardId = 'WildWolf'
        self.cardName = '流浪小狼'
        self.nickName = 'SR狼'
        self.role = CardRole.Garu
        self.type = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.isGroup = True

        self.lv60s5Hp = 5799
        self.lv60s5Atk = 1707
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 敌全体受伤+8%（1），攻124%/148%/173%（群）
    def skill(self, enemy):
        self.skillCount = 0
        for monster in self.enemies:
            buff = Buff('WildWolf_skill', 0.08, 1, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

        magnification = self.getMagnification(1.24, 1.48, 1.73)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)

        return damage

    # 敌全体受伤+4%（2），攻50%（群）
    def attack(self, enemy):
        self.skillCount = 0
        for monster in self.enemies:
            buff = Buff('WildWolf_attack', 0.04, 2, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 0.5, True, False)

        return damage

    def nextRound(self):
        super(WildWolf, self).nextRound()
        # 每回合攻+4%（max 10）
        if self.passive_star_5() and self.calBuffCount('WildWolf_passive_star_5') < 10:
            buff = Buff('WildWolf_passive_star_5', 0.04, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 队伍可尔每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(WildWolf, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Garu:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('WildWolf_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 每回合攻+4%（max 10）
    def passive_star_5(self):
        return super(WildWolf, self).passive_star_5()

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(WildWolf, self).passive_tier_6():
            buff = Buff('WildWolf_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
