from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RQuincy(RCard):
    def __init__(self):
        super(RQuincy, self).__init__()
        self.cardId = 'RQuincy'
        self.cardName = '隐居者'
        self.nickName = 'R昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 4874
        self.lv60s5Atk = 1494
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻100%
        self.attackMagnification = 1

        # 攻409%/513%/616%
        self.skillMagnificationLv1 = 4.09
        self.skillMagnificationLv2 = 5.13
        self.skillMagnificationLv3 = 6.16

    # 目标解除防御
    # 攻409%/513%/616%
    def skillBefore(self, enemies):
        enemies.defense = False

    # 攻100%
    # 攻+5%（6）
    def attackAfter(self, enemies):
        buff = Buff('RQuincy_attack', 0.05, 6, BuffType.AtkIncrease)
        self.addBuff(buff)

    # 队伍昆西每1位，必杀+12%(max 3)
    def passive_star_3(self):
        if super(RQuincy, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Quincy:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RQuincy_passive_star_3', 0.12 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(RQuincy, self).passive_star_5():
            buff = Buff('RQuincy_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_3(self):
        if super(RQuincy, self).passive_tier_3():
            buff = Buff('RQuincy_passive_tier_3', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
