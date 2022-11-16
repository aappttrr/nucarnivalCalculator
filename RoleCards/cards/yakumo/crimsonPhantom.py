from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.tierType import TierType


class CrimsonPhantom(SSRCard):
    def __init__(self):
        super(CrimsonPhantom, self).__init__()
        self.cardId = 'CrimsonPhantom'
        self.cardName = '殷红魅影'
        self.nickName = '盾八/伯爵八'
        self.role = CardRole.Yakumo
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 3

        self.lv60s5Hp = 12274
        self.lv60s5Atk = 1316
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 吸血效果100%（1）
    # 攻击力50%
    # 嘲讽（1）
    # 被攻击时，基础攻击力51%/60%/68%反击（2）
    # 转防御
    def skill(self, enemy):
        self.skillCount = 0

        buff = Buff('CrimsonPhantom_skill', 1, 1, BuffType.BloodSucking)
        self.addBuff(buff)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 0.5, False, True)

        ma = self.getMagnification(0.51, 0.6, 0.68)
        buff2 = Buff('CrimsonPhantom_skill_2', ma, 2, BuffType.CounterAttack)
        buff2.conditionType = ConditionType.WhenBeAttacked
        buff2.useBaseAtk = True
        buff2.seeAsSkill = True
        self.addBuff(buff2)
        return damage

    # 吸血效果50%(1)
    # 攻击力50%
    # 转防御
    def attack(self, enemy):
        buff = Buff('CrimsonPhantom_skill', 0.5, 1, BuffType.BloodSucking)
        self.addBuff(buff)

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 0.5, True, False)
        return damage

    # 守护<=1，受到回复量+30%
    def passive_star_3(self):
        if super(CrimsonPhantom, self).passive_star_3():
            count = 0
            for role in self.teamMate:
                if role.occupation == CardOccupation.Guardian:
                    count += 1

            if count <= 1:
                buff = Buff('CrimsonPhantom_passive_star_3', 0.3, 0, BuffType.BeHealIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 受到伤害-10%
    def passive_star_5(self):
        if super(CrimsonPhantom, self).passive_star_5():
            buff = Buff('CrimsonPhantom_passive_star_5', -0.1, 0, BuffType.BeDamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 受到回复量+20%
    def passive_tier_6(self):
        if super(CrimsonPhantom, self).passive_tier_6():
            buff = Buff('CrimsonPhantom_passive_tier_6', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
