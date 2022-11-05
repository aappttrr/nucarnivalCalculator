from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.tierType import TierType


class HowlingCyclone(SSRCard):
    def __init__(self):
        super(HowlingCyclone, self).__init__()
        self.cardId = 'HowlingCyclone'
        self.cardName = '诡夜疾风'
        self.nickName = '瓜狼'
        self.role = CardRole.Garu
        self.type = CardType.Light
        self.occupation = CardOccupation.Support
        self.tierType = TierType.Balance
        self.skillCD = 4

        self.lv60s5Hp = 8040
        self.lv60s5Atk = 2028
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力100%
    # 基础攻击力62%/74%/87%，全体攻击力增加（2）
    def skill(self, enemy):
        self.skillCount = 0

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, False,True)

        magnification = self.getMagnification(0.62, 0.74, 0.87)
        actualDamageIncrease = self.atk * magnification
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('HowlingCyclone_skill', actualDamageIncrease, 2, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)

        return damage

    def skillAfter(self, enemy):
        # 3星被动
        # 必杀时，触发全体攻击力+6%（max 2
        for role in self.teamMate:
            if self.passive_star_3() and role.calBuffCount('HowlingCyclone_passive_star_3') < 2:
                buff = Buff('HowlingCyclone_passive_star_3', 0.06, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 攻击力100%
    # 基础攻击力30%，全体攻击力增加（1）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, False,True)

        actualDamageIncrease = self.atk * 0.3
        actualDamageIncrease = roundDown(actualDamageIncrease)

        for role in self.teamMate:
            buff = Buff('HowlingCyclone_skill', actualDamageIncrease, 1, BuffType.AtkIncreaseByActualValue)
            role.addBuff(buff, self)

        return damage

    # 必杀时，触发全体攻击力+6%（max 2
    def passive_star_3(self):
        return super(HowlingCyclone, self).passive_star_3()

    # 全体攻击力+10%
    def passive_star_5(self):
        if super(HowlingCyclone, self).passive_star_5():
            for role in self.teamMate:
                buff = Buff('HowlingCyclone_passive_star_5', 0.10, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)

    # 全体攻击力+3%
    def passive_tier_6(self):
        if super(HowlingCyclone, self).passive_tier_6():
            for role in self.teamMate:
                buff = Buff('HowlingCyclone_passive_tier_6', 0.03, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                role.addBuff(buff, self)