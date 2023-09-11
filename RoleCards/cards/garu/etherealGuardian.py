from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class EtherealGuardian(SSRCard):
    def __init__(self):
        super(EtherealGuardian, self).__init__()
        self.cardId = 'EtherealGuardian'
        self.round = 18
        self.cardName = '缥缈之守候'
        self.nickName = '烟狼'
        self.role = CardRole.Garu
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7115
        self.lv60s5Atk = 2312
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力
        self.attackHealMagnification = 0.25

        # 攻击力
        self.skillHealMagnificationLv1 = 1
        self.skillHealMagnificationLv2 = 1
        self.skillHealMagnificationLv3 = 1

    # 以攻击力100%治疗
    # 以攻击力34%/47%/59%持续治疗（3）
    # 除自身以外，全体普攻伤害+27%（3）[lv2]
    def skillHeal(self, enemies, currentAtk):
        heal = super(EtherealGuardian, self).skillHeal(enemies, currentAtk)
        ma_hot = self.getMagnification(0.34, 0.47, 0.59)

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('EtherealGuardian_skill', hotHeal, 3, BuffType.Hot)
            role.addBuff(buff, self)

            if role.cardId != self.cardId and self.star >= 2:
                buff2 = Buff('EtherealGuardian_skill2', 0.27, 3, BuffType.AttackIncrease)
                role.addBuff(buff2, self)

        return heal

    # 攻击力25%治疗
    # 攻击力25%持续治疗
    def attackHeal(self, enemies, currentAtk):
        heal = super(EtherealGuardian, self).attackHeal(enemies, currentAtk)
        ma_hot = 0.25

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('EtherealGuardian_attack', hotHeal, 2, BuffType.Hot)
            role.addBuff(buff, self)

        return heal

    # 全体攻击力+9%
    # 全体攻击定位，普攻+23%
    def passive_star_3(self):
        if super(EtherealGuardian, self).passive_star_3():
            for role in self.teamMate:
                buff = Buff('EtherealGuardian_passive_star_3', 0.09, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

                if role.occupation == CardOccupation.Striker:
                    buff2 = Buff('EtherealGuardian_passive_star_3_2', 0.23, 0, BuffType.AttackIncrease)
                    buff2.isPassive = True
                    role.addBuff(buff2, self)

    # 造成回复量+27%
    # 造成持续回复量+27%
    def passive_star_5(self):
        if super(EtherealGuardian, self).passive_star_5():
            buff = Buff('EtherealGuardian_passive_star_5', 0.27, 0, BuffType.HealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
            buff2 = Buff('EtherealGuardian_passive_star_5_2', 0.27, 0, BuffType.HotIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)

    # 攻+10%
    def passive_tier_6(self):
        if super(EtherealGuardian, self).passive_tier_6():
            buff = Buff('EtherealGuardian_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
