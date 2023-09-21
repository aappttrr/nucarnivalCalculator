from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SpringChaos(SSRCard):
    def __init__(self):
        super(SpringChaos, self).__init__()
        self.cardId = 'SpringChaos'
        self.round = 12
        self.cardName = '春日迷乱'
        self.nickName = '花团'
        self.des = '普攻嘲讽，很灵活，但容易站不住，建议3星'
        self.role = CardRole.Edmond
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 11385
        self.lv60s5Atk = 1458
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力100%
        self.attackMagnification = 1

        # 攻击力100%
        self.skillMagnificationLv1 = 1
        self.skillMagnificationLv2 = 1
        self.skillMagnificationLv3 = 1

    # 攻击力100%
    # 目标造成伤害-10%（3）
    # 自身受到伤害-5%/6.75%/7.5%（最多2层）永久？
    # 以最大HP 7.5%/10%/12.5%对自身进行持续治疗（4）
    def skillAfter(self, enemies):
        buff1 = Buff('SpringChaos_skill', -0.1, 3, BuffType.DamageIncrease)
        enemies.addBuff(buff1, self)

        ma = self.getMagnification(0.05, 0.0675, 0.075)
        if self.calBuffCount("SpringChaos_skill_2") < 2:
            buff2 = Buff("SpringChaos_skill_2", -ma, 0, BuffType.BeDamageIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)

        ma2 = self.getMagnification(0.075, 0.1, 0.125)
        hotHeal = self.maxHp * ma2
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)
        buff3 = Buff('SpringChaos_skill_3', hotHeal, 4, BuffType.Hot)
        self.addBuff(buff3)

    # 攻击力100%
    # 嘲讽（1）
    # 自身转防御
    def attackAfter(self, enemies):
        buff = Buff('SpringChaos_attack', 0, 1, BuffType.Taunt)
        self.addBuff(buff)
        self.defense = True

    # hp + 27%
    def passive_star_3(self):
        if super(SpringChaos, self).passive_star_3():
            buff = Buff('SpringChaos_passive_star_3', 0.27, 0, BuffType.HpIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # hp>99%，受伤减少15%
    # 防御减伤增加10%
    def passive_star_5(self):
        if super(SpringChaos, self).passive_star_5():
            buff = Buff('SpringChaos_passive_star_5', -0.15, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            buff.conditionType = ConditionType.WhenHpMoreThan
            buff.conditionValue = 0.99
            self.addBuff(buff)

            buff2 = Buff('SpringChaos_passive_star_5_2', 0.1, 0, BuffType.DefenseDamageReduction)
            buff2.isPassive = True
            self.addBuff(buff2)
