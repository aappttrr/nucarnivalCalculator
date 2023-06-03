from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class DarkNova(SSRCard):
    def __init__(self):
        super(DarkNova, self).__init__()
        self.cardId = 'DarkNova'
        self.round = 14
        self.cardName = '幽暧新星的祷词'
        self.nickName = '早八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7151
        self.lv60s5Atk = 2312
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻125 %
        self.attackMagnification = 1.25

        # 攻击力125%
        self.skillMagnificationLv1 = 1.25
        self.skillMagnificationLv2 = 1.25
        self.skillMagnificationLv3 = 1.25

    # 目标受普攻+27%（最多1层）
    # 普攻时，61%/74%/94%攻击力追击(3)
    # lv2后增加，普攻时，61%/74%/94%攻击力追击(2)
    def skillAfter(self, enemies):
        if enemies.calBuffCount('DarkNova_skill') < 1:
            buff = Buff('DarkNova_skill', 0.27, 0, BuffType.BeAttackIncrease)
            buff.isPassive = True
            enemies.addBuff(buff, self)

        ma = self.getMagnification(0.61, 0.74, 0.94)
        buff2 = Buff('DarkNova_skill_2', ma, 3, BuffType.FollowUpAttack)
        buff2.useBaseAtk = False
        buff2.seeAsAttack = True
        buff2.conditionType = ConditionType.WhenAttack
        self.addBuff(buff2)

        if self.star >= 2:
            buff3 = Buff('DarkNova_skill_3', ma, 2, BuffType.FollowUpAttack)
            buff3.useBaseAtk = False
            buff3.seeAsAttack = True
            buff3.conditionType = ConditionType.WhenAttack
            self.addBuff(buff3)

    # 普攻+72%
    def passive_star_3(self):
        if super(DarkNova, self).passive_star_3():
            buff = Buff('DarkNova_passive_star_3', 0.72, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 队伍攻击每1位，普攻+18%(max 3）
    def passive_star_5(self):
        if super(DarkNova, self).passive_star_5():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('DarkNova_passive_star_5', 0.18 * count, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 普攻+20%
    def passive_tier_6(self):
        if super(DarkNova, self).passive_tier_6():
            buff = Buff('DarkNova_passive_tier_6', 0.2, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)
