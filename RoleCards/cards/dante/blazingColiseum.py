from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class BlazingColiseum(SSRCard):
    def __init__(self):
        super(BlazingColiseum, self).__init__()
        self.cardId = 'BlazingColiseum'
        self.cardName = '赛兽场上的暖阳'
        self.nickName = '普啖'
        self.role = CardRole.Dante
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 11314
        self.lv60s5Atk = 1387
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力100%
    # 最大hp13%/15%/18%护盾(1)
    def skill(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 1, False, True)
        return damage

    def skillAfter(self, enemies):
        ma = self.getMagnification(0.13, 0.15, 0.18)
        shield = self.maxHp * ma
        shield = roundDown(shield)
        shield = self.increaseShield(shield)
        shield = self.increaseDamage(shield, False, True)

        for role in self.teamMate:
            tempShield = role.increaseBeShield(shield)
            buff = Buff('BlazingColiseum_skill', tempShield, 1, BuffType.Shield)
            role.addBuff(buff, self)
            self.sendShieldEvent(tempShield, role)

    # 攻击力75%
    # 最大hp6%护盾(1)
    def attack(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 0.75, True, False)
        return damage

    def attackAfter(self, enemies):
        shield = self.maxHp * 0.06
        shield = roundDown(shield)
        shield = self.increaseShield(shield)
        shield = self.increaseDamage(shield, True, False)

        for role in self.teamMate:
            tempShield = role.increaseBeShield(shield)
            buff = Buff('BlazingColiseum_attack', tempShield, 1, BuffType.Shield)
            role.addBuff(buff, self)
            self.sendShieldEvent(tempShield, role)

    # 队伍啖天每1位，护盾效果+8%(max 3)
    def passive_star_3(self):
        if super(BlazingColiseum, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Dante:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('BlazingColiseum_passive_star_3', 0.08 * count, 0, BuffType.ShieldEffectIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 受伤-4%
    def passive_star_5(self):
        if super(BlazingColiseum, self).passive_star_5():
            buff = Buff('BlazingColiseum_passive_star_5', -0.04, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 受伤-2%
    def passive_tier_6(self):
        if super(BlazingColiseum, self).passive_tier_6():
            buff = Buff('BlazingColiseum_passive_tier_6', -0.02, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)
