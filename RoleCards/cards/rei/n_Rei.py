from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class NRei(NCard):
    def __init__(self):
        super(NRei, self).__init__()
        self.cardId = 'NRei'
        self.cardName = '逃捕者'
        self.nickName = 'N敛'
        self.role = CardRole.Rei
        self.occupation = CardOccupation.Saboteur
        self.cardType = CardType.Fire
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 4589
        self.lv60s5Atk = 1138
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

        # 攻125%
        self.attackMagnification = 1.25

    # 队伍敛每1位，攻+8%(max 3)
    def passive_star_3(self):
        if super(NRei, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Rei:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('NRei_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(NRei, self).passive_star_5():
            buff = Buff('NRei_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(NRei, self).passive_tier_6():
            buff = Buff('NRei_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)