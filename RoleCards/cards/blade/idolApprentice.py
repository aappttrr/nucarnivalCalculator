from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class IdolApprentice(SSRCard):
    def __init__(self):
        super(IdolApprentice, self).__init__()
        self.cardId = 'IdolApprentice'
        self.round = 5
        self.cardName = '偶像实习'
        self.nickName = '夏布'
        self.role = CardRole.Blade
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 6973
        self.lv60s5Atk = 2241
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        self.isAttackGroup = True
        self.isSkillGroup = True

        # 攻击力40%（群）
        self.attackMagnification = 0.4

        # 攻击力50%（群）
        self.skillMagnificationLv1 = 0.5
        self.skillMagnificationLv2 = 0.5
        self.skillMagnificationLv3 = 0.5

    # 攻击力50%（群）
    # 被攻击时，攻击力49%/65%/81%（群）反击（2）
    # 嘲讽（1），被攻击时解除嘲讽（1）
    def skillAfter(self, enemies):
        ma = self.getMagnification(0.48, 0.65, 0.81)
        buff = Buff('IdolApprentice_skill', ma, 2, BuffType.CounterAttack)
        buff.conditionType = ConditionType.WhenBeAttacked
        buff.isGroup = True
        buff.useBaseAtk = False
        buff.seeAsSkill = True
        self.addBuff(buff)

        buff2 = Buff('IdolApprentice_skill_2', 0, 1, BuffType.Taunt)
        self.addBuff(buff2)

        buff3 = Buff('IdolApprentice_skill_3', 0, 1, BuffType.DisTaunt)
        buff3.conditionType = ConditionType.WhenBeAttacked
        self.addBuff(buff3)

    # 攻击力40%（群）
    # 被攻击时，攻击力23%（群）造成伤害（1）
    # 嘲讽（1），被攻击时解除嘲讽（1）
    def attackAfter(self, enemies):
        buff = Buff('IdolApprentice_attack', 0.23, 1, BuffType.CounterAttack)
        buff.conditionType = ConditionType.WhenBeAttacked
        buff.isGroup = True
        buff.useBaseAtk = False
        buff.seeAsSkill = True
        self.addBuff(buff)

        buff2 = Buff('IdolApprentice_attack_2', 0, 1, BuffType.Taunt)
        self.addBuff(buff2)

        buff3 = Buff('IdolApprentice_attack_3', 0, 1, BuffType.DisTaunt)
        buff3.conditionType = ConditionType.WhenBeAttacked
        self.addBuff(buff3)

    # 八云在场，造成伤害+9%
    # 奥利文在场，攻击力+14%
    def passive_star_3(self):
        if super(IdolApprentice, self).passive_star_3():
            hasYakumo = False
            hasOlivine = False
            for role in self.teamMate:
                if role.role == CardRole.Yakumo:
                    hasYakumo = True
                elif role.role == CardRole.Olivine:
                    hasOlivine = True

            if hasYakumo:
                buff = Buff('IdolApprentice_passive_star_3', 0.09, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)
            if hasOlivine:
                buff = Buff('IdolApprentice_passive_star_3_2', 0.14, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(IdolApprentice, self).passive_star_5():
            buff = Buff('IdolApprentice_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(IdolApprentice, self).passive_tier_6():
            buff = Buff('IdolApprentice_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
