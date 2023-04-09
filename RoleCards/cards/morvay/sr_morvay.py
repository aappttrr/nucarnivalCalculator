from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SRMorvay(SRCard):
    def __init__(self):
        super(SRMorvay, self).__init__()
        self.cardId = 'SRMorvay'
        self.cardName = '使魔-墨菲'
        self.nickName = 'SR墨'
        self.role = CardRole.Morvay
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 9606
        self.lv60s5Atk = 1031
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

        buff = Buff('SRMorvay_skill', shield, 1, BuffType.Shield)
        self.addBuff(buff)
        self.sendShieldEvent(shield, self)

        buff2 = Buff('SRMorvay_skill_2', 0.1, 1, BuffType.DefenseDamageReduction)
        self.addBuff(buff2)

        buff3 = Buff('SRMorvay_skill_3', 0, 1, BuffType.Taunt)
        self.addBuff(buff3)

        self.defense = True

    # 攻100%，转防御
    def attackAfter(self, enemies):
        self.defense = True

    # 有艾斯特，最大HP+13%
    # 守护<=1，受伤-10%
    def passive_star_3(self):
        if super(SRMorvay, self).passive_star_3():
            count = 0
            hasAster = False
            for role in self.teamMate:
                if role.role == CardRole.Aster:
                    hasAster = True
                if role.occupation == CardOccupation.Guardian:
                    count += 1

            if hasAster:
                buff = Buff('SRMorvay_passive_star_3', 0.13, 0, BuffType.HpIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if count <= 1:
                buff = Buff('SRMorvay_passive_star_3_2', -0.1, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 受伤-10%
    def passive_star_5(self):
        if super(SRMorvay, self).passive_star_5():
            buff = Buff('SRMorvay_passive_star_5', -0.1, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 受回复量+20%
    def passive_tier_6(self):
        if super(SRMorvay, self).passive_tier_6():
            buff = Buff('SRMorvay_passive_tier_6', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
