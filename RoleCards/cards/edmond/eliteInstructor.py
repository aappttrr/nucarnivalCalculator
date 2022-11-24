from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class EliteInstructor(SSRCard):
    def __init__(self):
        super(EliteInstructor, self).__init__()
        self.cardId = 'EliteInstructor'
        self.cardName = '专属指导'
        self.nickName = '教师团'
        self.role = CardRole.Edmond
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 8254
        self.lv60s5Atk = 1992
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 目标获得【被攻击时，自身受伤增加3.5%(3)】(3)
    # 攻204%/238%/273%
    def skill(self, enemy):
        self.skillCount = 0

        buff = Buff('EliteInstructor_skill', 0.035, 3, BuffType.AddBeDamageIncrease)
        buff.addBuffTurn = 3
        buff.conditionType = ConditionType.WhenBeAttacked
        enemy.addBuff(buff, self)

        ma = self.getMagnification(2.04, 2.38, 2.73)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, ma, False, True)

        return damage

    # 攻击力125%造成伤害
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()

        damage = self.calDamage(currentAtk, 1.25, True, False)
        return damage

    # 队伍艾德蒙特每1位，自攻+9%(max 3)
    def passive_star_3(self):
        if super(EliteInstructor, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Edmond:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('EliteInstructor_passive_star_3', 0.09 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 第一回合，必杀技冷却时间减少3回合
    def passive_star_5(self):
        if super(EliteInstructor, self).passive_star_5():
            self.skillCount += 3

    # 攻+10%
    def passive_tier_6(self):
        if super(EliteInstructor, self).passive_tier_6():
            buff = Buff('EliteInstructor_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
