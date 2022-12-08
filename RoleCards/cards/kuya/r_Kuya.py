from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class RKuya(RCard):
    def __init__(self):
        super(RKuya, self).__init__()
        self.cardId = 'RKuya'
        self.cardName = '化形妖狐'
        self.nickName = 'R狐'
        self.role = CardRole.Kuya
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Saboteur
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5514
        self.lv60s5Atk = 1316
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻247%/296%/345%
    # 目标受回复量-100%（2）
    def skill(self, enemies, currentAtk):
        magnification = self.getMagnification(2.47, 2.96, 3.45)
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    def skillAfter(self, enemies):
        buff = Buff('RKuya_skill', -1, 2, BuffType.BeHealIncrease)
        enemies.addBuff(buff, self)

    # 攻100%
    # 目标受回复量-50%（1）
    def attack(self, enemies, currentAtk):
        damage = self.calDamage(currentAtk, 1, True, False)
        return damage

    def attackAfter(self, enemies):
        buff = Buff('RKuya_attack', -0.5, 1, BuffType.BeHealIncrease)
        enemies.addBuff(buff, self)

    # 队伍玖夜每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(RKuya, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Kuya:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RKuya_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(RKuya, self).passive_star_5():
            buff = Buff('RKuya_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(RKuya, self).passive_tier_3():
            buff = Buff('RKuya_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
