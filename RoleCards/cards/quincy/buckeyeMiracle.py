from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.tierType import TierType


class BuckeyeMiracle(SSRCard):
    def __init__(self):
        super(BuckeyeMiracle, self).__init__()
        self.cardId = 'BuckeyeMiracle'
        self.cardName = '七叶之花的奇迹'
        self.nickName = '盾昆/花昆'
        self.role = CardRole.Quincy
        self.cardType = CardType.Wood
        self.occupation = CardOccupation.Guardian
        self.tierType = TierType.Defense
        self.skillCD = 4

        self.lv60s5Hp = 11563
        self.lv60s5Atk = 1352
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    # 攻击力100%
    # 嘲讽（2）
    # 受麻痹-50%（2）
    # 受必杀伤害-40%（2）
    # 被攻击时，攻击力62%/74%/87%反击（2）
    # 转防御
    def skill(self, enemy):
        self.skillCount = 0

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, False, True)

        ma_buff = self.getMagnification(0.62, 0.74, 0.87)
        buff = Buff('BuckeyeMiracle_skill', ma_buff, 2, BuffType.CounterAttack)
        buff.conditionType = ConditionType.WhenBeAttacked
        buff.useBaseAtk = False
        buff.seeAsSkill = True
        self.addBuff(buff)

        buff2 = Buff('BuckeyeMiracle_skill_2', 0, 2, BuffType.Taunt)
        self.addBuff(buff2)

        buff3 = Buff('BuckeyeMiracle_skill_3', -0.4, 2, BuffType.BeSkillIncrease)
        self.addBuff(buff3)

        self.defense = True

        return damage

    # 攻击力100%
    # 转防御
    def attack(self, enemy):
        currentAtk = self.getCurrentAtk()

        damage = self.calDamage(currentAtk, 1, True, False)
        self.defense = True
        return damage

    # 第一回合，自身必杀技冷却时间-4
    # 辅助>=1，造成伤害+18%
    def passive_star_3(self):
        if super(BuckeyeMiracle, self).passive_star_3():
            self.skillCount += 4
            supportCount = 0
            for role in self.teamMate:
                if role.occupation == CardOccupation.Support:
                    supportCount += 1

            if supportCount >= 1:
                buff = Buff('BuckeyeMiracle_passive_star_3', 0.18, 0, BuffType.DamageIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 最大hp+14%
    # 攻击力+14%
    def passive_star_5(self):
        if super(BuckeyeMiracle, self).passive_star_5():
            buff = Buff('BuckeyeMiracle_passive_star_5', 0.14, 0, BuffType.HpIncrease)
            buff.isPassive = True
            self.addBuff(buff)

            buff2 = Buff('BuckeyeMiracle_passive_star_5_2', 0.14, 0, BuffType.AtkIncrease)
            buff2.isPassive = True
            self.addBuff(buff2)

    # 受回复量+20%
    def passive_tier_6(self):
        if super(BuckeyeMiracle, self).passive_tier_6():
            buff = Buff('BuckeyeMiracle_passive_tier_6', 0.2, 0, BuffType.BeHealIncrease)
            buff.isPassive = True
            self.addBuff(buff)
