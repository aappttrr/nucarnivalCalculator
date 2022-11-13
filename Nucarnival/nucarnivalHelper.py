import io

from openpyxl import Workbook

from RoleCards.common.card import ICard, roundDown
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.conditionTypeEnum import ConditionType


class NucarnivalHelper:
    def __init__(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.forcedCDAlignment: ICard = None
        self.maxTurn = 50
        self.defenseTurn: list[int] = []
        self.damageRecord = {}
        self.counterRecord = {}
        self.turnDamageRecord = {}
        self.currentTurn = 0
        self.totalDamage = 0
        self.output = io.StringIO()

    def clearUp(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.forcedCDAlignment: ICard = None
        self.maxTurn = 50
        self.defenseTurn: list[int] = []
        self.damageRecord = {}
        self.counterRecord = {}
        self.turnDamageRecord = {}
        self.currentTurn = 0
        self.totalDamage = 0

    def recordDamage(self, role: ICard, damage):
        record = damage
        if role in self.damageRecord:
            oldDamage = self.damageRecord[role]
            record += oldDamage
        self.damageRecord[role] = record

        tempDamageRecord = {}
        if self.currentTurn in self.turnDamageRecord:
            tempDamageRecord = self.turnDamageRecord[self.currentTurn]
            if role in tempDamageRecord:
                damage += tempDamageRecord[role]
        tempDamageRecord[role] = damage
        self.turnDamageRecord[self.currentTurn] = tempDamageRecord

    def recordBattleMsg(self, msg: str):
        self.output.seek(0, 2)
        self.output.write(msg + '\n')

    # 战斗开始
    # 双方清除旧buff、添加队友和敌方信息
    # 激活双方buff
    # 我方行动：防御/普攻/必杀 -> 结算dot ->结算hot
    # 敌方行动：防御/普攻/必杀 -> 结算dot ->结算hot
    # 我方全部阵亡/敌方全部阵亡-> 退出战斗
    def battleStart(self, printInfo=False):
        self.output.close()
        self.output = io.StringIO()
        for role in self.team:
            role.teamMate = self.team
            role.enemies = self.monsters
            role.clearUp()
        for monster in self.monsters:
            monster.teamMate = self.monsters
            monster.enemies = self.team
            monster.clearUp()

        self.damageRecord.clear()
        self.turnDamageRecord.clear()
        self.maxTurn += 1
        if self.maxTurn > 50:
            self.maxTurn = 50
        elif self.maxTurn < 1:
            self.maxTurn = 1

        msg = '-----------开始------------'
        self.recordBattleMsg(msg)
        if printInfo:
            print(msg)

        for turn in range(0, self.maxTurn):
            self.currentTurn = turn
            if turn == 0:
                for role in self.team:
                    role.activeBuffs()
                for tempMonster in self.monsters:
                    tempMonster.activeBuffs()
                for role in self.team:
                    role.calMaxHp()
                for tempMonster in self.monsters:
                    tempMonster.calMaxHp()
                continue

            msg = '---------第{0}回合---------'.format(turn)
            self.recordBattleMsg(msg)
            if printInfo:
                print(msg)

            # 我方行动
            self.action(turn, self.team, self.monsters, printInfo, False)

            self.settleDotAndHot(self.team, printInfo, False)

            self.counter(self.monsters, self.team, printInfo, True)

            self.counterRecord.clear()

            # 敌方行动
            self.action(turn, self.monsters, self.team, printInfo, True)

            self.settleDotAndHot(self.monsters, printInfo, True)

            self.counter(self.team, self.monsters, printInfo, False)

            self.counterRecord.clear()

            # 下个回合
            for role in self.team:
                role.nextRound()
            for monster in self.monsters:
                monster.nextRound()

        msg = '-----------结束------------'
        self.recordBattleMsg(msg)
        if printInfo:
            print(msg)
        self.totalDamage = 0
        for role in self.team:
            if role in self.damageRecord:
                self.totalDamage += self.damageRecord[role]
                msg = '总{}回合，{} 总伤害为：{}'.format(turn, role.cardInfo(False), self.damageRecord[role])
                self.recordBattleMsg(msg)
                if printInfo:
                    print(msg)
        msg = '总{}回合，整个队伍伤害：{}'.format(turn, self.totalDamage)
        self.recordBattleMsg(msg)
        if printInfo:
            print(msg)

    # 行动
    # 防御/普攻/必杀
    # 结算dot
    # 结算hot
    def action(self, turn=0, cardList: list[ICard] = [], cardList2: list[ICard] = [], printInfo=False, isEnemy=False):
        if turn in self.defenseTurn and isEnemy is False :
            for role in cardList:
                role.defense = True
                msg = role.cardInfo(False) + '  防御'
                self.recordBattleMsg(msg)
                if printInfo and isEnemy is False:
                    print(msg)
        else:
            for role in cardList:
                isAttack = True
                monster = cardList2[0]
                for card2 in cardList2:
                    if card2.isTaunt():
                        monster = card2
                        break

                if self.forcedCDAlignment is not None:
                    if self.forcedCDAlignment.canSkill() and role.canSkill():
                        isAttack = False
                else:
                    if role.canSkill():
                        isAttack = False

                if isAttack:
                    damage = self.doAttack(role, monster, cardList2, printInfo, isEnemy)
                    role.doBloodSuck(damage)
                    if isEnemy is False:
                        self.recordDamage(role, damage)
                else:
                    damage = self.doSkill(role, monster, cardList2, printInfo, isEnemy)
                    role.doBloodSuck(damage)
                    if isEnemy is False:
                        self.recordDamage(role, damage)

    def settleDotAndHot(self, cardList: list[ICard] = [], printInfo=False, isEnemy=False):
        # 结算dot
        for role in cardList:
            dotDamages = role.settleDot()
            if len(dotDamages) > 0:
                totalDamage = 0
                for source in dotDamages:
                    dotDamage = dotDamages[source]
                    totalDamage += dotDamage
                    if isEnemy:
                        self.recordDamage(source, dotDamage)
                    msg = '{}造成了持续伤害：{}'.format(source.cardInfo(False), dotDamage)
                    self.recordBattleMsg(msg)
                    if printInfo and isEnemy is True:
                        print(msg)
                role.beAttacked(totalDamage, False)

        # 结算hot
        for role in cardList:
            hotHeals = role.settleHot()
            if len(hotHeals) > 0:
                totalHeal = 0
                for source in hotHeals:
                    hotHeal = hotHeals[source]
                    totalHeal += hotHeal
                    msg = '{}受到了来自{}的持续治疗：{}'.format(role.cardInfo(False), source.cardInfo(False), hotHeal)
                    self.recordBattleMsg(msg)
                    if printInfo and isEnemy is False:
                        print(msg)
                role.beHealed(totalHeal, False)

    # 反击
    def counter(self, cardList: list[ICard] = [], cardList2: list[ICard] = [], printInfo=False, isEnemy=False):
        for role in cardList:
            if role in self.counterRecord and self.counterRecord[role] is not None:
                damage = self.doCounter(role,self.counterRecord[role], cardList2)
                role.doBloodSuck(damage)
                if damage > 0:
                    if isEnemy is False:
                        self.recordDamage(role, damage)
                    msg = role.cardInfo(False) + '  反击造成伤害：' + str(damage)
                    self.recordBattleMsg(msg)
                    if printInfo and isEnemy is False:
                        print(msg)

    def doCounter(self, role: ICard,monster:ICard, cardList2: list[ICard] = []):
        totalDamage = 0
        currentAtk = role.getCurrentAtk()
        for buff in role.buffs:
            if buff.buffType != BuffType.CounterAttack:
                continue
            if buff.conditionType:
                if buff.useBaseAtk:
                    counterDamage = role.atk * buff.value
                else:
                    counterDamage = currentAtk * buff.value
                counterDamage = roundDown(counterDamage)
                counterDamage = role.increaseDamage(counterDamage, buff.seeAsAttack, buff.seeAsSkill)
                totalDamage += self.groupDamage(counterDamage, role,monster, cardList2, buff.isGroup, buff.seeAsAttack,
                                                buff.seeAsSkill)
        return totalDamage

    # 追击
    def followUp(self, role: ICard, monster: ICard, cardList2: list[ICard] = [], isAttack=True):
        totalDamage = 0
        currentAtk = role.getCurrentAtk()
        for buff in role.buffs:
            if buff.buffType != BuffType.FollowUpAttack:
                continue

            doFollowUp = False
            if isAttack and buff.conditionType == ConditionType.WhenAttack:
                doFollowUp = True
            elif isAttack is False and buff.conditionType == ConditionType.WhenSkill:
                doFollowUp = True
            if doFollowUp is False:
                continue

            if buff.useBaseAtk:
                followUpDamage = role.atk * buff.value
            else:
                followUpDamage = currentAtk * buff.value
            followUpDamage = roundDown(followUpDamage)
            followUpDamage = role.increaseDamage(followUpDamage, buff.seeAsAttack, buff.seeAsSkill)
            totalDamage += self.groupDamage(followUpDamage, role, monster, cardList2, buff.isGroup, buff.seeAsAttack,
                                            buff.seeAsSkill, True)
        return totalDamage

    # 必杀
    def doSkill(self, role: ICard, monster: ICard, cardList2: list[ICard] = [], printInfo=False, isEnemy=False):
        role.skillCount = 0
        damage = role.skill(monster)
        totalDamage = self.groupDamage(damage, role, monster, cardList2, role.isGroup, False, True, True)

        # 必杀时追击
        fuDamage = self.followUp(role, monster, cardList2, False)
        totalDamage += fuDamage
        damageStr = str(damage)
        if fuDamage > 0:
            damageStr = '(' + str(damage) + ',' + str(fuDamage) + ') = ' + str(totalDamage)
        msg = role.cardInfo(False) + '  必杀造成伤害：' + damageStr
        self.recordBattleMsg(msg)
        if printInfo and isEnemy is False:
            print(msg)
        role.skillAfter(monster)
        return totalDamage

    # 普攻
    def doAttack(self, role: ICard, monster: ICard, cardList2: list[ICard] = [], printInfo=False, isEnemy=False):
        damage = role.attack(monster)
        totalDamage = self.groupDamage(damage, role, monster, cardList2, role.isGroup, True, False, True)

        # 普攻时追击
        fuDamage = self.followUp(role, monster, cardList2, True)
        totalDamage += fuDamage
        damageStr = str(damage)
        if fuDamage > 0:
            damageStr = '(' + str(damage) + ',' + str(fuDamage) + ') = ' + str(totalDamage)

        msg = role.cardInfo(False) + '  普攻造成伤害：' + damageStr
        self.recordBattleMsg(msg)
        if printInfo and isEnemy is False:
            print(msg)

        role.attackAfter(monster)
        return totalDamage

    def groupDamage(self, damage, role: ICard, monster: ICard, cardList2: list[ICard] = [], isGroup=False,
                    seeAsAttack=False,
                    seeAsSkill=False, isAttackOrSkill=False):
        totalDamage = 0
        # 暗奥特殊处理
        if role.cardId == 'RadiantAdmiral':
            size = len(cardList2)
            monster1 = cardList2[0]
            monster2 = cardList2[0]
            monster3 = cardList2[0]
            if size >= 5:
                monster2 = cardList2[2]
                monster3 = cardList2[4]
            elif size >= 3:
                monster2 = cardList2[2]

            temp1 = monster1.increaseBeDamage(damage, role, seeAsAttack, seeAsSkill)
            totalDamage += temp1
            monster1.beAttacked(temp1, True)
            if isAttackOrSkill:
                monster1.disTauntWhenBeAttacked()
                self.counterRecord[monster1] = role

            temp2 = monster2.increaseBeDamage(damage, role, seeAsAttack, seeAsSkill)
            totalDamage += temp2
            monster2.beAttacked(temp2, True)
            if isAttackOrSkill:
                monster2.disTauntWhenBeAttacked()
                self.counterRecord[monster2] = role

            temp3 = monster3.increaseBeDamage(damage, role, seeAsAttack, seeAsSkill)
            totalDamage += temp3
            monster3.beAttacked(temp3, True)
            if isAttackOrSkill:
                monster3.disTauntWhenBeAttacked()
                self.counterRecord[monster3] = role
            return totalDamage

        if isGroup:
            for tempMonster in cardList2:
                temp = tempMonster.increaseBeDamage(damage, role, seeAsAttack, seeAsSkill)
                totalDamage += temp
                tempMonster.beAttacked(temp, True)
                if isAttackOrSkill:
                    tempMonster.disTauntWhenBeAttacked()
                    self.counterRecord[tempMonster] = role
        else:
            temp = monster.increaseBeDamage(damage, role, seeAsAttack, seeAsSkill)
            totalDamage += temp
            monster.beAttacked(temp, True)
            if isAttackOrSkill:
                monster.disTauntWhenBeAttacked()
                self.counterRecord[monster] = role
        return totalDamage

    def exportExcel(self, fileName, filePath):
        wb = Workbook()

        ws = wb.create_sheet(fileName, 0)

        for i in range(0, len(self.team)):
            role = self.team[i]
            row = i + 2
            ws.cell(row, 1, role.cardInfo(False))
            ws.cell(row, self.maxTurn + 1, self.damageRecord[role])

        for j in range(1, self.maxTurn):
            column = j + 1
            ws.cell(1, column, '第{}回合'.format(j))

            turnDamage = 0
            for i in range(0, len(self.team)):
                role = self.team[i]
                row = i + 2

                record = 0
                if j in self.turnDamageRecord:
                    tempDamageRecord = self.turnDamageRecord[j]
                    if role in tempDamageRecord:
                        record += tempDamageRecord[role]
                turnDamage += record
                ws.cell(row, column, record)

            ws.cell(len(self.team) + 2, column, turnDamage)

        ws.cell(1, self.maxTurn + 1, '总计')
        ws.cell(len(self.team) + 2, 1, '全队伤害')
        ws.cell(len(self.team) + 2, self.maxTurn + 1, self.totalDamage)

        wb.save(filePath)
