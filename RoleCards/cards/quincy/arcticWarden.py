from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ArcticWarden(SSRCard):
    def __init__(self):
        super(ArcticWarden, self).__init__()
        self.cardId = 'ArcticWarden'
        self.round = 10
        self.cardName = '守望者的冬季馈礼'
        self.nickName = '冬昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7507
        self.lv60s5Atk = 2205
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻100%
        self.attackMagnification = 1

        # 攻247%/296%/345%
        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    # 攻247%/296%/345%
    # 自身最大HP20%全体治
    def skillHeal(self, enemies, currentAtk):
        heal = self.maxHp * 0.2
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)
        heal = self.increaseDamage(heal, False, True)
        return heal

    # 攻100%
    # 自身最大HP10%全体治
    def attackHeal(self, enemies, currentAtk):
        heal = self.maxHp * 0.1
        heal = roundDown(heal)
        heal = self.increaseHeal(heal)
        heal = self.increaseDamage(heal, True, False)
        return heal

    # 队伍攻击每1位，必杀+13%(max 3）
    def passive_star_3(self):
        if super(ArcticWarden, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('ArcticWarden_passive_star_3', 0.13 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(ArcticWarden, self).passive_star_5():
            buff = Buff('ArcticWarden_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(ArcticWarden, self).passive_tier_6():
            buff = Buff('ArcticWarden_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
