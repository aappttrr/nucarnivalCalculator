from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class InfernalTreatymaker(SSRCard):
    def __init__(self):
        super(InfernalTreatymaker, self).__init__()
        self.cardId = 'InfernalTreatymaker'
        self.round = 20
        self.cardName = '烈焰的缔约者'
        self.nickName = '枪啖'
        self.des = ''
        self.tag = ''
        self.role = CardRole.Dante
        self.cardType = CardType.Dark
        self.occupation = CardOccupation.Saboteur
        self.tierType = TierType.Balance
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 7329
        self.lv60s5Atk = 2241
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力45%
        self.attackMagnification = 0.45

        # 攻击力43%/51%/60% 各造成两次伤害
        self.skillMagnificationLv1 = 0.43 *2
        self.skillMagnificationLv2 = 0.51 *2
        self.skillMagnificationLv3 = 0.6 *2

    #   解除敌方全体的防御状态
    #   使敌方全体受到伤害增加14%(3)
    #   普攻伤害减少14%(3回合)
    #   再以攻击力43%/51%/60%对敌方站位2、3、4各造成2次伤害[冷却时间:3回合]
    def skillBefore(self, enemies):
        for monster in self.enemies:
            monster.defense = False

            if self.star >= 2:
                buff = Buff('InfernalTreatymaker_skill', 0.14, 3, BuffType.BeDamageIncrease)
                monster.addBuff(buff, self)
                buff2 = Buff('InfernalTreatymaker_skill2', -0.14, 3, BuffType.AttackIncrease)
                monster.addBuff(buff2, self)

    def skillAfter(self, enemies):
        if self.passive_star_3():
            ps3CountMap = {}

            for monster in enemies:
                ps3Count = 0
                if monster in ps3CountMap:
                    ps3Count = ps3CountMap[monster]
                ps3Count += 1
                ps3CountMap[monster] = ps3Count

            for monster, ps3Count in ps3CountMap.items():
                if monster.calBuffCount('InfernalTreatymaker_passive_star_3') < 3:
                    buff2 = Buff('InfernalTreatymaker_passive_star_3', 0.025 * ps3Count, 0, BuffType.BeDamageIncrease)
                    buff2.isPassive = True
                    monster.addBuff(buff2, self)

    # 以攻击力45%对敌方站位2、3、4造成伤害，
    # 并使敌方站位2、3、4受到伤害增加2.5%(1回合)
    def attackAfter(self, enemies):
        for monster in enemies:
            buff = Buff('InfernalTreatymaker_attack', 0.025, 1, BuffType.BeDamageIncrease)
            monster.addBuff(buff, self)

        if self.passive_star_3():
            ps3CountMap = {}

            for monster in enemies:
                ps3Count = 0
                if monster in ps3CountMap:
                    ps3Count = ps3CountMap[monster]
                ps3Count += 1
                ps3CountMap[monster] = ps3Count

            for monster, ps3Count in ps3CountMap.items():
                if monster.calBuffCount('InfernalTreatymaker_passive_star_3') < 3:
                    buff2 = Buff('InfernalTreatymaker_passive_star_3', 0.025 * ps3Count, 0, BuffType.BeDamageIncrease)
                    buff2.isPassive = True
                    monster.addBuff(buff2, self)

    # 攻击时，触发使敌方站位2、3、4受到伤害增加2.5%(最多3层)
    def passive_star_3(self):
        return super(InfernalTreatymaker, self).passive_star_3()

    # 攻击力增加27%
    def passive_star_5(self):
        if super(InfernalTreatymaker, self).passive_star_5():
            buff = Buff('InfernalTreatymaker_passive_star_5', 0.27, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 攻击力增加10%
    def passive_tier_6(self):
        if super(InfernalTreatymaker, self).passive_tier_6():
            buff = Buff('InfernalTreatymaker_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def seizeEnemy(self, isAtk: bool):
        enemies = self.enemies
        if len(enemies) == 1:
            temp1 = [enemies[0], enemies[0], enemies[0]]
            return temp1
        elif len(enemies) == 2:
            temp1 = [enemies[0], enemies[1], enemies[1]]
            return temp1
        elif len(enemies) == 3:
            return enemies
        elif len(enemies) == 4:
            temp1 = [enemies[1], enemies[2], enemies[3]]
            return temp1
        elif len(enemies) == 5:
            temp1 = [enemies[1], enemies[2], enemies[3]]
            return temp1