from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.tierType import TierType


class SRBlade(SRCard):
    def __init__(self):
        super(SRBlade, self).__init__()
        self.cardId = 'SRBlade'
        self.cardName = '魔人偶'
        self.nickName = 'SR布'
        self.role = CardRole.Blade
        self.type = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.isGroup = True

        self.lv60s5Hp = 6048
        self.lv60s5Atk = 1672
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻142%/173%/203%（群）
    def skill(self, enemy):
        self.skillCount = 0
        magnification = self.getMagnification(1.42, 1.73, 2.03)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)

        return damage

    # 攻63%（群）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 0.63, True, False)

        return damage

    # 队伍布儡每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(SRBlade, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Blade:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SRBlade_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(SRBlade, self).passive_star_5():
            buff = Buff('SRBlade_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_6(self):
        if super(SRBlade, self).passive_tier_6():
            buff = Buff('SRBlade_passive_tier_6', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
