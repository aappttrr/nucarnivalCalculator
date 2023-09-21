from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class FallenLeaves(SSRCard):
    def __init__(self):
        super(FallenLeaves, self).__init__()
        self.cardId = 'FallenLeaves'
        self.cardName = '化形宴，飘落叶'
        self.nickName = '普狐'
        self.des = '减疗麻痹群攻，功能性超多，缺点是伤害巨低，但依然是最值得培养的对策角色'
        self.role = CardRole.Kuya
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 7791
        self.lv60s5Atk = 2028
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        self.isAttackGroup = True
        self.isSkillGroup = True

        # 攻50%（群）
        self.attackMagnification = 0.5

        # 攻124%/148%/173%（群）
        self.skillMagnificationLv1 = 1.24
        self.skillMagnificationLv2 = 1.48
        self.skillMagnificationLv3 = 1.73

    # 攻124%/148%/173%（群）
    # 敌25%麻痹[4]
    def skillAfter(self, enemies):
        for enemy in self.enemies:
            if self.passive_star_5() and enemy.calBuffCount('FallenLeaves_passive_star_5') < 1:
                buff = Buff('FallenLeaves_passive_star_5', -0.15, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                enemy.addBuff(buff, self)

    # 攻50%（群）
    # 敌回复量-50%
    def attackAfter(self, enemies):
        for monster in enemies:
            buff = Buff('FallenLeaves_attack', -0.5, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            monster.addBuff(buff, self)

    # 队伍玖夜每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(FallenLeaves, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Kuya:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('FallenLeaves_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀时，敌全体攻-15%（max 1）
    def passive_star_5(self):
        return super(FallenLeaves, self).passive_star_5()

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(FallenLeaves, self).passive_tier_6():
            buff = Buff('FallenLeaves_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
