from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class CocoaLiqueur(SSRCard):
    def __init__(self):
        super(CocoaLiqueur, self).__init__()
        self.cardId = 'CocoaLiqueur'
        self.round = 2
        self.cardName = '酒心可可'
        self.nickName = '白八/暗八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 7044
        self.lv60s5Atk = 2241
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻100 %
        self.attackMagnification = 1

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

    # 敌受必杀伤 + 27 % (2)
    # 攻204%/238%/273 % [3]
    def skillBefore(self, enemies):
        buff = Buff('CocoaLiqueur_skill', 0.27, 2, BuffType.BeSkillIncrease)
        enemies.buffs.append(buff)

    # 攻100 %
    # 必杀 + 3 % (max 6)
    def attackAfter(self, enemies):
        if self.calBuffCount('CocoaLiqueur_attack') < 6:
            buff = Buff('CocoaLiqueur_attack', 0.03, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def beAttackedAfter(self, seeAsBeAttacked, source):
        super(CocoaLiqueur, self).beAttackedAfter(seeAsBeAttacked, source)
        if seeAsBeAttacked and self.passive_star_3() and self.calBuffCount('CocoaLiqueur_passive_star_3') < 3:
            buff = Buff('CocoaLiqueur_passive_star_3', 0.09, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 被攻击时，攻 + 9 % (max 3)
    def passive_star_3(self):
        return super(CocoaLiqueur, self).passive_star_3()

    # 攻 + 18 %
    # 必杀 + 15 %
    def passive_star_5(self):
        if super(CocoaLiqueur, self).passive_star_5():
            buff = Buff('CocoaLiqueur_passive_star_5', 0.18, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

            buff = Buff('CocoaLiqueur_passive_star_5_2', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀 + 15 %
    def passive_tier_6(self):
        if super(CocoaLiqueur, self).passive_tier_6():
            buff = Buff('CocoaLiqueur_passive_tier_6', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
