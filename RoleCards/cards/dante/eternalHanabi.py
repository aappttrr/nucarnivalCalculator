from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class EternalHanabi(SSRCard):
    def __init__(self):
        super(EternalHanabi, self).__init__()
        self.cardId = 'EternalHanabi'
        self.round = 6
        self.cardName = '永不消散的焰火'
        self.nickName = '水啖'
        self.des = '必杀易伤，伤害中等，是不错的必杀拐，实战站不住再考虑升星'
        self.role = CardRole.Dante
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 6511
        self.lv60s5Atk = 2419
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力125%
        self.attackMagnification = 1.25

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

    # 目标解除防御
    # 目标受必杀+27%（1）
    # 攻击力204%/238%/273%
    def skillBefore(self, enemies):
        enemies.defense = False
        buff = Buff('EternalHanabi_skill', 0.27, 1, BuffType.BeSkillIncrease)
        enemies.addBuff(buff, self)

    def skillAfter(self, enemies):
        if self.star >= 3:
            for role in self.teamMate:
                buff = Buff('EternalHanabi_passive_star_3', 0.05, 5, BuffType.ShieldIncrease)
                role.addBuff(buff, self)

    def attackAfter(self, enemies):
        if self.star >= 3:
            for role in self.teamMate:
                buff = Buff('EternalHanabi_passive_star_3', 0.05, 5, BuffType.ShieldIncrease)
                role.addBuff(buff, self)

    # 攻击时，造成护盾+5%(5)
    # 队伍啖天每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(EternalHanabi, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Dante:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('EternalHanabi_passive_star_3_2', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 敌方全体受必杀+19%
    def passive_star_5(self):
        if super(EternalHanabi, self).passive_star_5():
            for enemy in self.enemies:
                buff = Buff('EternalHanabi_passive_star_5', 0.19, 0, BuffType.BeSkillIncrease)
                buff.isPassive = True
                enemy.addBuff(buff, self)

    # 全体攻击+10%
    def passive_tier_6(self):
        if super(EternalHanabi, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('EternalHanabi_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)
