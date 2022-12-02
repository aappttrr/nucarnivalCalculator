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
        self.role = CardRole.Kuya
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.isGroup = True
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 7791
        self.lv60s5Atk = 2028
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻124%/148%/173%（群），敌25%麻痹[4]
    def skill(self, enemy):
        magnification = self.getMagnification(1.24, 1.48, 1.73)
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    def skillAfter(self, enemy):
        for monster in self.enemies:
            if self.passive_star_5() and monster.calBuffCount('FallenLeaves_passive_star_5') < 1:
                buff = Buff('FallenLeaves_passive_star_5', -0.15, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                monster.addBuff(buff, self)

    # 攻50%（群），敌回复量-50%
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()

        damage = self.calDamage(currentAtk, 0.5, True, False)
        for monster in self.enemies:
            buff = Buff('FallenLeaves_attack', -0.5, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            monster.addBuff(buff, self)
        return damage

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
