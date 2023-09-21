from Common.ncRound import roundDown
from Common.nvEventManager import Event, EventType, eventManagerInstance
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class BlossomingLegend(SSRCard):
    def __init__(self):
        super(BlossomingLegend, self).__init__()
        self.cardId = 'BlossomingLegend'
        self.round = 15
        self.cardName = '花期尽头的故闻'
        self.nickName = '伞昆'
        self.des = '带必杀增益的治疗，没有hot，但总体治疗量很高，适合各种队伍，建议2星'
        self.role = CardRole.Quincy
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Healer
        self.tierType = TierType.Defense
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7400
        self.lv60s5Atk = 2241
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻75%全体治
        self.attackHealMagnification = 0.75

        # 攻150%全体治
        self.skillHealMagnificationLv1 = 1.5
        self.skillHealMagnificationLv2 = 1.5
        self.skillHealMagnificationLv3 = 1.5

    # 除自身必杀伤害+37.5%（1）（lv2）
    # 攻150%全体治疗
    # 自身普攻伤害+50%/70%/90%（3）
    def skillBefore(self, enemies):
        if self.star >= 2:
            for mate in self.teamMate:
                if mate == self:
                    continue
                buff = Buff("BlossomingLegend_skill", 0.375, 1, BuffType.SkillIncrease)
                mate.addBuff(buff, self)

    def skillAfter(self, enemies):
        ma = self.getMagnification(0.5, 0.7, 0.9)

        buff = Buff("BlossomingLegend_skill_2", ma, 3, BuffType.AttackIncrease)
        self.addBuff(buff)

        if self.star >= 3:
            currentAtk = self.getCurrentAtk()
            hpLowestRole = self
            for role in self.teamMate:
                if role.hpCurrent < hpLowestRole.hpCurrent:
                    hpLowestRole = role

            heal2 = currentAtk * 0.75
            heal2 = roundDown(heal2)
            heal2 = self.increaseHeal(heal2, False, True)
            heal2 = hpLowestRole.increaseBeHeal(heal2)

            event = Event(EventType.skillHeal)
            event.data['source'] = self
            event.data['value'] = heal2
            event.data['target'] = hpLowestRole
            eventManagerInstance.sendEvent(event)

    def attackAfter(self, enemies):
        if self.star >= 3:
            currentAtk = self.getCurrentAtk()
            hpLowestRole = self
            for role in self.teamMate:
                if role.hpCurrent < hpLowestRole.hpCurrent:
                    hpLowestRole = role

            heal2 = currentAtk * 0.75
            heal2 = roundDown(heal2)
            heal2 = self.increaseHeal(heal2, False, True)
            heal2 = hpLowestRole.increaseBeHeal(heal2)

            event = Event(EventType.attackHeal)
            event.data['source'] = self
            event.data['value'] = heal2
            event.data['target'] = hpLowestRole
            eventManagerInstance.sendEvent(event)

    # 攻+18%
    # 攻击时，攻75%对HP最低者进行治疗
    def passive_star_3(self):
        if super(BlossomingLegend, self).passive_star_3():
            buff = Buff("BlossomingLegend_passive_star_3",0.18,0,BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 全体最大HP+12%
    def passive_star_5(self):
        if super(BlossomingLegend, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('BlossomingLegend_passive_star_5', 0.12, 0, BuffType.HpIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 攻+10%
    def passive_tier_6(self):
        if super(BlossomingLegend, self).passive_tier_6():
            buff = Buff("BlossomingLegend_passive_tier_6",0.1,0,BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)