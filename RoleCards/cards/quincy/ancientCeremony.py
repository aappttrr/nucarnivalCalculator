from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class AncientCeremony(SSRCard):
    def __init__(self):
        super(AncientCeremony, self).__init__()
        self.cardId = 'AncientCeremony'
        self.cardName = '古老祭祀的赌约'
        self.nickName = '普昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7151
        self.lv60s5Atk = 2205
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 以攻击力125%造成伤害
        self.attackMagnification = 1.25

        # 以攻击力434%/546%/657%
        self.skillMagnificationLv1 = 4.34
        self.skillMagnificationLv2 = 5.46
        self.skillMagnificationLv3 = 6.57

    def skillAfter(self, enemies):
        # 3星被动
        # 攻击时，自身攻击力+5%（最多6层）
        if self.passive_star_3() and self.calBuffCount('AncientCeremony_passive_star_3') < 6:
            buff = Buff('AncientCeremony_passive_star_3', 0.05, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def attackAfter(self, enemies):
        # 3星被动
        # 攻击时，自身攻击力+5%（最多6层）
        if self.passive_star_3() and self.calBuffCount('AncientCeremony_passive_star_3') < 6:
            buff = Buff('AncientCeremony_passive_star_3', 0.05, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击时，自身攻击力+5%（最多6层）
    def passive_star_3(self):
        return super(AncientCeremony, self).passive_star_3()

    # 必杀+33%
    def passive_star_5(self):
        if super(AncientCeremony, self).passive_star_5():
            buff = Buff('AncientCeremony_passive_star_5', 0.33, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(AncientCeremony, self).passive_tier_6():
            buff = Buff('AncientCeremony_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
