from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.nCard import NCard
from RoleCards.common.rCard import RCard
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class NYakumo(NCard):
    def __init__(self):
        super(NYakumo, self).__init__()
        self.cardId = 'NYakumo'
        self.cardName = '弱气青年'
        self.nickName = 'N八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Healer
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 4554
        self.lv60s5Atk = 1138
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻133%/157%/182%全体治
    # 攻34%/41%/47%全体hot(2)
    def skillHeal(self, enemy):
        self.skillCount = 0
        ma = self.getMagnification(1.33, 1.57, 1.82)
        ma_hot = self.getMagnification(0.34, 0.41, 0.47)
        currentAtk = self.getCurrentAtk()

        heal = currentAtk * ma
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        for role in self.teamMate:
            buff = Buff('NYakumo_skill', hotHeal, 2, BuffType.Hot)
            role.addBuff(buff, self)
        return heal

    # 攻75%全体治
    def attackHeal(self, enemy):
        currentAtk = self.getCurrentAtk()

        heal = currentAtk * 0.75
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)
        return heal

    # 造成回复量+25%
    def passive_star_3(self):
        if super(NYakumo, self).passive_star_3():
            buff = Buff('NYakumo_passive_star_3', 0.25, 0, BuffType.HealIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 全体最大HP+6%
    def passive_star_5(self):
        if super(NYakumo, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('NYakumo_passive_star_5', 0.06, 0, BuffType.HpIncrease)
                buff.isPassive = True
                role.addBuff(buff,self)

    # 攻+10%
    def passive_tier_3(self):
        if super(NYakumo, self).passive_tier_3():
            buff = Buff('NYakumo_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
