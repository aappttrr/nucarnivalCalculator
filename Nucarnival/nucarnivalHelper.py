import io
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from RoleCards.common.card import ICard, roundDown
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.conditionTypeEnum import ConditionType
from Common.ncRound import roundHalfEven


class NucarnivalHelper:
    def __init__(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.maxTurn = 50
        self.defenseTurn = {}
        self.skillTurn = {}
        self.damageRecord = {}
        self.damageRecord_attack = {}
        self.damageRecord_skill = {}
        self.damageRecord_dot = {}
        self.damageRecord_counter = {}
        self.counterRecord = {}
        self.turnDamageRecord = {}
        self.currentTurn = 0
        self.totalDamage = 0
        self.output = io.StringIO()
        self.wb: Workbook = None
        self.ws: Worksheet = None
        self.markBattleResult = False
        self.sheetCount = 0

    def clearUp(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.maxTurn = 50
        self.defenseTurn = {}
        self.skillTurn = {}
        self.clearUpBattleResult()

    def clearUpBattleResult(self):
        self.damageRecord = {}
        self.damageRecord_attack = {}
        self.damageRecord_skill = {}
        self.damageRecord_dot = {}
        self.damageRecord_counter = {}
        self.counterRecord = {}
        self.turnDamageRecord = {}
        self.currentTurn = 0
        self.totalDamage = 0
        self.output.close()
        self.output = io.StringIO()
        self.sheetCount += 1
        if self.wb is not None and self.ws is not None and self.markBattleResult is False:
            self.wb.remove_sheet(self.ws)
            self.sheetCount -= 1
            self.ws = None
        if self.wb is None:
            self.wb = Workbook()
            self.ws = self.wb.active
            self.ws.title = '伤害模拟结果' + str(self.sheetCount)
        if self.ws is None:
            self.ws = self.wb.create_sheet('伤害模拟结果' + str(self.sheetCount), 0)

    def recordDamage(self, role: ICard, damage, damageType:int):
        record = damage
        if role in self.damageRecord:
            oldDamage = self.damageRecord[role]
            record += oldDamage
        self.damageRecord[role] = record
        record2 = damage
        match damageType:
            case 0:
                if role in self.damageRecord_attack:
                    oldDamage2 = self.damageRecord_attack[role]
                    record2 += oldDamage2
                self.damageRecord_attack[role] = record2
            case 1:
                if role in self.damageRecord_skill:
                    oldDamage2 = self.damageRecord_skill[role]
                    record2 += oldDamage2
                self.damageRecord_skill[role] = record2
            case 2:
                if role in self.damageRecord_dot:
                    oldDamage2 = self.damageRecord_dot[role]
                    record2 += oldDamage2
                self.damageRecord_dot[role] = record2
            case 3:
                if role in self.damageRecord_counter:
                    oldDamage2 = self.damageRecord_counter[role]
                    record2 += oldDamage2
                self.damageRecord_counter[role] = record2

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
        self.clearUpBattleResult()

        for role in self.team:
            role.teamMate = self.team
            role.enemies = self.monsters
            role.clearUp()
            role.calHpAtk()
        for monster in self.monsters:
            monster.teamMate = self.monsters
            monster.enemies = self.team
            monster.clearUp()
        row = self.writeCardInfoInExcel()
        row += 1

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
            self.ws.cell(row, turn + 1, '第{0}回合'.format(turn))
            self.recordBattleMsg(msg)
            if printInfo:
                print(msg)

            # 我方行动
            self.action(turn, self.team, self.monsters, row, printInfo, False)

            self.settleDotAndHot(self.team, row, printInfo, False)

            self.counter(self.monsters, self.team, row, printInfo, True)

            self.counterRecord.clear()

            # 敌方行动
            self.action(turn, self.monsters, self.team, row, printInfo, True)

            self.settleDotAndHot(self.monsters, row, turn, printInfo, True)

            self.counter(self.team, self.monsters, row, turn, printInfo, False)

            self.counterRecord.clear()

            # 下个回合
            tempRow = row + 1
            for role in self.team:
                role.nextRound()
                if turn in self.turnDamageRecord:
                    tempDamageRecord = self.turnDamageRecord[turn]
                    if role in tempDamageRecord:
                        record = tempDamageRecord[role]
                        cellMsg = self.ws.cell(tempRow, turn + 1).value
                        if cellMsg is None:
                            cellMsg = '回合总伤害：' + str(record)
                        else:
                            cellMsg += '\n回合总伤害：' + str(record)
                        self.ws.cell(tempRow, turn + 1, cellMsg)
                tempRow += 1
            for monster in self.monsters:
                monster.nextRound()

        msg = '-----------结束------------'
        self.recordBattleMsg(msg)
        if printInfo:
            print(msg)
        self.totalDamage = 0
        self.ws.cell(row, turn + 2, '总伤害')
        self.ws.cell(row, turn + 3, '伤害占比')
        temp = 1
        for role in self.team:
            self.ws.cell(row + temp, 1, role.cardInfo(False))
            if role in self.damageRecord:
                self.totalDamage += self.damageRecord[role]
                msg = '总{}回合，{} 总伤害为：{}'.format(turn, role.cardInfo(False), self.damageRecord[role])
                msg2 = '{}输出占比为：'.format(role.cardInfo(False))
                msg3 = ''
                self.recordBattleMsg(msg)
                self.ws.cell(row + temp, turn + 2, str(self.damageRecord[role]))
                if self.damageRecord[role] > 0:
                    if role in self.damageRecord_attack:
                        if self.damageRecord_attack[role] > 0:
                            damageProportion = self.damageRecord_attack[role] / self.damageRecord[role] * 100
                            damageProportion = roundHalfEven(damageProportion)
                            msg2 += '普攻（' + str(damageProportion) + '%）'
                            if len(msg3) != 0:
                                msg3 += '\n'
                            msg3 += '普攻占比（' + str(damageProportion) + '%）'
                    if role in self.damageRecord_skill:
                        if self.damageRecord_skill[role] > 0:
                            damageProportion = self.damageRecord_skill[role] / self.damageRecord[role] * 100
                            damageProportion = roundHalfEven(damageProportion)
                            msg2 += '必杀（' + str(damageProportion) + '%）'
                            if len(msg3) != 0:
                                msg3 += '\n'
                            msg3 += '必杀占比（' + str(damageProportion) + '%）'
                    if role in self.damageRecord_dot:
                        if self.damageRecord_dot[role] > 0:
                            damageProportion = self.damageRecord_dot[role] / self.damageRecord[role] * 100
                            damageProportion = roundHalfEven(damageProportion)
                            msg2 += '持续伤害（' + str(damageProportion) + '%）'
                            if len(msg3) != 0:
                                msg3 += '\n'
                            msg3 += '持续伤害占比（' + str(damageProportion) + '%）'
                    if role in self.damageRecord_counter:
                        if self.damageRecord_counter[role] > 0:
                            damageProportion = self.damageRecord_counter[role] / self.damageRecord[role] * 100
                            damageProportion = roundHalfEven(damageProportion)
                            msg2 += '反击（' + str(damageProportion) + '%）'
                            if len(msg3) != 0:
                                msg3 += '\n'
                            msg3 += '反击占比（' + str(damageProportion) + '%）'

                if printInfo:
                    print(msg)
                    print(msg2)
                self.ws.cell(row + temp, turn + 3, msg3)
                self.recordBattleMsg(msg3)

            temp += 1
        msg = '总{}回合，整个队伍伤害：{}'.format(turn, self.totalDamage)
        self.ws.cell(row + temp, turn + 2, str(self.totalDamage))
        self.recordBattleMsg(msg)
        if printInfo:
            print(msg)

    # 行动
    # 防御/普攻/必杀
    # 结算dot
    # 结算hot
    def action(self, turn=0, cardList: list[ICard] = [], cardList2: list[ICard] = [], defaultRow=0, printInfo=False,
               isEnemy=False):
        row = defaultRow + 1
        for role in cardList:
            if role in self.defenseTurn and turn in self.defenseTurn[role]:
                role.defense = True
                msg = role.cardInfo(False) + '  防御'
                if isEnemy is False:
                    self.ws.cell(row, turn + 1, '防御')
                    self.recordBattleMsg(msg)
                if printInfo and isEnemy is False:
                    print(msg)

            if role.defense:
                continue

            isAttack = True
            monster = cardList2[0]
            for card2 in cardList2:
                if card2.isTaunt():
                    monster = card2
                    break

            if role in self.skillTurn:
                if turn in self.skillTurn[role] and role.canSkill():
                    isAttack = False
            else:
                if role.canSkill():
                    isAttack = False

            if isAttack:
                damage = self.doAttack(role, monster, cardList2, row, turn, printInfo, isEnemy)
                role.doBloodSuck(damage)
                if isEnemy is False:
                    self.recordDamage(role, damage, 0)
            else:
                damage = self.doSkill(role, monster, cardList2, row, turn, printInfo, isEnemy)
                role.doBloodSuck(damage)
                if isEnemy is False:
                    self.recordDamage(role, damage, 1)
            row += 1

    def settleDotAndHot(self, cardList: list[ICard] = [], defaultRow=0, turn=0, printInfo=False, isEnemy=False):
        # 结算dot
        for role in cardList:
            dotDamages = role.settleDot()
            if len(dotDamages) > 0:
                totalDamage = 0
                for source in dotDamages:
                    dotDamage = dotDamages[source]
                    totalDamage += dotDamage
                    if isEnemy:
                        if source in self.team:
                            row = self.team.index(source) + defaultRow + 1
                            cellMsg = self.ws.cell(row, turn + 1).value
                            if cellMsg is None:
                                cellMsg = '持续伤害：' + str(dotDamage)
                            else:
                                cellMsg += '\n持续伤害：' + str(dotDamage)
                            self.ws.cell(row, turn + 1, cellMsg)
                        self.recordDamage(source, dotDamage, 2)
                    msg = '{}造成了持续伤害：{}'.format(source.cardInfo(False), dotDamage)
                    if isEnemy:
                        self.recordBattleMsg(msg)
                    if printInfo and isEnemy:
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
                    if isEnemy is False:
                        self.recordBattleMsg(msg)
                    if printInfo and isEnemy is False:
                        print(msg)
                role.beHealed(totalHeal, False)

    # 反击
    def counter(self, cardList: list[ICard] = [], cardList2: list[ICard] = [], defaultRow=0, turn=0, printInfo=False,
                isEnemy=False):
        row = defaultRow + 1
        for role in cardList:
            if role in self.counterRecord and self.counterRecord[role] is not None:
                damage = self.doCounter(role, self.counterRecord[role], cardList2)
                role.doBloodSuck(damage)
                if damage > 0:
                    if isEnemy is False:
                        cellMsg = self.ws.cell(row, turn + 1).value
                        if cellMsg is None:
                            cellMsg = '反击：' + str(damage)
                        else:
                            cellMsg += '\n反击：' + str(damage)
                        self.ws.cell(row, turn + 1, cellMsg)
                        self.recordDamage(role, damage, 3)
                    msg = role.cardInfo(False) + '  反击造成伤害：' + str(damage)
                    if isEnemy is False:
                        self.recordBattleMsg(msg)
                    if printInfo and isEnemy is False:
                        print(msg)
            row += 1

    def doCounter(self, role: ICard, monster: ICard, cardList2: list[ICard] = []):
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
                totalDamage += self.groupDamage(counterDamage, role, monster, cardList2, buff.isGroup, buff.seeAsAttack,
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
    def doSkill(self, role: ICard, monster: ICard, cardList2: list[ICard] = [], row=0, turn=0, printInfo=False,
                isEnemy=False):
        role.skillCount = 0
        damage = role.skill(monster)
        damage2 = self.groupDamage(damage, role, monster, cardList2, role.isGroup, False, True, True)
        totalDamage = damage2
        # 必杀时追击
        fuDamage = self.followUp(role, monster, cardList2, False)
        totalDamage += fuDamage
        damageStr = str(damage2)
        if fuDamage > 0:
            damageStr = '(' + str(damage2) + ',' + str(fuDamage) + ') = ' + str(totalDamage)
        msg = role.cardInfo(False) + '  必杀造成伤害：' + damageStr
        if isEnemy is False:
            cellMsg = self.ws.cell(row, turn + 1).value
            if cellMsg is None:
                cellMsg = '必杀：' + damageStr
            else:
                cellMsg += '\n必杀：' + damageStr
            self.ws.cell(row, turn + 1, cellMsg)
            self.recordBattleMsg(msg)
        if printInfo and isEnemy is False:
            print(msg)
        role.skillAfter(monster)
        if totalDamage > 0:
            monster.beAttackedAfter(True)
        return totalDamage

    # 普攻
    def doAttack(self, role: ICard, monster: ICard, cardList2: list[ICard] = [], row=0, turn=0, printInfo=False,
                 isEnemy=False):
        damage = role.attack(monster)
        damage2 = self.groupDamage(damage, role, monster, cardList2, role.isGroup, True, False, True)

        totalDamage = damage2
        # 普攻时追击
        fuDamage = self.followUp(role, monster, cardList2, True)
        totalDamage += fuDamage
        damageStr = str(damage2)
        if fuDamage > 0:
            damageStr = '(' + str(damage2) + ',' + str(fuDamage) + ') = ' + str(totalDamage)

        msg = role.cardInfo(False) + '  普攻造成伤害：' + damageStr
        if isEnemy is False:
            cellMsg = self.ws.cell(row, turn + 1).value
            if cellMsg is None:
                cellMsg = '普攻：' + damageStr
            else:
                cellMsg += '\n普攻：' + damageStr
            self.ws.cell(row, turn + 1, cellMsg)
            self.recordBattleMsg(msg)
        if printInfo and isEnemy is False:
            print(msg)

        role.attackAfter(monster)
        if totalDamage > 0:
            monster.beAttackedAfter(True)
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

    def writeCardInfoInExcel(self):
        self.ws.cell(1, 1, '名称')
        self.ws.cell(1, 2, '昵称')
        self.ws.cell(1, 3, '角色')
        self.ws.cell(1, 4, '属性')
        self.ws.cell(1, 5, '定位')
        self.ws.cell(1, 6, 'Hp')
        self.ws.cell(1, 7, 'Atk')
        self.ws.cell(1, 8, '等级')
        self.ws.cell(1, 9, '星级')
        self.ws.cell(1, 10, '潜能')
        self.ws.cell(1, 11, '蜜话')

        row = 2
        for role in self.team:
            if role.cardName == '临时队友':
                continue
            self.ws.cell(row, 1, role.cardName)
            self.ws.cell(row, 2, role.nickName)
            self.ws.cell(row, 3, role.role.value)
            self.ws.cell(row, 4, role.cardType.typeName)
            self.ws.cell(row, 5, role.occupation.occupationName)
            self.ws.cell(row, 6, role.hp)
            self.ws.cell(row, 7, role.atk)
            self.ws.cell(row, 8, role.lv)
            self.ws.cell(row, 9, role.star)
            self.ws.cell(row, 10, role.tier)
            self.ws.cell(row, 11, role.bond)
            row += 1
        return row

    def exportExcel(self, filePath):
        self.wb.save(filePath)
        self.wb.close()
        self.wb = None
