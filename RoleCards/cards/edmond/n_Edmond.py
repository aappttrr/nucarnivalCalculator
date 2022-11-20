from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class NEdmond(NCard):
    def __init__(self):
        super(NEdmond, self).__init__()
        self.cardId = 'NEdmond'
        self.cardName = '贵族青年'
        self.nickName = 'N团'
        self.role = CardRole.Edmond
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 4305
        self.lv60s5Atk = 1209
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻229%/273%/316%
    def skill(self, enemy):
        self.skillCount = 0
        magnification = self.getMagnification(2.29, 2.73, 3.16)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)

        return damage

    # 攻125%
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1.25, True, False)

        return damage

    # 队伍艾德蒙特每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(NEdmond, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Edmond:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NEdmond_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(NEdmond, self).passive_star_5():
            buff = Buff('NEdmond_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(NEdmond, self).passive_tier_3():
            buff = Buff('NEdmond_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
