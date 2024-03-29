from RoleCards.buff.buff import Buff
from RoleCards.common.rCard import RCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


class RGaru(RCard):
    def __init__(self):
        super(RGaru, self).__init__()
        self.cardId = 'RGaru'
        self.cardName = '人类征服'
        self.nickName = 'R狼'
        self.role = CardRole.Garu
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Striker
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 4945
        self.lv60s5Atk = 1458
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

    # 敌全体受伤+8%（1）
    # 攻124%/148%/173%（群）
    def skillBefore(self, enemies):
        for monster in enemies:
            buff = Buff('RGaru_skill', 0.08, 1, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

    # 敌全体受伤+4%（2）
    # 攻50%（群）
    def attackBefore(self, enemies):
        for monster in enemies:
            buff = Buff('RGaru_attack', 0.04, 2, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

    def nextRound(self):
        super(RGaru, self).nextRound()
        # 每回合攻+4%（max 10）
        if self.passive_star_5() and self.calBuffCount('RGaru_passive_star_5') < 10:
            buff = Buff('RGaru_passive_star_5', 0.04, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 队伍可尔每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(RGaru, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Garu:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('RGaru_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 每回合攻+4%（max 10）
    def passive_star_5(self):
        return super(RGaru, self).passive_star_5()

    # 攻击力增加10%（被动）
    def passive_tier_3(self):
        if super(RGaru, self).passive_tier_3():
            buff = Buff('RGaru_passive_tier_3', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
