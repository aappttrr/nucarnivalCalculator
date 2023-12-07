from Common.ncRound import roundDown
from RoleCards.buff.buff import Buff
from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType
from Common.nvEventManager import eventManagerInstance, EventType, Event


class BinaryStarlight(SSRCard):
    def __init__(self):
        super(BinaryStarlight, self).__init__()
        self.cardId = 'BinaryStarlight'
        self.round = 16
        self.cardName = '双星辉映'
        self.nickName = '霜狼'
        self.des = ''
        self.tag = ''
        self.role = CardRole.Garu
        self.cardType = CardType.Water
        self.occupation = CardOccupation.Striker
        self.tierType = TierType.Attack
        self.skillCD = 4
        self.ped = PassiveEffectivenessDifficulty.easy

        self.lv60s5Hp = 6866
        self.lv60s5Atk = 2383
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        # # 攻击力100%
        self.attackMagnification = 1.25

        # 攻击力204%/238%/273%
        self.skillMagnificationLv1 = 0.56
        self.skillMagnificationLv2 = 0.69
        self.skillMagnificationLv3 = 0.82

    # 以当前HP 20%对自身造成真实伤害
    # 并以攻击力56%/69%/82%对敌方站位1、2、3造成伤害
    # 再以攻击力56%/69%/82%对敌方站位3、4、5造成伤害[冷却时间: 4回合]
    def skillBefore(self, enemies):
        damage = self.hpCurrent * 0.2
        damage = roundDown(damage)
        self.hpCurrent -= damage

        # self.doBloodSuck(damage)

    def skillAfter(self, enemies):
        if self.star >= 2:
            buff = Buff('BinaryStarlight_skill', 0.5, 3, BuffType.BloodSucking)
            self.addBuff(buff)

    # 队伍中每存在1名定位攻击的角色
    # 发动「必杀技伤害增加20%」(最多3次)
    def passive_star_3(self):
        if super(BinaryStarlight, self).passive_star_3():
            count = 0
            for mate in self.teamMate:
                if mate.occupation == CardOccupation.Striker:
                    count += 1

            if count > 3:
                count = 3

            if count > 0:
                buff = Buff('BinaryStarlight_passive_star_3', 0.2 * count, 0, BuffType.SkillIncrease)
                buff.isPassive = True
                self.addBuff(buff)

    # 必杀技伤害增加41%
    def passive_star_5(self):
        if super(BinaryStarlight, self).passive_star_5():
            buff = Buff('BinaryStarlight_passive_star_5', 0.41, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    # 必杀技伤害增加15%
    def passive_tier_6(self):
        if super(BinaryStarlight, self).passive_tier_6():
            buff = Buff('BinaryStarlight_passive_tier_6', 0.15, 0, BuffType.SkillIncrease)
            buff.isPassive = True
            self.addBuff(buff)

    def doSkill(self):
        self.skillCount = 0
        enemies = self.seizeEnemySp1(True)
        enemies2 = self.seizeEnemySp2(True)
        enemies.append(enemies2[0])
        enemies.append(enemies2[1])
        enemies.append(enemies2[2])
        self.skillBefore(enemies)
        currentAtk = self.getCurrentAtk()
        event1 = Event(EventType.actionAtk)
        event1.data['source'] = self
        event1.data['value'] = currentAtk
        event1.data['target'] = self
        eventManagerInstance.sendEvent(event1)

        self.damageCount = {}
        for tempEnemy in self.enemies:
            self.damageCount[tempEnemy] = 0
            tempEnemy.beDamageCount[self] = 0
        damage = self.skill(enemies, currentAtk)
        totalDamage = 0
        if damage > 0:
            if isinstance(enemies, list):
                for enemy in enemies:
                    damage2 = enemy.increaseBeDamage(damage, self, False, True)
                    totalDamage += damage2
                    self.addDamageCount(damage2, enemy, False)
                    event = Event(EventType.skillDamage)
                    event.data['source'] = self
                    event.data['value'] = damage2
                    event.data['target'] = enemy
                    eventManagerInstance.sendEvent(event)
            else:
                damage2 = enemies.increaseBeDamage(damage, self, False, True)
                totalDamage += damage2
                self.addDamageCount(damage2, enemies, False)
                event = Event(EventType.skillDamage)
                event.data['source'] = self
                event.data['value'] = damage2
                event.data['target'] = enemies
                eventManagerInstance.sendEvent(event)

        heal = self.skillHeal(enemies, currentAtk)
        if heal > 0:
            for mate in self.teamMate:
                heal2 = mate.increaseBeHeal(heal)
                event = Event(EventType.skillHeal)
                event.data['source'] = self
                event.data['value'] = heal2
                event.data['target'] = mate
                eventManagerInstance.sendEvent(event)
                mate.beHealed(heal2, True)

        if damage <= 0 and heal <= 0:
            event = Event(EventType.skill)
            event.data['source'] = self
            event.data['value'] = 0
            event.data['target'] = self
            eventManagerInstance.sendEvent(event)

        totalDamage += self.followUp(currentAtk, False)
        self.triggerWhenAttackOrSkill(enemies, False)
        self.doBloodSuck(totalDamage)

        self.skillAfter(enemies)
        currentAtk2 = self.getCurrentAtk()
        event2 = Event(EventType.actionAfterAtk)
        event2.data['source'] = self
        event2.data['value'] = currentAtk2
        event2.data['target'] = self
        eventManagerInstance.sendEvent(event2)

    def seizeEnemySp1(self, isAtk: bool):
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
            temp1 = [enemies[0], enemies[1], enemies[2]]
            return temp1
        elif len(enemies) == 5:
            temp1 = [enemies[0], enemies[1], enemies[2]]
            return temp1

    def seizeEnemySp2(self, isAtk: bool):
        enemies = self.enemies
        if len(enemies) == 1:
            temp1 = [enemies[0], enemies[0], enemies[0]]
            return temp1
        elif len(enemies) == 2:
            temp1 = [enemies[0], enemies[1], enemies[1]]
            return temp1
        elif len(enemies) == 3:
            temp1 = [enemies[2], enemies[2], enemies[2]]
            return temp1
        elif len(enemies) == 4:
            temp1 = [enemies[2], enemies[3], enemies[3]]
            return temp1
        elif len(enemies) == 5:
            temp1 = [enemies[2], enemies[3], enemies[4]]
            return temp1