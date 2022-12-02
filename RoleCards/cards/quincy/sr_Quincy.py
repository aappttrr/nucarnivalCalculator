from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SRQuincy(SRCard):
    def __init__(self):
        super(SRQuincy, self).__init__()
        self.cardId = 'SRQuincy'
        self.cardName = '古森守护者'
        self.nickName = 'SR昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5728
        self.lv60s5Atk = 1743
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 目标解除防御，攻409%/513%/616%
    def skill(self, enemy):
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
        buff = Buff('SRQuincy_attack', 0.05, 6, BuffType.AtkIncrease)
        self.addBuff(buff)

    # 队伍昆西每1位，必杀+12%(max 3)
    def passive_star_3(self):
        if super(SRQuincy, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Quincy:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SRQuincy_passive_star_3', 0.12 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(SRQuincy, self).passive_star_5():
            buff = Buff('SRQuincy_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_6(self):
        if super(SRQuincy, self).passive_tier_6():
            buff = Buff('SRQuincy_passive_tier_6', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
