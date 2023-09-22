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


class AfternoonDaze(SSRCard):
    def __init__(self):
        super(AfternoonDaze, self).__init__()
        self.cardId = 'AfternoonDaze'
        self.round = 12
        self.cardName = '午后醺然'
        self.nickName = '水狐'
        self.des = '通用易伤，伤害中等偏上，目前最好用的通用拐，实战站不住再考虑升星'
        self.tag = '叠层通用易伤'
        self.role = CardRole.Kuya
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 7293
        self.lv60s5Atk = 2277
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻100%
        self.attackMagnification = 1

        # 攻247%/296%/345%
        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    # 目标受到伤害增加15%（2）
    # 攻247%/296%/345%
    # 自身获得【攻击时，触发使目标受到伤害增加15%（2）】（4）
    def skillBefore(self, enemies):
        buff = Buff('AfternoonDaze_skill', 0.15, 2, BuffType.BeDamageIncrease)
        enemies.addBuff(buff, self)

    def skillAfter(self, enemies):
        buff = Buff('AfternoonDaze_skill_2', 0.15, 4, BuffType.AddDamageIncrease)
        buff.addBuffTurn = 2
        buff.conditionType = ConditionType.WhenAttack
        self.addBuff(buff)

    # 攻100%
    # 攻20%持续伤害（2）
    def attack(self, enemies, currentAtk):
        damage = super(AfternoonDaze, self).attack(enemies, currentAtk)

        dotDamage = currentAtk * 0.2
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)

        buff = Buff('AfternoonDaze_Attack', dotDamage, 2, BuffType.Dot)
        enemies.addBuff(buff, self)
        return damage

    # 每位妨碍者，攻击力增加13.5%（最多2次）
    # 玖夜在场时，持续伤害增加50%
    def passive_star_3(self):
        if super(AfternoonDaze, self).passive_star_3():
            buff2 = Buff('AfternoonDaze_passive_star_3_2', 0.5, 0, BuffType.DotIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Saboteur:
                    count += 1

            if count > 2:
                count = 2

            if count > 0:
                buff = Buff('AfternoonDaze_passive_star_3', 0.135 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # Hp>99%，攻击力+33%
    def passive_star_5(self):
        if super(AfternoonDaze, self).passive_star_5():
            buff = Buff('AfternoonDaze_passive_star_5', 0.33, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            buff.conditionType = ConditionType.WhenHpMoreThan
            buff.conditionValue = 0.99
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(AfternoonDaze, self).passive_tier_6():
            buff = Buff('AfternoonDaze_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

