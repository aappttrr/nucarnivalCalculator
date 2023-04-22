from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SmokedTimber(SRCard):
    def __init__(self):
        super(SmokedTimber, self).__init__()
        self.cardId = 'SmokedTimber'
        self.cardName = '沉郁的熏灼木'
        self.nickName = '水昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 6546
        self.lv60s5Atk = 1921
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻125%
        self.attackMagnification = 1.25

        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    # 攻247%/296%/345%
    # 目标攻-15%（2）
    def skillAfter(self, enemies):
        buff = Buff("SmokedTimber_skill", -0.15, 2, BuffType.AtkIncrease)
        enemies.addBuff(buff, self)

    # 队伍昆西每1位，攻+8%(max 3)
    def passive_star_3(self):
        if super(SmokedTimber, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Quincy:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SmokedTimber_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(SmokedTimber, self).passive_star_5():
            buff = Buff('SmokedTimber_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(SmokedTimber, self).passive_tier_6():
            buff = Buff('SmokedTimber_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
