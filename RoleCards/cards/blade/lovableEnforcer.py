from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class LovableEnforcer(SSRCard):
    def __init__(self):
        super(LovableEnforcer, self).__init__()
        self.cardId = 'LovableEnforcer'
        self.round = 9
        self.cardName = '守护甜心'
        self.nickName = '女仆布'
        self.des = '沉默+生存，伤害很低，辅助也不太行，不建议使用'
        self.tag = '75%沉默 / 降低敌方伤害 / 布儡专属伤害增益'
        self.role = CardRole.Blade
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7578
        self.lv60s5Atk = 2170
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻100%
        self.attackMagnification = 1

        # 攻247%/296%/345%
        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    # 自伤+20%（3）
    # 攻247%/296%/345%
    # 50%沉默
    def skillBefore(self, enemies):
        buff = Buff('LovableEnforcer_skill', 0.2, 3, BuffType.DamageIncrease)
        self.addBuff(buff)

    def skillAfter(self, enemies):
        if self.passive_star_5() and enemies.calBuffCount('LovableEnforcer_passive_star_5') < 5:
            buff2 = Buff('LovableEnforcer_passive_star_5', 0.05, 0, BuffType.BeDamageIncreaseByRole)
            buff2.targetRole = CardRole.Blade
            buff2.isPassive = True
            enemies.addBuff(buff2, self)

    # 攻100%
    # 目标伤害-10%（1）
    def attackAfter(self, enemies):
        buff = Buff('LovableEnforcer_attack', -0.1, 1, BuffType.DamageIncrease)
        enemies.addBuff(buff, self)
        if self.passive_star_5() and enemies.calBuffCount('LovableEnforcer_passive_star_5') < 5:
            buff2 = Buff('LovableEnforcer_passive_star_5', 0.05, 0, BuffType.BeDamageIncreaseByRole)
            buff2.targetRole = CardRole.Blade
            buff2.isPassive = True
            enemies.addBuff(buff2, self)

    # 每Wave第一回合，全体沉默几率+25%
    def passive_star_3(self):
        return super(LovableEnforcer, self).passive_star_3()

    # 攻击时，触发【使目标受到布儡伤害增加5%（最多5层）】
    def passive_star_5(self):
        return super(LovableEnforcer, self).passive_star_5()

    # 攻+10%
    def passive_tier_6(self):
        if super(LovableEnforcer, self).passive_tier_6():
            buff = Buff('LovableEnforcer_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
