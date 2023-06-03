from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class IcyEquilibrium(SSRCard):
    def __init__(self):
        super(IcyEquilibrium, self).__init__()
        self.cardId = 'IcyEquilibrium'
        self.round = 10
        self.cardName = '权衡者的雪藏初心'
        self.nickName = '圣蛋'
        self.role = CardRole.Dante
        self.cardType = CardType.Light
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 8112
        self.lv60s5Atk = 2028
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 我方全体攻击角色获得【普攻时，追击攻47%/58%/68%（3）】
    def skill(self, enemies, currentAtk):
        ma = self.getMagnification(0.47, 0.58, 0.68)
        for role in self.teamMate:
            if role.occupation == CardOccupation.Striker:
                buff = Buff('IcyEquilibrium_skill', ma, 3, BuffType.FollowUpAttack)
                buff.useBaseAtk = False
                buff.seeAsAttack = True
                buff.conditionType = ConditionType.WhenAttack
                role.addBuff(buff, self)
        return 0

    # 基攻30%全体攻+（1）
    def attack(self, enemies, currentAtk):
        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('IcyEquilibrium_attack', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)
        return 0

    # 我方全体普攻+14%
    # 第一回合自身必杀CD-3
    def passive_star_3(self):
        if super(IcyEquilibrium, self).passive_star_3():
            for role in self.teamMate:
                buff = Buff('IcyEquilibrium_skill', 0.14, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

            self.skillCount += 3

    # 我方全体获得【攻击each，普攻+9（max3）】
    def passive_star_5(self):
        if super(IcyEquilibrium, self).passive_star_5():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                for role in self.teamMate:
                    buff = Buff('IcyEquilibrium_passive_star_5', 0.09 * count, 0, BuffType.AttackIncrease)
                    buff.isPassive = True
                    role.addBuff(buff, self)

    # 全体普攻+6%
    def passive_tier_6(self):
        if super(IcyEquilibrium, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('IcyEquilibrium_passive_tier_6', 0.06, 0, BuffType.AttackIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)


