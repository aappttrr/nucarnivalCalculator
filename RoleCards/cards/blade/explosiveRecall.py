from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ExplosiveRecall(SSRCard):
    def __init__(self):
        super(ExplosiveRecall, self).__init__()
        self.cardId = 'ExplosiveRecall'
        self.cardName = '战斗人偶与回忆'
        self.nickName = '普布'
        self.role = CardRole.Blade
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 6937
        self.lv60s5Atk = 2277
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 伤+12.5%(max 2)
    # 攻204%/238%/273%
    def skillBefore(self, enemies):
        if self.calBuffCount('ExplosiveRecall_skill') < 2:
            buff = Buff('ExplosiveRecall_skill', 0.125, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(2.04, 2.38, 2.73)
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    # 攻125%
    def attack(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 1.25, True, False)
        return damage

    # 队伍布儡每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(ExplosiveRecall, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Blade:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('ExplosiveRecall_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻击力增加25%（被动）
    def passive_star_5(self):
        if super(ExplosiveRecall, self).passive_star_5():
            buff = Buff('ExplosiveRecall_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(ExplosiveRecall, self).passive_tier_6():
            buff = Buff('ExplosiveRecall_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
