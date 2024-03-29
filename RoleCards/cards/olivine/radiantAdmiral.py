from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class RadiantAdmiral(SSRCard):
    def __init__(self):
        super(RadiantAdmiral, self).__init__()
        self.cardId = 'RadiantAdmiral'
        self.round = 5
        self.cardName = '闪耀领航'
        self.nickName = '夏奥'
        self.des = '必杀输出，伤害高，缺点是怪多伤害分散，3星可用'
        self.role = CardRole.Olivine
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.difficult

        self.lv60s5Hp = 6724
        self.lv60s5Atk = 2348
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk
        # 攻击力50%对1、3、5造成伤害
        self.attackMagnification = 0.5

        # 攻击力107%/132%/156%对1、3、5造成伤害
        self.skillMagnificationLv1 = 1.07
        self.skillMagnificationLv2 = 1.32
        self.skillMagnificationLv3 = 1.56

    # 必杀+27%（2）
    # 攻击力107%/132%/156%对1、3、5造成伤害
    def skillBefore(self, enemies):
        buff = Buff('RadiantAdmiral_skill', 0.27, 2, BuffType.SkillIncrease)
        self.addBuff(buff)

    # hp>90,攻击力+30%
    def passive_star_3(self):
        if super(RadiantAdmiral, self).passive_star_3():
            buff = Buff('RadiantAdmiral_passive_star_3', 0.3, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            buff.conditionType = ConditionType.WhenHpMoreThan
            buff.conditionValue = 0.9
            self.addBuff(buff)

    # 必杀+38%
    def passive_star_5(self):
        if super(RadiantAdmiral, self).passive_star_5():
            buff = Buff('RadiantAdmiral_passive_star_5', 0.38, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力+10%
    def passive_tier_6(self):
        if super(RadiantAdmiral, self).passive_tier_6():
            buff = Buff('RadiantAdmiral_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def seizeEnemy(self, isAtk: bool):
        enemies = self.enemies
        if len(enemies) == 1:
            temp1 = [enemies[0], enemies[0], enemies[0]]
            return temp1
        elif len(enemies) == 2:
            temp1 = [enemies[0], enemies[0], enemies[1]]
            return temp1
        elif len(enemies) == 3:
            return enemies
        elif len(enemies) == 4:
            temp1 = [enemies[0], enemies[2], enemies[3]]
            return temp1
        elif len(enemies) == 5:
            temp1 = [enemies[0], enemies[2], enemies[4]]
            return temp1
