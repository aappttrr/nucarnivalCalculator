from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RainyRebirth(SSRCard):
    def __init__(self):
        super(RainyRebirth, self).__init__()
        self.cardId = 'RainyRebirth'
        self.round = 15
        self.cardName = '雨季终时的新生'
        self.nickName = '伞敛'
        self.role = CardRole.Rei
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 11207
        self.lv60s5Atk = 1458
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻100%
        self.attackMagnification = 1

        # 攻100%
        self.skillMagnificationLv1 = 1
        self.skillMagnificationLv2 = 1
        self.skillMagnificationLv3 = 1

    # 攻100%
    # 最大HP30%/40%护盾（1）
    # 反击129%/173%/216%（1）
    # 被攻击时，解除反击
    # 嘲讽（1），转防御
    def skillAfter(self, enemies):
        if self.star >= 2:
            ma = self.getMagnification(0, 0.3, 0.4)
            shield = self.maxHp * ma
            shield = roundDown(shield)
            shield = self.increaseShield(shield)

            buff = Buff('RainyRebirth_skill', shield, 1, BuffType.Shield)
            self.addBuff(buff)
            self.sendShieldEvent(shield, self)

        ma2 = self.getMagnification(1.29, 1.73, 2.16)
        buff2 = Buff('RainyRebirth_skill_2', ma2, 1, BuffType.CounterAttack)
        buff2.conditionType = ConditionType.WhenBeAttacked
        buff2.useBaseAtk = False
        buff2.seeAsSkill = True
        self.addBuff(buff2)

        buff3 = Buff('RainyRebirth_skill_3', 0, 1, BuffType.DisTaunt)
        buff3.conditionType = ConditionType.WhenBeAttacked
        self.addBuff(buff3)

        buff4 = Buff('RainyRebirth_skill_4', 0, 1, BuffType.Taunt)
        self.addBuff(buff4)

        self.defense = True

    def attackAfter(self, enemies):
        self.defense = True

    # 最大HP + 18 %
    # 攻 + 18 %
    def passive_star_3(self):
        if super(RainyRebirth, self).passive_star_3():
            buff = Buff("RainyRebirth_passive_star_3", 0.18, 0, BuffType.HpIncrease)
            buff.isPassive = True
            self.addBuff(buff)

            buff2 = Buff("RainyRebirth_passive_star_3_2", 0.18, 0, BuffType.AtkIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)

    # 敛each，自身受伤害-4%，自身造成伤害+9%（max3）
    def passive_star_5(self):
        if super(RainyRebirth, self).passive_star_5():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Rei:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff("RainyRebirth_passive_star_5", -0.04 * count, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)
                buff2 = Buff("RainyRebirth_passive_star_5_2", 0.09 * count, 0, BuffType.DamageIncrease)
                buff2.isPassive = True
                self.addBuff(buff2)

    # 受回复量+20%
    def passive_tier_6(self):
        if super(RainyRebirth, self).passive_tier_6():
            buff = Buff('RainyRebirth_passive_tier_6', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
