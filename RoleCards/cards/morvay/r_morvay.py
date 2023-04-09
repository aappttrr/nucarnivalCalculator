from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RMorvay(RCard):
    def __init__(self):
        super(RMorvay, self).__init__()
        self.cardId = 'RMorvay'
        self.cardName = '淫魔'
        self.nickName = 'R墨'
        self.role = CardRole.Morvay
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Guardian
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 8147
        self.lv60s5Atk = 889
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻100 %
        self.attackMagnification = 1

        # 攻100 %
        self.skillMagnificationLv1 = 1
        self.skillMagnificationLv2 = 1
        self.skillMagnificationLv3 = 1

    # 攻100%
    # 最大HP20%/30%/40%护盾（1），防御减伤+10%（1），嘲讽（1），转防御
    def skillAfter(self, enemies):
        ma = self.getMagnification(0.2, 0.3, 0.4)
        shield = self.maxHp * ma
        shield = roundDown(shield)
        shield = self.increaseShield(shield)

        buff = Buff('RMorvay_skill', shield, 1, BuffType.Shield)
        self.addBuff(buff)
        self.sendShieldEvent(shield, self)

        buff2 = Buff('RMorvay_skill_2', 0.1, 1, BuffType.DefenseDamageReduction)
        self.addBuff(buff2)

        buff3 = Buff('RMorvay_skill_3', 0, 1, BuffType.Taunt)
        self.addBuff(buff3)

        self.defense = True

    # 攻100%，转防御
    def attackAfter(self, enemies):
        self.defense = True

    # 有艾斯特，最大HP+13%
    # 守护<=1，受伤-10%
    def passive_star_3(self):
        if super(RMorvay, self).passive_star_3():
            count = 0
            hasAster = False
            for role in self.teamMate:
                if role.role == CardRole.Aster:
                    hasAster = True
                if role.occupation == CardOccupation.Guardian:
                    count += 1

            if hasAster:
                buff = Buff('RMorvay_passive_star_3', 0.13, 0, BuffType.HpIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if count <= 1:
                buff = Buff('RMorvay_passive_star_3_2', -0.1, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 受伤-10%
    def passive_star_5(self):
        if super(RMorvay, self).passive_star_5():
            buff = Buff('RMorvay_passive_star_5', -0.1, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 受回复量+20%
    def passive_tier_3(self):
        if super(RMorvay, self).passive_tier_3():
            buff = Buff('RMorvay_passive_tier_3', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
