from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SalaciousKing(SSRCard):
    def __init__(self):
        super(SalaciousKing, self).__init__()
        self.cardId = 'SalaciousKing'
        self.round = 17
        self.cardName = '深欲暗王'
        self.nickName = '黑伊'
        self.des = ''
        self.tag = ''
        self.role = CardRole.Eiden
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 6973
        self.lv60s5Atk = 2348
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻125%
        self.attackMagnification = 1.25

        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

    def skillBefore(self, enemies):
        buff = Buff('SalaciousKing_skill', 0.34, 3, BuffType.BeDamageIncreaseByOccupation)
        buff.targetOccupation = CardOccupation.Striker
        enemies.addBuff(buff, self)

    def skillAfter(self, enemies):
        if self.star >= 2:
            for role in self.teamMate:
                if role.cardId != self.cardId and role.occupation == CardOccupation.Striker:
                    role.skillCount += 1

    def passive_star_3(self):
        if super(SalaciousKing, self).passive_star_3():
            self.skillCount += 3
            for role in self.teamMate:
                if role.occupation == CardOccupation.Striker:
                    buff = Buff('SalaciousKing_passive_star_3', 0.12, 50, BuffType.AtkIncrease)
                    buff.isPassive = True
                    role.addBuff(buff)

    def passive_star_5(self):
        if super(SalaciousKing, self).passive_star_5():
            strikerCount = 0
            for role in self.teamMate:
                if role.occupation == CardOccupation.Striker:
                    strikerCount += 1

            if strikerCount > 3:
                strikerCount = 3
            if strikerCount > 0:
                for role in self.teamMate:
                    buff = Buff('SalaciousKing_passive_star_5', 0.06 * strikerCount, 50, BuffType.AtkIncrease)
                    buff.isPassive = True
                    role.addBuff(buff)

    def passive_tier_6(self):
        if super(SalaciousKing, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('SalaciousKing_passive_tier_6', 0.02, 50, BuffType.DamageIncrease)
                buff.isPassive = True
                role.addBuff(buff)
                buff2 = Buff('SalaciousKing_passive_tier_6_2', 0.05, 50, BuffType.BeHealIncrease)
                buff2.isPassive = True
                role.addBuff(buff2)
                buff3 = Buff('SalaciousKing_passive_tier_6_3', -0.02, 50, BuffType.BeDamageIncrease)
                buff3.isPassive = True
                role.addBuff(buff3)