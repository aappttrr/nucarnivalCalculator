from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ScarletFinesse(SSRCard):
    def __init__(self):
        super(ScarletFinesse, self).__init__()
        self.cardId = 'ScarletFinesse'
        self.round = 17
        self.cardName = '冷艳猩红'
        self.nickName = '大艾'
        self.role = CardRole.Aster
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 7009
        self.lv60s5Atk = 2348
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻击力125%对目标造成伤害
        self.attackMagnification = 1.25

        # 攻击力269%/325%/382%对目标造成伤害
        self.skillMagnificationLv1 = 2.69
        self.skillMagnificationLv2 = 3.25
        self.skillMagnificationLv3 = 3.82

    # 吸血50%（1）
    # 以攻击力 269%/325%/382%造成伤害
    # 目标造成伤伤害减少15%（2）(lv2)
    # 100%机率 睡眠（2）(lv2)
    def skillBefore(self, enemies):
        buff = Buff('ScarletFinesse_skill', 0.5, 1, BuffType.BloodSucking)
        self.addBuff(buff)

    def skillAfter(self, enemies):
        if self.star >= 2:
            buff = Buff('ScarletFinesse_skill_2', -0.15, 2, BuffType.DamageIncrease)
            enemies.addBuff(buff, self)

    # 吸血25%（1）
    def attackBefore(self, enemies):
        buff = Buff('ScarletFinesse_attack', 0.25, 1, BuffType.BloodSucking)
        self.addBuff(buff)

    # 队友有辅助，攻+18%
    # 队友有墨菲，攻+18%
    def passive_star_3(self):
        if super(ScarletFinesse, self).passive_star_3():
            hasMorvay = False
            hasSupport = False
            for role in self.teamMate:
                if role.role == CardRole.Morvay:
                    hasMorvay = True
                if role.occupation == CardOccupation.Support:
                    hasSupport = True
            if hasSupport:
                buff = Buff('ScarletFinesse_passive_star_3', 0.18, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if hasMorvay:
                buff2 = Buff('ScarletFinesse_passive_star_3_2', 0.18, 0, BuffType.AtkIncrease)
                buff2.isPassive = True
                self.addBuff(buff2)

    # 攻击力增加25%
    def passive_star_5(self):
        if super(ScarletFinesse, self).passive_star_5():
            buff = Buff('ScarletFinesse_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%
    def passive_tier_6(self):
        if super(ScarletFinesse, self).passive_tier_6():
            buff = Buff('ScarletFinesse_passive_tier_6', 0.10, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
