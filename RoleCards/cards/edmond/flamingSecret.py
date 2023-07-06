from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class FlamingSecret(SSRCard):
    def __init__(self):
        super(FlamingSecret, self).__init__()
        self.cardId = 'FlamingSecret'
        self.round = 16
        self.cardName = '焰沙暗探的秘梦'
        self.nickName = '夏团'
        self.role = CardRole.Edmond
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7969
        self.lv60s5Atk = 2063
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力100%
        self.attackMagnification = 1

        # 攻击力100%
        self.skillMagnificationLv1 = 1
        self.skillMagnificationLv2 = 1
        self.skillMagnificationLv3 = 1

    def skillAfter(self, enemies):
        if self.star >= 2:
            buff = Buff('FlamingSecret_skll', 0.54, 2, BuffType.AttackIncrease)
            if len(self.teamMate) == 1:
                self.teamMate[0].addBuff(buff, self)
            else:
                self.teamMate[1].addBuff(buff, self)

        magnification = self.getMagnification(1.02, 1.19, 1.37)
        buff2 = Buff('FlamingSecret_skll2', magnification, 2, BuffType.FollowUpAttack)
        buff2.seeAsAttack = True
        if len(self.teamMate) == 1:
            self.teamMate[0].addBuff(buff2, self)
        else:
            self.teamMate[1].addBuff(buff2, self)

        if self.passive_star_3():
            buff3 = Buff('FlamingSecret_passive_star_3', 0.12, 0, BuffType.BeAttackIncrease)
            buff2.isPassive = True
            if self.calBuffCount('FlamingSecret_passive_star_3') < 3:
                enemies.addBuff(buff3, self)

    def attackAfter(self, enemies):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('FlamingSecret_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)

        if self.passive_star_3():
            buff2 = Buff('FlamingSecret_passive_star_3', 0.12, 0, BuffType.BeAttackIncrease)
            buff2.isPassive = True
            if self.calBuffCount('FlamingSecret_passive_star_3') < 3:
                enemies.addBuff(buff2, self)

    def passive_star_5(self):
        if super(FlamingSecret, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('FlamingSecret_passive_star_5', 0.27, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    def passive_tier_6(self):
        if super(FlamingSecret, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('FlamingSecret_passive_tier_6', 0.06, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)



