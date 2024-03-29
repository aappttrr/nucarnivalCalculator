from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class RDante(RCard):
    def __init__(self):
        super(RDante, self).__init__()
        self.cardId = 'RDante'
        self.cardName = '世袭少主'
        self.nickName = 'R啖'
        self.role = CardRole.Dante
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 5230
        self.lv60s5Atk = 1387
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻100%
        self.attackMagnification = 1

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 2.04
        self.skillMagnificationLv2 = 2.38
        self.skillMagnificationLv3 = 2.73

    # 目标受伤+12%（2）
    # 攻204%/238%/273%
    def skillBefore(self, enemies):
        buff = Buff('RDante_skill', 0.12, 2, BuffType.BeDamageIncrease)
        enemies.addBuff(buff, self)

    # 解除目标防御
    # 攻100%
    def attackBefore(self, enemies):
        enemies.defense = False

    # 队伍啖天每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(RDante, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Dante:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RDante_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(RDante, self).passive_star_5():
            buff = Buff('RDante_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_3(self):
        if super(RDante, self).passive_tier_3():
            buff = Buff('RDante_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
