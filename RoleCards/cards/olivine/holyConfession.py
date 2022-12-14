from Common.nvEventManager import Event, EventType, eventManagerInstance
from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class HolyConfession(SSRCard):
    def __init__(self):
        super(HolyConfession, self).__init__()
        self.cardId = 'HolyConfession'
        self.cardName = '向纯洁象征告解'
        self.nickName = '奶奥'
        self.role = CardRole.Olivine
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Defense
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7934
        self.lv60s5Atk = 1992
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力133%/157%/182%全体治疗
    # 攻击力17%/20%/24%hot(4)
    def skillHeal(self, enemies, currentAtk):
        ma = self.getMagnification(1.33, 1.57, 1.82)
        ma2 = self.getMagnification(0.17, 0.2, 0.24)

        heal = currentAtk * ma
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)

        hotHeal = currentAtk * ma2
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('HolyConfession_skill', hotHeal, 4, BuffType.Hot)
            role.addBuff(buff, self)

        if self.passive_star_3():
            hpLowestRole = self
            for role in self.teamMate:
                if role.hpCurrent < hpLowestRole.hpCurrent:
                    hpLowestRole = role

            heal = currentAtk * 0.75
            heal = roundDown(heal)
            heal = self.increaseHeal(heal)
            heal2 = hpLowestRole.increaseBeHeal(heal)

            event = Event(EventType.skillHeal)
            event.data['source'] = self
            event.data['value'] = heal2
            event.data['target'] = hpLowestRole
            eventManagerInstance.sendEvent(event)
        return heal


    # 攻击力25%hot(3)
    def attackHeal(self, enemies, currentAtk):
        hotHeal = currentAtk * 0.25
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        for role in self.teamMate:
            buff = Buff('HolyConfession_attack', hotHeal, 3, BuffType.Hot)
            role.addBuff(buff, self)

        if self.passive_star_3():
            hpLowestRole = self
            for role in self.teamMate:
                if role.hpCurrent < hpLowestRole.hpCurrent:
                    hpLowestRole = role

            heal = currentAtk * 0.75
            heal = roundDown(heal)
            heal = self.increaseHeal(heal)
            heal2 = hpLowestRole.increaseBeHeal(heal)

            event = Event(EventType.attackHeal)
            event.data['source'] = self
            event.data['value'] = heal2
            event.data['target'] = hpLowestRole
            eventManagerInstance.sendEvent(event)
        return 0

    # 攻击时，以攻击力75%对Hp最低者进行治疗
    def passive_star_3(self):
        return super(HolyConfession, self).passive_star_3()

    # 攻击力+25%
    def passive_star_5(self):
        if super(HolyConfession, self).passive_star_5():
            buff = Buff('HolyConfession_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(HolyConfession, self).passive_tier_6():
            buff = Buff('HolyConfession_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
