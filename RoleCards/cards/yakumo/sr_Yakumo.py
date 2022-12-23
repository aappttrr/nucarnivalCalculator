from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SRYakumo(SRCard):
    def __init__(self):
        super(SRYakumo, self).__init__()
        self.cardId = 'SRYakumo'
        self.cardName = '隐异之蛇'
        self.nickName = '奶八/SR八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 6155
        self.lv60s5Atk = 1636
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻133%/157%/182%全体治
    # 攻34%/41%/47%全体hot(2)
    def skillHeal(self, enemies, currentAtk):
        ma = self.getMagnification(1.33, 1.57, 1.82)
        ma_hot = self.getMagnification(0.34, 0.41, 0.47)

        heal = currentAtk * ma
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)

        hotHeal = currentAtk * ma_hot
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('SRYakumo_skill', hotHeal, 2, BuffType.Hot)
            role.addBuff(buff, self)

        return heal

    # 攻75%全体治
    def attackHeal(self, enemies, currentAtk):
        heal = currentAtk * 0.75
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)
        return heal

    # 造成回复量+25%
    def passive_star_3(self):
        if super(SRYakumo, self).passive_star_3():
            buff = Buff('SRYakumo_passive_star_3', 0.25, 0, BuffType.HealIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 全体最大HP+6%
    def passive_star_5(self):
        if super(SRYakumo, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('SRYakumo_passive_star_5', 0.06, 0, BuffType.HpIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 攻+10%
    def passive_tier_6(self):
        if super(SRYakumo, self).passive_tier_6():
            buff = Buff('SRYakumo_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
