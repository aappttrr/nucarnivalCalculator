from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType


class ScorchingSun(SSRCard):
    def __init__(self):
        super(ScorchingSun, self).__init__()
        self.cardId = 'ScorchingSun'
        self.round = 16
        self.cardName = '烈日炎阳的戏语'
        self.nickName = '夏啖/沙啖'
        self.role = CardRole.Dante
        self.cardType = CardType.Fire
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 3
        self.ped = PassiveEffectivenessDifficulty.veryEasy

        self.lv60s5Hp = 6937
        self.lv60s5Atk = 2383
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # 攻击力50%
        self.attackMagnification = 0.5

        # 攻击力85%/102%/119%
        self.skillMagnificationLv1 = 0.85
        self.skillMagnificationLv2 = 1.02
        self.skillMagnificationLv3 = 1.19

        self.ps3CD = 3
        self.ps3CDCount = 0

    def skillBefore(self, enemies):
        for enemy in self.enemies:
            buff = Buff('ScorchingSun_skill', 0.135, 0, BuffType.BeSkillIncrease)
            buff.isPassive = True
            if enemy.calBuffCount('ScorchingSun_skill') < 1:
                enemy.addBuff(buff, self)

        if self.star >= 2:
            buff2 = Buff('ScorchingSun_skill2', 0.27, 1, BuffType.AtkIncrease)
            self.addBuff(buff2)

    def passive_star_5(self):
        if super(ScorchingSun, self).passive_star_5():
            buff = Buff('ScorchingSun_passive_star_5', 0.41, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def nextRound(self):
        super(ScorchingSun, self).nextRound()
        self.ps3CDCount += 1
        if self.passive_star_3() and self.ps3CDCount >= self.ps3CD:
            self.ps3CDCount = 0
            buff = Buff('ScorchingSun_passive_star_3', 0.6, 1, BuffType.SkillIncrease)
            self.addBuff(buff)

    def passive_tier_6(self):
        if super(ScorchingSun, self).passive_tier_6():
            buff = Buff('ScorchingSun_passive_tier_6', 0.1, 0, BuffType.AtkIncrease)
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

    def clearUp(self):
        super(ScorchingSun, self).clearUp()
        self.ps3CDCount = 0
