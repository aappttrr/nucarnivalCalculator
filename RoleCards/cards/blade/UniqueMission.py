from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class UniqueMission(SSRCard):
    def __init__(self):
        super(UniqueMission, self).__init__()
        self.cardId = 'UniqueMission'
        self.round = 19
        self.cardName = '唯一使命'
        self.nickName = '锖布'
        self.des = '生存占模较多的万金油输出'
        self.tag = ''
        self.role = CardRole.Blade
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7080
        self.lv60s5Atk = 2312
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻125%
        self.attackMagnification = 1.25

        # 攻284%/345%/406%
        self.skillMagnificationLv1 = 2.84
        self.skillMagnificationLv2 = 3.45
        self.skillMagnificationLv3 = 4.06

    def skillBefore(self, enemies):
        buff = Buff('UniqueMission_skill', -0.08, 4, BuffType.DamageIncrease)
        enemies.addBuff(buff, self)

    def skillAfter(self, enemies):
        if self.star <= 1:
            return
        hotHeal = self.maxHp * 0.1
        hotHeal = roundDown(hotHeal)
        hotHeal = self.increaseHot(hotHeal)

        buff = Buff('UniqueMission_skill2', hotHeal, 4, BuffType.Hot)
        self.addBuff(buff)

        shield = self.maxHp * 0.2
        shield = roundDown(shield)
        shield = self.increaseShield(shield)

        buff2 = Buff('UniqueMission_skill3', shield, 4, BuffType.Shield)
        self.addBuff(buff2)
        self.sendShieldEvent(shield, self)

    # 攻击力+36%
    def passive_star_3(self):
        if super(UniqueMission, self).passive_star_3():
            buff = Buff('UniqueMission_passive_star_3', 0.36, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+27%
    def passive_star_5(self):
        if super(UniqueMission, self).passive_star_5():
            buff = Buff('UniqueMission_passive_star_5', 0.27, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(UniqueMission, self).passive_tier_6():
            buff = Buff('UniqueMission_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
