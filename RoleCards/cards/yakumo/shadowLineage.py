from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ShadowLineage(SSRCard):
    def __init__(self):
        super(ShadowLineage, self).__init__()
        self.cardId = 'ShadowLineage'
        self.round = 18
        self.cardName = '黔云之血脉'
        self.nickName = '烟八/烟云'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 6795
        self.lv60s5Atk = 2419
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力125%
        self.attackMagnification = 1.25

        # 攻击力360%/447%/533%
        self.skillMagnificationLv1 = 3.6
        self.skillMagnificationLv2 = 4.47
        self.skillMagnificationLv3 = 5.33

    # 攻击力增加27%/54%/54%（4）
    # 攻击力360%/447%/533%
    # 自身dot，最大HP5%(4)
    def skillBefore(self, enemies):
        ma = self.getMagnification(0.27, 0.54, 0.54)
        buff = Buff('ShadowLineage_skill', ma, 4, BuffType.AtkIncrease)
        self.addBuff(buff)

    def skillAfter(self, enemies):
        dotDamage = self.maxHp * 0.05
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('ShadowLineage_skill2', dotDamage, 4, BuffType.Dot)
        # self.addBuff(buff)

    # 辅助 > 1，造成伤害增加18%
    # 治疗 > 1，造成伤害增加18%
    def passive_star_3(self):
        if super(ShadowLineage, self).passive_star_3():
            hasSupport = False
            hasHealer = False
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Support:
                    hasSupport = True
                if mate.occupation == CardOccupation.Healer:
                    hasHealer = True

            if hasSupport:
                buff = Buff('ShadowLineage_passive_star_3', 0.18, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)
            if hasHealer:
                buff2 = Buff('ShadowLineage_passive_star_3_2', 0.18, 0, BuffType.DamageIncrease)
                buff2.isPassive = True
                self.addBuff(buff2)

    # 造成伤害增加27%
    def passive_star_5(self):
        if super(ShadowLineage, self).passive_star_5():
            buff = Buff('ShadowLineage_passive_star_5', 0.27, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 造成伤害增加10%
    def passive_tier_6(self):
        if super(ShadowLineage, self).passive_tier_6():
            buff = Buff('ShadowLineage_passive_tier_6', 0.1, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)
