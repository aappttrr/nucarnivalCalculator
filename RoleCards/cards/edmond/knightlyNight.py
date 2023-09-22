import math

from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class KnightlyNight(SSRCard):
    def __init__(self):
        super(KnightlyNight, self).__init__()
        self.cardId = 'KnightlyNight'
        self.cardName = '爵士册封之夜'
        self.nickName = '普团/水团'
        self.des = '普攻输出，伤害中等偏上，必须3星'
        self.tag = '普攻输出'
        self.role = CardRole.Edmond
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7400
        self.lv60s5Atk = 2134
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻125%
        self.attackMagnification = 1.25

        # 攻125%
        self.skillMagnificationLv1 = 1.25
        self.skillMagnificationLv2 = 1.25
        self.skillMagnificationLv3 = 1.25

    # 攻125%
    # 普攻时，78%/111%/143%攻击力追击(3)
    def skillAfter(self, enemies):
        ma = self.getMagnification(0.78, 1.11, 1.43)
        buff = Buff('KnightlyNight_skill', ma, 3, BuffType.FollowUpAttack)
        buff.useBaseAtk = False
        buff.seeAsAttack = True
        buff.conditionType = ConditionType.WhenAttack
        self.addBuff(buff)

    # 队伍攻击每1位，普攻+17%(max 3）
    def passive_star_3(self):
        if super(KnightlyNight, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('KnightlyNight_passive_star_3', 0.17 * count, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 普攻+50%
    def passive_star_5(self):
        if super(KnightlyNight, self).passive_star_5():
            buff = Buff('KnightlyNight_passive_star_5', 0.5, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 普攻+20%
    def passive_tier_6(self):
        if super(KnightlyNight, self).passive_tier_6():
            buff = Buff('KnightlyNight_passive_tier_6', 0.2, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)
