from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class DistantPromise(SSRCard):
    def __init__(self):
        super(DistantPromise, self).__init__()
        self.cardId = 'DistantPromise'
        self.cardName = '追逐悠远之约'
        self.nickName = '暗昆/月昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 6617
        self.lv60s5Atk = 2383
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 自伤+40%（2）
    # 攻125%
    # 普攻时追击135%/189%/242%（2）[4]
    def skillBefore(self, enemies):
        buff = Buff('DistantPromise_skill', 0.4, 2, BuffType.DamageIncrease)
        self.addBuff(buff)

    def skill(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 1.25, False, True)
        return damage

    def skillAfter(self, enemies):
        magnification_fu = self.getMagnification(1.35, 1.89, 2.42)
        buff2 = Buff('DistantPromise_skill_2', magnification_fu, 2, BuffType.FollowUpAttack)
        buff2.conditionType = ConditionType.WhenAttack
        buff2.useBaseAtk = False
        buff2.seeAsAttack = True
        self.addBuff(buff2)

    # 攻击力125%造成伤害
    def attack(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 1.25, True, False)
        return damage

    # 队伍攻击每1位，伤+8%(max 3)
    def passive_star_3(self):
        if super(DistantPromise, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('DistantPromise_passive_star_3', 0.08 * count, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 自伤+38%
    def passive_star_5(self):
        if super(DistantPromise, self).passive_star_5():
            buff = Buff('DistantPromise_passive_star_5', 0.38, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 自伤+10%
    def passive_tier_6(self):
        if super(DistantPromise, self).passive_tier_6():
            buff = Buff('DistantPromise_passive_tier_6', 0.1, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)
