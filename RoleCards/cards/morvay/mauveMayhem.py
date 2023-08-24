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


class MauveMayhem(SSRCard):
    def __init__(self):
        super(MauveMayhem, self).__init__()
        self.cardId = 'MauveMayhem'
        self.round = 17
        self.cardName = '狂傲紫魅'
        self.nickName = '大墨'
        self.role = CardRole.Morvay
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 6902
        self.lv60s5Atk = 2383
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻击力125%对目标造成伤害
        self.attackMagnification = 1.25

        # 攻击力245%/299%/354%对目标造成伤害
        self.skillMagnificationLv1 = 2.45
        self.skillMagnificationLv2 = 2.99
        self.skillMagnificationLv3 = 3.54

    # 最大HP20%自身护盾（2）(lv2)
    # 以攻击力245%/299%/354%造成伤害
    # 获得 反击 攻61%/75%/89%（2）
    # 嘲讽（1）
    # 被攻击时，解除嘲讽（1）
    def skillBefore(self, enemies):
        if self.star >= 2:
            shield = self.maxHp * 0.2
            shield = roundDown(shield)
            shield = self.increaseShield(shield)
            buff = Buff('MauveMayhem_skill', shield, 2, BuffType.Shield)
            self.addBuff(buff)
            self.sendShieldEvent(shield, self)

    def skillAfter(self, enemies):
        ma = self.getMagnification(0.61, 0.75, 0.89)
        buff = Buff('MauveMayhem_skill_2', ma, 2, BuffType.CounterAttack)
        buff.conditionType = ConditionType.WhenBeAttacked
        buff.useBaseAtk = False
        buff.seeAsSkill = True
        self.addBuff(buff)

        buff2 = Buff('MauveMayhem_skill_3', 0, 1, BuffType.Taunt)
        self.addBuff(buff2)

        buff3 = Buff('MauveMayhem_skill_4', 0, 1, BuffType.DisTaunt)
        buff3.conditionType = ConditionType.WhenBeAttacked
        self.addBuff(buff3)

    # 队友有辅助，攻+18%
    # 队友有艾斯特，攻+18%
    def passive_star_3(self):
        if super(MauveMayhem, self).passive_star_3():
            hasAster = False
            hasSupport = False
            for role in self.teamMate:
                if role.role == CardRole.Aster:
                    hasAster = True
                if role.occupation == CardOccupation.Support:
                    hasSupport = True
            if hasSupport:
                buff = Buff('MauveMayhem_passive_star_3', 0.18, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if hasAster:
                buff2 = Buff('MauveMayhem_passive_star_3_2', 0.18, 0, BuffType.AtkIncrease)
                buff2.isPassive = True
                self.addBuff(buff2)

    # 必杀伤害增加38%
    def passive_star_5(self):
        if super(MauveMayhem, self).passive_star_5():
            buff = Buff('MauveMayhem_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀伤害增加15%
    def passive_tier_6(self):
        if super(MauveMayhem, self).passive_tier_6():
            buff = Buff('MauveMayhem_passive_tier_6', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
