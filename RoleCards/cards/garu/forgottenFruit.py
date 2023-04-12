from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ForgottenFruit(SSRCard):
    def __init__(self):
        super(ForgottenFruit, self).__init__()
        self.cardId = 'ForgottenFruit'
        self.cardName = '遗忘的甜蜜果'
        self.nickName = '盾狼'
        self.role = CardRole.Garu
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 11741
        self.lv60s5Atk = 1387
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力100%
        self.attackMagnification = 1

        self.skillMagnificationLv1 = 0
        self.skillMagnificationLv2 = 0
        self.skillMagnificationLv3 = 0

    # 我方全体受必杀-10%/-13%/-15%（2）
    # 我方全体最大HP13%/15%/18%护盾（1）
    # 嘲讽（1）
    # 防御
    def skill(self, enemies, currentAtk):
        ma = self.getMagnification(-0.1, -0.13, -0.15)
        ma2 = self.getMagnification(0.13, 0.15, 0.18)
        shield = self.maxHp * ma2
        shield = roundDown(shield)
        shield = self.increaseShield(shield)
        shield = self.increaseDamage(shield, False, True)
        for mate in self.teamMate:
            buff1 = Buff('ForgottenFruit_skill', ma, 2, BuffType.BeSkillIncrease)
            mate.addBuff(buff1, self)

            tempShield = mate.increaseBeShield(shield)
            buff2 = Buff('ForgottenFruit_skill_2', tempShield, 1, BuffType.Shield)
            mate.addBuff(buff2, self)
            self.sendShieldEvent(tempShield, mate)
        self.defense = True
        return 0

    def attackAfter(self, enemies):
        self.defense = True

    # 有辅助，最大HP+14%
    # 守护<=1，受伤-5%
    def passive_star_3(self):
        if super(ForgottenFruit, self).passive_star_3():
            count = 0
            hasSupport = False
            for role in self.teamMate:
                if role.occupation == CardOccupation.Support:
                    hasSupport = True
                if role.occupation == CardOccupation.Guardian:
                    count += 1

            if hasSupport:
                buff = Buff('ForgottenFruit_passive_star_3', 0.14, 0, BuffType.HpIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if count <= 1:
                buff = Buff('ForgottenFruit_passive_star_3_2', -0.05, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 我方全体受伤-5%
    def passive_star_5(self):
        if super(ForgottenFruit, self).passive_star_5():
            for mate in self.teamMate:
                buff1 = Buff('ForgottenFruit_passive_star_5', -0.05, 0, BuffType.BeDamageIncrease)
                buff1.isPassive = True
                mate.addBuff(buff1, self)

    # 我方全体受伤-2%
    def passive_tier_6(self):
        for mate in self.teamMate:
            buff1 = Buff('ForgottenFruit_passive_tier_6', -0.02, 0, BuffType.BeDamageIncrease)
            buff1.isPassive = True
            mate.addBuff(buff1, self)
