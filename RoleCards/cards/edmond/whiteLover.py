from RoleCards.buff.buff import Buff
from RoleCards.common.card import roundDown
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.tierType import TierType


class WhiteLover(SSRCard):
    def __init__(self):
        super(WhiteLover, self).__init__()
        self.cardId = 'WhiteLover'
        self.cardName = '白色恋人'
        self.nickName = '白团'
        self.role = CardRole.Edmond
        self.type = CardType.Light
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3

        self.lv60s5Hp = 6831
        self.lv60s5Atk = 2312
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        self.isGroup = True

    # 攻击力64%/77%/90%（群）
    # 攻击力21%/26%/30%持续伤害(群)（3）
    def skill(self, enemy):
        self.skillCount = 0

        ma = self.getMagnification(0.64, 0.77, 0.9)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, ma, False, True)

        ma_dot = self.getMagnification(0.21, 0.26, 0.3)
        dotDamage = currentAtk * ma_dot
        dotDamage = roundDown(dotDamage)
        dotDamage = self.increaseDot(dotDamage)
        for monster in self.enemies:
            buff = Buff('WhiteLover_skill', dotDamage, 3, BuffType.Dot)
            monster.addBuff(buff, self)

        return damage

    # 攻击力63%（群）
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 0.63, True,False)
        return damage

    # 八云在场，攻击力+27%
    def passive_star_3(self):
        if super(WhiteLover, self).passive_star_3():
            for role in self.teamMate:
                if role.role == CardRole.Yakumo:
                    buff = Buff('WhiteLover_passive_star_3', 0.27, 0, BuffType.AtkIncrease)
                    buff.isPassive = True
                    self.addBuff(buff)
                    break

    # 攻击力+27%
    def passive_star_5(self):
        if super(WhiteLover, self).passive_star_5():
            buff = Buff('WhiteLover_passive_star_5', 0.27, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(WhiteLover, self).passive_tier_6():
            buff = Buff('WhiteLover_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

