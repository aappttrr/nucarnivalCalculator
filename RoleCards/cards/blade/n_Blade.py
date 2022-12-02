from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class NBlade(NCard):
    def __init__(self):
        super(NBlade, self).__init__()
        self.cardId = 'NBlade'
        self.cardName = '纯真傀儡'
        self.nickName = 'N布'
        self.role = CardRole.Blade
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Striker
        self.skillCD = 4
        self.isGroup = True
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 4447
        self.lv60s5Atk = 1174
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻142%/173%/203%（群）
    def skill(self, enemy):
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
        if super(NBlade, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Blade:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NBlade_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(NBlade, self).passive_star_5():
            buff = Buff('NBlade_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_3(self):
        if super(NBlade, self).passive_tier_3():
            buff = Buff('NBlade_passive_tier_3', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
