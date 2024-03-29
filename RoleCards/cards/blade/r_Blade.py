from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class RBlade(RCard):
    def __init__(self):
        super(RBlade, self).__init__()
        self.cardId = 'RBlade'
        self.cardName = '谜样人形'
        self.nickName = 'R布'
        self.role = CardRole.Blade
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 5158
        self.lv60s5Atk = 1387
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        self.isAttackGroup = True
        self.isSkillGroup = True

        # 攻63%（群）
        self.attackMagnification = 0.63

        # 攻142%/173%/203%（群）
        self.skillMagnificationLv1 = 1.42
        self.skillMagnificationLv2 = 1.73
        self.skillMagnificationLv3 = 2.03

    # 队伍布儡每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(RBlade, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Blade:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RBlade_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(RBlade, self).passive_star_5():
            buff = Buff('RBlade_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀+15%
    def passive_tier_3(self):
        if super(RBlade, self).passive_tier_3():
            buff = Buff('RBlade_passive_tier_3', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)
