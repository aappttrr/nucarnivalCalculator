from RoleCards.buff.buff import Buff
from RoleCards.common.srCard import SRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class SRGaru(SRCard):
    def __init__(self):
        super(SRGaru, self).__init__()
        self.cardId = 'SRGaru'
        self.cardName = '流浪小狼'
        self.nickName = 'SR狼'
        self.des = '群体通用易伤，本身也是群攻，缺点是打单体伤害太低，后期可以练一只用来处理机制、割草'
        self.tag = '群体通用易伤'
        self.role = CardRole.Garu
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 5799
        self.lv60s5Atk = 1707
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
        for monster in self.enemies:
            buff = Buff('SRGaru_skill', 0.08, 1, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

    # 敌全体受伤+4%（2）
    # 攻50%（群）
    def attackBefore(self, enemies):
        for monster in self.enemies:
            buff = Buff('SRGaru_attack', 0.04, 2, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

    def nextRound(self):
        super(SRGaru, self).nextRound()
        # 每回合攻+4%（max 10）
        if self.passive_star_5() and self.calBuffCount('SRGaru_passive_star_5') < 10:
            buff = Buff('SRGaru_passive_star_5', 0.04, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 队伍可尔每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(SRGaru, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Garu:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('SRGaru_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 每回合攻+4%（max 10）
    def passive_star_5(self):
        return super(SRGaru, self).passive_star_5()

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(SRGaru, self).passive_tier_6():
            buff = Buff('SRGaru_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
