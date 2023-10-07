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


class TruthSeeker(SSRCard):
    def __init__(self):
        super(TruthSeeker, self).__init__()
        self.cardId = 'TruthSeeker'
        self.round = 19
        self.cardName = '索隐探奥'
        self.nickName = '锖敛'
        self.des = ''
        self.tag = ''
        self.role = CardRole.Rei
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 6
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 7009
        self.lv60s5Atk = 2348
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻125%
        self.attackMagnification = 1.25

        # 攻125%
        self.skillMagnificationLv1 = 1.25
        self.skillMagnificationLv2 = 1.25
        self.skillMagnificationLv3 = 1.25

    # 造成伤害+25%
    # 攻125%
    # 普攻追击57%/77%/98%
    def skillBefore(self, enemies):
        if self.star >= 2 and self.calBuffCount('TruthSeeker_skill') < 1:
            buff = Buff('TruthSeeker_skill', 0.25, 0, BuffType.DamageIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def skillAfter(self, enemies):
        ma = self.getMagnification(0.57, 0.77, 0.98)
        buff = Buff('TruthSeeker_skill2', ma, 6, BuffType.FollowUpAttack)
        buff.useBaseAtk = False
        buff.seeAsAttack = True
        buff.conditionType = ConditionType.WhenAttack
        self.addBuff(buff)

    # 第一回合自身必杀CD-3
    # 普攻伤害+36%
    def passive_star_3(self):
        if super(TruthSeeker, self).passive_star_3():
            self.skillCount += 3
            buff = Buff('TruthSeeker_passive_star_3', 0.36, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 被攻击时，普攻+18%（最多3层）
    def beAttackedAfter(self, seeAsBeAttacked, source):
        super(TruthSeeker, self).beAttackedAfter(seeAsBeAttacked, source)
        if seeAsBeAttacked and self.passive_star_5() and self.calBuffCount('TruthSeeker_passive_star_5') < 3:
            buff = Buff('TruthSeeker_passive_star_5', 0.18, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 普攻伤害+20%
    def passive_tier_6(self):
        if super(TruthSeeker, self).passive_tier_6():
            buff = Buff('TruthSeeker_passive_tier_6', 0.2, 0, BuffType.AttackIncrease)
            buff.isPassive = True
            self.addBuff(buff)
