from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SRDante(SRCard):
    def __init__(self):
        super(SRDante, self).__init__()
        self.cardId = 'SRDante'
        self.cardName = '太阳城主'
        self.nickName = 'SR啖'
        self.des = '通用易伤+普攻破防，SR中较为好用的拐，5星可用'
        self.tag = '通用易伤 / 普攻破防'
        self.role = CardRole.Dante
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryDifficult

        self.lv60s5Hp = 6190
        self.lv60s5Atk = 1601
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
        buff = Buff('SRDante_skill', 0.12, 2, BuffType.BeDamageIncrease)
        enemies.addBuff(buff, self)

    # 解除目标防御
    # 攻100%
    def attackBefore(self, enemies):
        enemies.defense = False

    # 队伍啖天每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(SRDante, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Dante:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SRDante_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻+25%
    def passive_star_5(self):
        if super(SRDante, self).passive_star_5():
            buff = Buff('SRDante_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻+10%
    def passive_tier_6(self):
        if super(SRDante, self).passive_tier_6():
            buff = Buff('SRDante_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
