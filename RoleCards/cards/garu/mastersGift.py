from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class MastersGift(SSRCard):
    def __init__(self):
        super(MastersGift, self).__init__()
        self.cardId = 'MastersGift'
        self.cardName = '来自主人的新礼物'
        self.nickName = '普狼'
        self.role = CardRole.Garu
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.isGroup = True
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 7258
        self.lv60s5Atk = 2170
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻142%/173%/203%（群）[4]
    def skill(self, enemy):
        magnification = self.getMagnification(1.42, 1.73, 2.03)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, magnification, False, True)
        return damage

    # 攻63%（群）
    def attack(self, enemy, printInfo=False):
        currentAtk = self.getCurrentAtk()

        damage = self.calDamage(currentAtk, 0.63, True, False)
        return damage

    # 队伍可尔每1位，自攻+8%(max 3)
    def passive_star_3(self):
        if super(MastersGift, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.role == CardRole.Garu:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('MastersGift_passive_star_3', 0.08 * count, 0, BuffType.AtkIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 攻击力增加25%（被动）
    def passive_star_5(self):
        if super(MastersGift, self).passive_star_3():
            buff = Buff('MastersGift_passive_star_5', 0.25, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%（被动）
    def passive_tier_6(self):
        if super(MastersGift, self).passive_tier_6():
            buff = Buff('MastersGift_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)
