from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class EndlessBanquet(SSRCard):
    def __init__(self):
        super(EndlessBanquet, self).__init__()
        self.cardId = 'EndlessBanquet'
        self.round = 4
        self.cardName = '华宴夜未央'
        self.nickName = '光狼'
        self.role = CardRole.Garu
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.medium

        self.lv60s5Hp = 7329
        self.lv60s5Atk = 2134
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力100%
        self.attackMagnification = 1

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

    # 攻击力204%/238%/273%
    # 目标受到伤害+10%（9）
    def skillAfter(self, enemies):
        buff = Buff('EndlessBanquet_skill', 0.1, 9, BuffType.BeDamageIncrease)
        enemies.addBuff(buff, self)

    # 攻击力100%
    # 目标受到伤害+2%（7）
    def attackAfter(self, enemies):
        buff = Buff('EndlessBanquet_attack', 0.02, 7, BuffType.BeDamageIncrease)
        enemies.addBuff(buff, self)

    # 玖夜在场，攻击力+27%
    def passive_star_3(self):
        if super(EndlessBanquet, self).passive_star_3():
            for role in self.teamMate:
                if role.role == CardRole.Kuya:
                    buff = Buff('EndlessBanquet_passive_star_3', 0.27, 0, BuffType.AtkIncrease)
                    buff.isPassive = True
                    self.addBuff(buff)
                    break

    # 目标受到伤害+8%
    def passive_star_5(self):
        if super(EndlessBanquet, self).passive_star_5():
            for enemy in self.enemies:
                buff = Buff('EndlessBanquet_passive_star_5', 0.08, 0, BuffType.BeDamageIncrease)
                buff.isPassive = True
                enemy.addBuff(buff, self)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(EndlessBanquet, self).passive_tier_6():
            buff = Buff('EndlessBanquet_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
