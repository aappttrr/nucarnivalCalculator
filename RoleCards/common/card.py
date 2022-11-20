import math
from decimal import Decimal

from RoleCards.buff.buff import Buff
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from RoleCards.enum.conditionTypeEnum import ConditionType
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty
from RoleCards.enum.tierType import TierType
from RoleCards.tier.tierData import getTierData


def calBond(lv60s5=1, _bond=0):
    result = lv60s5
    match _bond:
        case 1:
            result = result * 1.05
        case 2:
            result = result * 1.1
        case 3:
            result = result * 1.2
        case 4:
            result = result * 1.3
        case 5:
            result = result * 1.5
    # result = roundCeiling(result)
    return result


def calStar(lv60s5=1, _star=5):
    if _star == 5 or _star <= 0:
        return lv60s5
    result = lv60s5
    for i in reversed(range(_star, 5)):
        temp = 1 + (1 / (5 + i))
        result = result / temp
        # result = roundCeiling(result)
    return result


def calTier(lv60s5=1, _tierValue=0.0):
    result = lv60s5 * (1 + _tierValue)
    # result = roundCeiling(result)
    return result


def calLv(lv60s5=1, _lv=60):
    if _lv == 60 or _lv <= 0:
        return lv60s5
    result = lv60s5
    for i in reversed(range(_lv, 60)):
        result = result / 1.05
        # result = roundCeiling(result)
    return result


'''
ROUND_CEILING（朝向无限），
ROUND_DOWN（朝向零），
ROUND_FLOOR（朝向无限），
ROUND_HALF_DOWN（最接近，领带朝向零），
ROUND_HALF_EVEN（到最近的，领带到最近的偶数整数），
ROUND_HALF_UP（最接近零）或ROUND_ UP（远离零）。
ROUND_05UP（如果向零舍入后的最后一位数字为0或5，则远离零；否则为零）
'''


def roundCeiling(value=0):
    return int(Decimal(value).quantize(Decimal("1."), rounding='ROUND_CEILING'))


def roundDown(value=0):
    return int(Decimal(value).quantize(Decimal("1."), rounding='ROUND_DOWN'))


class ICard:
    def __init__(self):
        # id
        self.cardId = None

        # 名称
        self.cardName = None

        # 昵称
        self.nickName = None

        # 角色
        self.role: CardRole = None

        # 稀有度
        self.rarity: CardRarity = None

        # 属性
        self.cardType: CardType = None

        # 职业定位
        self.occupation: CardOccupation = None

        # 是否为群体攻击
        self.isGroup = False

        # 等级(1-60)
        self.lv = 60

        # 星级
        self.star = 5

        # 生命值
        self.hp = 1

        # 战斗中的当前生命值
        self.hpCurrent = self.hp

        # 最大生命值
        self.maxHp = self.hp

        # 攻击力
        self.atk = 1

        # 蜜话等级(0-5)
        self.bond = 0

        # 潜能(0-12)
        self.tier = 0

        # 潜能类型
        self.tierType: TierType = None

        # 技能CD
        self.skillCD = 0

        # 临时属性，用于计算当前角色是否能释放技能
        self.skillCount = 0

        # 获得的增益
        self.buffs: list[Buff] = []

        # 队友（0-4）
        self.teamMate: list[ICard] = []

        # 敌方（1-5）
        self.enemies: list[ICard] = []

        # lv60 5星 时数据（回廊
        self.lv60s5Hp = 0
        self.lv60s5Atk = 0

        # 当前是否正在防御
        self.defense = False

        # 使用期望数值
        self.useExpectedValue = True

        # 被动吃满难易程度
        self.ped: PassiveEffectivenessDifficulty = None

    def clearUp(self):
        self.skillCount = 0
        self.defense = False
        self.buffs: list[Buff] = []

    def activeBuffs(self):
        self.passive_star_3()
        self.passive_star_5()

    def setProperties(self, _lv, _star, _bond, _tier):
        self.lv = _lv
        self.star = _star
        self.bond = _bond
        self.tier = _tier
        if self.lv <= 0:
            self.lv = 1
        elif self.lv >= 61:
            self.lv = 60
        if self.star <= 0:
            self.star = 1
        elif self.star >= 6:
            self.star = 5
        if self.bond < 0:
            self.bond = 0
        elif self.bond >= 6:
            self.bond = 5

    def setLv(self, _lv):
        self.lv = _lv

    def setStar(self, _star):
        self.star = _star

    def setBond(self, _bond):
        self.bond = _bond

    def setTier(self, _tier):
        self.tier = _tier

    def calHpAtk(self, ignore=False):
        if self.useExpectedValue or ignore:
            self.atk = self.cal(self.lv60s5Atk, True)
            self.hp = self.cal(self.lv60s5Hp, False)

    def calMaxHp(self):
        maxHp = self.hp
        increase = 0
        for buff in self.buffs:
            if buff.buffType == BuffType.HpIncrease:
                increase += buff.value

        if increase != 0:
            maxHp = maxHp * (1 + increase)
            maxHp = roundDown(maxHp)

        self.maxHp = maxHp
        self.hpCurrent = self.maxHp

    def cal(self, lv60s5=1, isAtk=True):
        result = lv60s5

        result = calBond(result, self.bond)

        tierValue = getTierData(self.tierType, self.tier, isAtk)

        result = calTier(result, tierValue)
        result = calStar(result, self.star)
        result = calLv(result, self.lv)
        result = roundCeiling(result)
        return result

    def setHpAtkDirect(self, _hp, _atk):
        self.hp = _hp
        self.atk = _atk

    def setHpDirect(self, _hp,):
        self.hp = _hp

    def setAtkDirect(self,_atk):
        self.atk = _atk

    def getMagnification(self, _s1, _s2, _s4):
        magnification = _s1
        if self.star >= 4:
            magnification = _s4
        elif 2 <= self.star < 4:
            magnification = _s2
        return magnification

    # 吸血
    def doBloodSuck(self, damage):
        for buff in self.buffs:
            if buff.buffType == BuffType.BloodSucking:
                heal = damage * buff.value
                heal = self.increaseHeal(heal)

                self.hpCurrent += heal
                if self.hpCurrent > self.maxHp:
                    self.hpCurrent = self.maxHp

    # dot伤害结算：攻击力*倍率*[造成伤害增加*持续伤害增加(来源于自身，挂上dot的那一刻已确定该伤害)]*[(目标受持续伤害增加+目标受伤害增加)(来源于敌方，在敌方结算dot时计算)]
    # 结算dot，dot是锁面板技能
    def settleDot(self):
        dotDamages = {}
        for buff in self.buffs:
            if buff.buffType == BuffType.Dot:
                dotDamage = buff.value
                dotDamage = self.increaseBeDot(dotDamage)
                oldDamage = 0
                if buff.source in dotDamages:
                    oldDamage = dotDamages.get(buff.source)
                dotDamages[buff.source] = dotDamage + oldDamage

        return dotDamages

    # hot治疗结算：攻击力*倍率*[持续治疗增加(来源于治疗的角色)]*[回复量增加(来源于被治疗的角色)]（不一定对）
    # 结算hot，hot是锁面板技能
    def settleHot(self):
        hotHeals = {}
        for buff in self.buffs:
            if buff.buffType == BuffType.Hot:
                hotHeal = buff.value
                hotHeal = self.increaseBeHeal(hotHeal)
                if buff.source in hotHeals:
                    hotHeal += hotHeals.get(buff.source)
                hotHeals[buff.source] = hotHeal

        return hotHeals

    def getCurrentAtk(self):
        result = self.atk
        increase = 0
        increaseActualValue = 0
        for buff in self.buffs:
            # 如果当前buff条件时，当hp>xx时，当前生命值比例小于条件数值，则不判断该加成
            # 普八、火狐、火团、暗奥
            if buff.conditionType == ConditionType.WhenHpMoreThan:
                condition = self.hpCurrent / self.maxHp
                if condition <= buff.conditionValue:
                    continue
            # 获取攻击力增益（百分比）
            if buff.buffType == BuffType.AtkIncrease:
                increase += buff.value
            # 获取攻击力增益（具体数值），一般来源于辅助
            if buff.buffType == BuffType.AtkIncreaseByActualValue:
                increaseActualValue += buff.value

        if increase != 0:
            result = result * (1 + increase)
            result = roundDown(result)
        if increaseActualValue != 0:
            result = result + increaseActualValue

        if result < 0:
            result = 0

        return result

    # 由于dot挂在敌方身上，由敌方结算，所以这里直接获取自身的buff
    def increaseBeDot(self, damage):
        result = damage

        # 由敌方提升的受到持续伤害增加
        dotIncrease = 0

        # 由敌方提升的受到伤害增加
        damageIncrease = 0
        for buff in self.buffs:
            if buff.buffType == BuffType.BeDotIncrease:
                dotIncrease += buff.value

            if buff.buffType == BuffType.BeDamageIncrease:
                damageIncrease += buff.value

        if dotIncrease != 0:
            result = result * (1 + dotIncrease)
            result = roundDown(result)
        if damageIncrease != 0:
            result = result * (1 + damageIncrease)
            result = roundDown(result)

        if result < 0:
            result = 0

        return result

    def increaseDot(self, damage):
        result = damage

        # 由自身提升的持续伤害增加
        dotIncrease = 0

        # 由自身提升的造成伤害增加
        damageIncrease = 0
        for buff in self.buffs:
            if buff.buffType == BuffType.DotIncrease:
                dotIncrease += buff.value
            if buff.buffType == BuffType.DamageIncrease:
                damageIncrease += buff.value

        if dotIncrease != 0:
            result = result * (1 + dotIncrease)
            result = roundDown(result)
        if damageIncrease != 0:
            result = result * (1 + damageIncrease)
            result = roundDown(result)

        return result

    def increaseHeal(self,heal):
        result = heal

        # 由自身提升的造成回复量增加
        healIncrease = 0

        for buff in self.buffs:
            if buff.buffType == BuffType.HealIncrease:
                healIncrease += buff.value

        if healIncrease != 0:
            result = result * (1 + healIncrease)
            result = roundDown(result)
        if result < 0:
            result = 0
        return result

    def increaseBeHeal(self, heal):
        result = heal

        # 由自身提升的受回复量增加
        healIncrease = 0

        for buff in self.buffs:
            if buff.buffType == BuffType.BeHealIncrease:
                healIncrease += buff.value

        if healIncrease != 0:
            result = result * (1 + healIncrease)
            result = roundDown(result)
        if result < 0:
            result = 0
        return result

    def increaseHot(self, heal):
        result = heal

        # 由自身提升的受持续治疗增加
        healIncrease = 0

        for buff in self.buffs:
            if buff.buffType == BuffType.HotIncrease:
                healIncrease += buff.value

        if healIncrease != 0:
            result = result * (1 + healIncrease)
            result = roundDown(result)

        if result < 0:
            result = 0
        return result

    def increaseDamage(self, damage, seeAsAttack, seeAsSkill):
        result = damage
        # 由自身提升的普攻/必杀伤害增加
        aIncrease = 0
        sIncrease = 0

        # 由自身提升的造成伤害增加
        damageIncrease = 0
        for buff in self.buffs:
            if seeAsAttack and buff.buffType == BuffType.AttackIncrease:
                aIncrease += buff.value
            elif seeAsSkill and buff.buffType == BuffType.SkillIncrease:
                sIncrease += buff.value

            if buff.buffType == BuffType.DamageIncrease:
                damageIncrease += buff.value

        if aIncrease != 0:
            result = result * (1 + aIncrease)
            result = roundDown(result)
        if sIncrease != 0:
            result = result * (1 + sIncrease)
            result = roundDown(result)
        if damageIncrease != 0:
            result = result * (1 + damageIncrease)
            result = roundDown(result)

        if result < 0:
            result = 0
        return result

    def increaseBeDamage(self, damage, enemy, seeAsAttack, seeAsSkill):
        result = damage
        # 由自己提升的受到普攻/必杀伤害
        aIncrease = 0
        sIncrease = 0

        # 由自己提升的受到伤害增加
        damageIncrease = 0
        defenseIncrease = 0.5
        for buff in self.buffs:
            if seeAsAttack and buff.buffType == BuffType.BeAttackIncrease:
                aIncrease += buff.value
            elif seeAsSkill and buff.buffType == BuffType.BeSkillIncrease:
                sIncrease += buff.value

            if buff.buffType == BuffType.BeDamageIncrease:
                damageIncrease += buff.value
            if buff.buffType == BuffType.DefenseDamageReduction:
                defenseIncrease += buff.value

        if self.defense:
            damageIncrease -= defenseIncrease

        if aIncrease != 0:
            result = result * (1 + aIncrease)
            result = roundDown(result)
        if sIncrease != 0:
            result = result * (1 + sIncrease)
            result = roundDown(result)
        if damageIncrease != 0:
            result = result * (1 + damageIncrease)
            result = roundDown(result)

        # 属性克制
        if enemy.cardType is not None and self.cardType is not None:
            if self.cardType.isBeRestrained(enemy.cardType):
                result = result * 1.2
                result = roundDown(result)
            elif self.cardType.isRestrained(enemy.cardType):
                result = result * 0.8
                result = roundDown(result)

        if result < 0:
            result = 0
        return result

    def calDamage(self, _atk, _magnification, seeAsAttack, seeAsSkill):
        damage = _atk * _magnification
        damage = roundDown(damage)
        damage = self.increaseDamage(damage, seeAsAttack, seeAsSkill)
        return damage

    def increaseShield(self, shield):
        result = shield
        increase = 0
        effectIncrease = 0
        for buff in self.buffs:
            if buff.buffType == BuffType.ShieldIncrease:
                increase += buff.value
            if buff.buffType == BuffType.ShieldEffectIncrease:
                effectIncrease += buff.value

        if increase != 0:
            result = result * (1 + increase)
            result = roundDown(result)
        if effectIncrease != 0:
            result = result * (1 + effectIncrease)
            result = roundDown(result)

        if result < 0:
            result = 0
        return result

    def increaseBeShield(self, shield):
        result = shield
        increase = 0
        for buff in self.buffs:
            if buff.buffType == BuffType.BeShieldIncrease:
                increase += buff.value

        if increase != 0:
            result = result * (1 + increase)
            result = roundDown(result)

        if result < 0:
            result = 0
        return result

    def isTaunt(self):
        for buff in self.buffs:
            if buff.buffType == BuffType.Taunt:
                return True
        return False

    def disTauntWhenBeAttacked(self):
        tauntBuff = None
        disTaunt = False
        for buff in self.buffs:
            if buff.buffType == BuffType.Taunt:
                tauntBuff = buff
            elif buff.buffType == BuffType.DisTaunt and buff.conditionType == ConditionType.WhenBeAttacked:
                disTaunt = True
        if disTaunt and tauntBuff is not None:
            self.buffs.remove(tauntBuff)

    # 必杀技
    # 必杀伤害结算：攻击力*倍率*[造成伤害增加*必杀伤害增加(来源于自身)]*[目标受必杀伤害增加*目标受伤害增加*属性克制(1.2/1/0.8)(来源于敌方)]
    def skill(self, enemy):
        pass

    def skillAfter(self, enemy):
        pass

    # 普攻
    # 普攻伤害结算：攻击力*倍率*[造成伤害增加*普攻伤害增加(来源于自身)]*[目标受普攻伤害增加*目标受伤害增加*属性克制(1.2/1/0.8)(来源于敌方)]
    def attack(self, enemy):
        pass

    def attackAfter(self, enemy):
        pass

    # 3星被动
    def passive_star_3(self):
        if self.star >= 3:
            return True
        return False

    # 5星被动
    def passive_star_5(self):
        if self.star >= 5:
            return True
        return False

    # 信息
    def cardInfo(self, printInfo=True):
        infoStr = self.cardName
        if self.role is not None:
            infoStr = '{} - {}'.format(self.cardName, self.role.value)
        if printInfo:
            print(infoStr, end='')
        return infoStr

    def cardDetail(self):
        self.cardInfo()
        print()
        print(
            '等级：{}\n生命值：{}\n攻击力：{}\n蜜话：{}\n潜能：{}'.format(self.lv, self.hp, self.atk, self.bond, self.tier))

    # 是否已阵亡
    def isDead(self):
        if self.hpCurrent <= 0:
            return True
        return False

    # 是否可以释放技能
    def canSkill(self):
        if self.skillCount >= self.skillCD:
            return True
        return False

    def nextRound(self):
        self.skillCount += 1
        self.defense = False
        removeBuffs: list[Buff] = []
        for buff in self.buffs:
            buff.nextRound()
            if buff.isOver():
                removeBuffs.append(buff)

        for buff in removeBuffs:
            self.buffs.remove(buff)

        removeBuffs.clear()

    def addBuff(self, buff, _source=None):
        if _source is not None:
            buff.source = _source
        else:
            buff.source = self
        self.buffs.append(buff)

    def beAttacked(self, damage, seeAsBeAttacked):
        removeBuffs: list[Buff] = []
        result = damage
        for buff in self.buffs:
            if buff.buffType == BuffType.Shield:
                if buff.value > result:
                    buff.value -= result
                    result = 0
                elif buff.value == result:
                    removeBuffs.append(buff)
                    result = 0
                else:
                    removeBuffs.append(buff)
                    result -= buff.value

        for buff in removeBuffs:
            self.buffs.remove(buff)

        self.hpCurrent -= result
        return 0

    def beHealed(self, heal, seeAsHeal):
        self.hpCurrent += heal
        if self.hpCurrent > self.maxHp:
            self.hpCurrent = self.maxHp

    def calBuffCount(self, _buffId):
        count = 0
        for buff in self.buffs:
            if buff.buffId == _buffId:
                count += 1
        return count
