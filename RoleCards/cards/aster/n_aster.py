from RoleCards.buff.buff import Buff
from RoleCards.common.nCard import NCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class NAster(NCard):
    def __init__(self):
        super(NAster, self).__init__()
        self.cardId = 'NAster'
        self.cardName = '王国首富'
        self.nickName = 'N艾'
        self.role = CardRole.Aster
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 4767
        self.lv60s5Atk = 1102
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻125%
        self.attackMagnification = 1.25

        self.skillMagnificationLv1 = 2.47
        self.skillMagnificationLv2 = 2.96
        self.skillMagnificationLv3 = 3.45

    # 吸血25%（4），攻247%/296%/345%
    def skillBefore(self, enemies):
        buff = Buff('NAster_skill', 0.25, 4, BuffType.BloodSucking)
        self.addBuff(buff)

    # 有墨菲，攻+10%
    # 队伍艾斯特每1位，自攻+5%(max 3)
    def passive_star_3(self):
        if super(NAster, self).passive_star_3():
            count = 0
            hasMorvay = False
            for mate in self.teamMate:
                if mate.role == CardRole.Aster:
                    count += 1
                elif mate.role == CardRole.Morvay:
                    hasMorvay = True

            if count > 3:
                count = 3

            if hasMorvay:
                buff = Buff('NAster_passive_star_3', 0.1, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

            if count > 0:
                buff = Buff('NAster_passive_star_3_2', 0.05 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 普攻+50%
    def passive_star_5(self):
        if super(NAster, self).passive_star_5():
            buff = Buff('NAster_passive_star_5', 0.5, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 普攻+20%
    def passive_tier_3(self):
        if super(NAster, self).passive_tier_3():
            buff = Buff('NAster_passive_tier_3', 0.2, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)
