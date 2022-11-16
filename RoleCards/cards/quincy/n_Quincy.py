from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.common.rCard import RCard
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.tierType import TierType


class NQuincy(NCard):
    def __init__(self):
        super(NQuincy, self).__init__()
        self.cardId = 'NQuincy'
        self.cardName = '边境者'
        self.nickName = 'N昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.skillCD = 6

        self.lv60s5Hp = 4127
        self.lv60s5Atk = 1245
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 目标解除防御，攻409%/513%/616%
    def skill(self, enemy):
        self.skillCount = 0
        enemy.defense = False

        magnification = self.getMagnification(4.09, 5.13, 6.16)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)

        return damage

    # 攻100%，攻+5%（6）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)

        return damage

    def attackAfter(self, enemy):
        buff = Buff('NQuincy_attack', 0.05, 6, BuffType.AtkIncrease)
        self.addBuff(buff)

    # 队伍昆西每1位，必杀+12%(max 3)
    def passive_star_3(self):
        if super(NQuincy, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Quincy:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NQuincy_passive_star_3', 0.12 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(NQuincy, self).passive_star_5():
            buff = Buff('NQuincy_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_3(self):
        if super(NQuincy, self).passive_tier_3():
            buff = Buff('NQuincy_passive_tier_3', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
