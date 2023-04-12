from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class CrystalAwakening(SSRCard):
    def __init__(self):
        super(CrystalAwakening, self).__init__()
        self.cardId = 'CrystalAwakening'
        self.cardName = '觉醒的晶莹花'
        self.nickName = '火布'
        self.role = CardRole.Blade
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7044
        self.lv60s5Atk = 2348
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻50%
        self.attackMagnification = 0.5

        self.skillMagnificationLv1 = 0.6 * 3 + 2.84
        self.skillMagnificationLv2 = 0.6 * 3 + 3.45
        self.skillMagnificationLv3 = 0.6 * 3 + 4.06

    # 目标解除防御
    # 攻60%攻击3次
    # 攻284%/345%/406%
    def skillBefore(self, enemies):
        enemies.defense = False

    # 目标解除防御
    # 攻50%
    # 受伤减少5%（4）
    def attackBefore(self, enemies):
        enemies.defense = False

    def attackAfter(self, enemies):
        buff = Buff('CrystalAwakening_attack', -0.05, 4, BuffType.BeDamageIncrease)
        self.addBuff(buff)

    # 3星被动，被治疗时，攻击力+9%（max 3）
    def beHealed(self, heal, seeAsHeal):
        super(CrystalAwakening, self).beHealed(heal, seeAsHeal)
        if seeAsHeal and self.passive_star_3() and self.calBuffCount('CrystalAwakening_passive_star_3') < 3:
            buff = Buff('CrystalAwakening_passive_star_3', 0.09, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+25%
    # 队伍有守护，必杀+25%
    def passive_star_5(self):
        if super(CrystalAwakening, self).passive_star_5():
            buff1 = Buff('CrystalAwakening_passive_star_5', 0.25, 0, BuffType.SkillIncrease)
            buff1.isPassive = True
            self.addBuff(buff1)

            hasGuardian = False
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Guardian:
                    hasGuardian = True
                    break

            if hasGuardian:
                buff2 = Buff('CrystalAwakening_passive_star_5_2', 0.25, 0, BuffType.SkillIncrease)
                buff2.isPassive = True
                self.addBuff(buff2)

    # 攻10%
    def passive_tier_6(self):
        buff = Buff('CrystalAwakening_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
        buff.isPassive = True
        self.addBuff(buff)
