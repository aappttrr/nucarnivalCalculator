import io
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from Common.nvEventManager import EventListener, Event, EventType, eventManagerInstance
from RoleCards.common.card import ICard, writeCardInfoTitleInExcel
from RoleCards.enum.buffTypeEnum import BuffType
from RoleCards.enum.conditionTypeEnum import ConditionType
from Common.ncRound import roundHalfEven, roundDown


# 索敌
def seizeEnemy(role: ICard, enemies: list[ICard], targetEnemy: ICard = None):
    if role.cardId == 'RadiantAdmiral':
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
    if role.isGroup:
        return enemies
    else:
        enemy = enemies[0]
        temp1 = [x for x in enemies if x.isTaunt()]
        if len(temp1) > 0:
            enemy = temp1[0]
            for temp in temp1:
                if temp.hpCurrent > enemy.hpCurrent:
                    enemy = temp
        else:
            if targetEnemy is not None:
                return targetEnemy
            for temp in enemies:
                if temp.hpCurrent > enemy.hpCurrent:
                    enemy = temp
        return enemy


class NucarnivalHelper:
    def __init__(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.maxTurn = 50
        self.defenseTurn = {}
        self.skillTurn = {}
        self.currentTurn = 0
        self.totalDamage = 0
        self.output = io.StringIO()
        self.wb: Workbook = None
        self.ws: Worksheet = None
        self.markBattleResult = False
        self.sheetCount = 0
        self.battleListener = BattleRecordListener()
        eventManagerInstance.addListener(self.battleListener)

    def clearUp(self):
        self.team: list[ICard] = []
        self.monsters: list[ICard] = []
        self.maxTurn = 50
        self.defenseTurn = {}
        self.skillTurn = {}
        self.clearUpBattleResult()

    def clearUpBattleResult(self):
        self.battleListener.cleanUp()
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

        if self.maxTurn > 50:
            self.maxTurn = 50
        elif self.maxTurn < 1:
            self.maxTurn = 1

        msg = '-----------开始------------'
        self.recordBattleMsg(msg)

        for turn in range(0, self.maxTurn + 1):
            self.currentTurn = turn
            self.battleListener.currentTurn = turn
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

            if turn > 1:
                self.recordBattleMsg('')
            msg = '---------第{0}回合---------'.format(turn)
            self.ws.merge_cells(None, row, turn * 2, row, turn * 2 + 1)
            self.ws.cell(row, turn * 2, '第{0}回合'.format(turn))
            self.recordBattleMsg(msg)

            # 我方行动
            self.action(turn, self.team, self.monsters)

            for role in self.team:
                role.settleDot()
                role.settleHot()

            # 敌方行动
            self.action(turn, self.monsters, self.team)

            for role in self.monsters:
                role.settleDot()
                role.settleHot()

            # 下个回合
            tempRow = row + 1
            for role in self.team:
                if tempRow > row + 1:
                    self.recordBattleMsg('')
                self.recordResult(role, turn, tempRow)
                role.nextRound()
                tempRow += 1
            for monster in self.monsters:
                monster.nextRound()

        msg = '-----------结束------------'
        self.recordBattleMsg(msg)
        self.totalDamage = 0
        self.ws.cell(row, turn * 2 + 2, '总伤害')
        self.ws.cell(row, turn * 2 + 3, '伤害占比')
        self.ws.cell(row, turn * 2 + 4, '总治疗')
        self.ws.cell(row, turn * 2 + 5, '治疗占比')
        temp = 1
        self.recordBattleMsg('总{}回合'.format(turn))
        totalDamage = 0
        for role in self.team:
            self.ws.cell(row + temp, 1, role.cardInfo(False))
            if temp != 1:
                self.recordBattleMsg('')
            totalDamage += self.recordTotalResult(role, turn, row + temp)
            temp += 1
        msg = '全队伤害：{}'.format(totalDamage)
        self.ws.cell(row + temp,  turn * 2 + 2, str(totalDamage))
        self.recordBattleMsg(msg)
        if printInfo:
            print(self.output.getvalue())

    # 获取本回合总伤害
    def recordResult(self, role: ICard, turn, row):
        msg = role.cardInfo(False)
        msg2 = ''
        isDefense = False

        turnAtk = role.getCurrentAtk()
        eventAtk = Event(EventType.turnAtk)
        eventAtk.data['source'] = role
        eventAtk.data['value'] = turnAtk
        eventAtk.data['target'] = role
        eventManagerInstance.sendEvent(eventAtk)

        atkMag = '行动实时攻击力：'
        atkAfterMag = '行动后实时攻击力：'
        atkTurnMag = '回合实时攻击力：{}'.format(turnAtk)

        if len(self.battleListener.findSourceEvent(role, EventType.actionAtk)) > 0:
            try:
                actionAtk = self.battleListener.findSourceEvent(role, EventType.actionAtk)[0].value
                msg += '[{}]'.format(actionAtk)
                atkMag += str(actionAtk)
            except:
                print('获取行动实时攻击力记录出错')

        if len(self.battleListener.findSourceEvent(role, EventType.defense)) > 0:
            msg += '  防御'
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 = '防御'
            isDefense = True

        attackDamage = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackDamage):
            try:
                attackDamage += record.value
            except:
                print('获取普攻记录出错')
        attackFU = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackFollowUp):
            try:
                attackFU += record.value
            except:
                print('获取普攻追击记录出错')
        attackHeal = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackHeal):
            try:
                attackHeal += record.value
            except:
                print('获取普攻治疗记录出错')
        skillDamage = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillDamage):
            try:
                skillDamage += record.value
            except:
                print('获取必杀记录出错')
        skillFU = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillFollowUp):
            try:
                skillFU += record.value
            except:
                print('获取必杀追击记录出错')
        skillHeal = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillHeal):
            try:
                skillHeal += record.value
            except:
                print('获取必杀治疗记录出错')
        dot = 0
        for record in self.battleListener.findSourceEvent(role, EventType.dot):
            try:
                dot += record.value
            except:
                print('获取持续伤害记录出错')
        hot = 0
        for record in self.battleListener.findSourceEvent(role, EventType.hot):
            try:
                hot += record.value
            except:
                print('获取持续治疗记录出错')
        bloodSuck = 0
        for record in self.battleListener.findSourceEvent(role, EventType.bloodSucking):
            try:
                bloodSuck += record.value
            except:
                print('获取吸血记录出错')
        shield = 0
        for record in self.battleListener.findSourceEvent(role, EventType.shield):
            try:
                shield += record.value
            except:
                print('获取护盾记录出错')
        counter = 0
        for record in self.battleListener.findSourceEvent(role, EventType.counter):
            try:
                counter += record.value
            except:
                print('获取反击记录出错')

        turnDamage = attackDamage + attackFU + skillDamage + skillFU + dot + counter
        turnHeal = attackHeal + skillHeal + hot
        if attackDamage > 0:
            astr = str(attackDamage)
            if attackFU > 0:
                astr += '(' + str(attackFU) + ')'
            msg += '  普攻造成伤害：' + astr
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '普攻：' + astr
        else:
            if attackFU > 0:
                msg += '  普攻造成伤害：' + str(attackFU)
                if len(msg2) > 0:
                    msg2 += '\n'
                msg2 += '普攻：' + str(attackFU)
        if counter > 0:
            msg += '  反击造成伤害：' + str(counter)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '反击伤害：' + str(counter)
        if skillDamage > 0:
            astr = str(skillDamage)
            if skillFU > 0:
                astr += '(' + str(skillFU) + ')'
            msg += '  必杀造成伤害：' + astr
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '必杀：' + astr
        else:
            if skillFU > 0:
                msg += '  必杀造成伤害：' + str(skillFU)
                if len(msg2) > 0:
                    msg2 += '\n'
                msg2 += '必杀：' + str(skillFU)
        if attackHeal > 0:
            msg += '  普攻造成治疗：' + str(attackHeal)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '普攻治疗：' + str(attackHeal)
        if skillHeal > 0:
            msg += '  必杀造成治疗：' + str(skillHeal)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '必杀治疗：' + str(skillHeal)
        if bloodSuck > 0:
            msg += '  吸血造成治疗：' + str(bloodSuck)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '吸血：' + str(bloodSuck)
        if dot > 0:
            msg += '  造成持续伤害：' + str(dot)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '持续伤害：' + str(dot)
        if hot > 0:
            msg += '  造成持续治疗：' + str(hot)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '持续治疗：' + str(hot)
        if shield > 0:
            msg += '  造成护盾：' + str(shield)
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '护盾：' + str(shield)
        if turnDamage > 0:
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '回合总伤害：' + str(turnDamage)
        if turnHeal > 0:
            if len(msg2) > 0:
                msg2 += '\n'
            msg2 += '回合总治疗：' + str(turnHeal)

        if turnDamage <= 0 and turnHeal <= 0 and isDefense is False:
            if len(self.battleListener.findSourceEvent(role, EventType.attack)) > 0:
                msg += '  普攻'
                if len(msg2) > 0:
                    msg2 += '\n'
                msg2 = '普攻'
            if len(self.battleListener.findSourceEvent(role, EventType.skill)) > 0:
                msg += '  必杀'
                if len(msg2) > 0:
                    msg2 += '\n'
                msg2 = '必杀'

        self.recordBattleMsg(msg)

        if len(self.battleListener.findSourceEvent(role, EventType.actionAfterAtk)) > 0:
            try:
                actionAtk = self.battleListener.findSourceEvent(role, EventType.actionAfterAtk)[0].value
                msg_atkAfter = '行动后实时攻击力[{}]'.format(actionAtk)
                self.recordBattleMsg(msg_atkAfter)
                atkAfterMag += str(actionAtk)
            except:
                print('获取行动后实时攻击力记录出错')
        msg_turnAtk = '我方所有角色行动后，本回合实时攻击力[{}]'.format(turnAtk)
        self.recordBattleMsg(msg_turnAtk)

        msg3 = atkMag + '\n' + atkAfterMag + '\n' + atkTurnMag
        self.ws.cell(row, turn * 2, msg3)
        self.ws.cell(row, turn * 2 + 1, msg2)

    def getTotalResult(self, role: ICard):
        attackDamage = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackDamage, True):
            try:
                attackDamage += record.value
            except:
                print('获取普攻记录出错')
        attackFU = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackFollowUp, True):
            try:
                attackFU += record.value
            except:
                print('获取普攻追击记录出错')
        attackHeal = 0
        for record in self.battleListener.findSourceEvent(role, EventType.attackHeal, True):
            try:
                attackHeal += record.value
            except:
                print('获取普攻治疗记录出错')
        skillDamage = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillDamage, True):
            try:
                skillDamage += record.value
            except:
                print('获取必杀记录出错')
        skillFU = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillFollowUp, True):
            try:
                skillFU += record.value
            except:
                print('获取必杀追击记录出错')
        skillHeal = 0
        for record in self.battleListener.findSourceEvent(role, EventType.skillHeal, True):
            try:
                skillHeal += record.value
            except:
                print('获取必杀治疗记录出错')
        dot = 0
        for record in self.battleListener.findSourceEvent(role, EventType.dot, True):
            try:
                dot += record.value
            except:
                print('获取持续伤害记录出错')
        hot = 0
        for record in self.battleListener.findSourceEvent(role, EventType.hot, True):
            try:
                hot += record.value
            except:
                print('获取持续治疗记录出错')
        bloodSuck = 0
        for record in self.battleListener.findCustomEvent(role, EventType.bloodSucking, True):
            try:
                bloodSuck += record.value
            except:
                print('获取吸血记录出错')
        shield = 0
        for record in self.battleListener.findSourceEvent(role, EventType.shield, True):
            try:
                shield += record.value
            except:
                print('获取护盾记录出错')
        counter = 0
        for record in self.battleListener.findSourceEvent(role, EventType.counter, True):
            try:
                counter += record.value
            except:
                print('获取反击记录出错')
        totalDamage = attackDamage + attackFU + skillDamage + skillFU + dot + counter
        totalHeal = attackHeal + skillHeal + hot + bloodSuck
        data = {}
        data['attackDamage'] = attackDamage
        data['attackFU'] = attackFU
        data['skillDamage'] = skillDamage
        data['skillFU'] = skillFU
        data['dot'] = dot
        data['counter'] = counter
        data['attackHeal'] = attackHeal
        data['skillHeal'] = skillHeal
        data['hot'] = hot
        data['bloodSuck'] = bloodSuck
        data['shield'] = shield
        data['totalDamage'] = totalDamage
        data['totalHeal'] = totalHeal
        return data

    def recordTotalResult(self, role: ICard, turn, row):
        msg = role.cardInfo(False)
        data = self.getTotalResult(role)
        attackDamage = data['attackDamage']
        attackFU = data['attackFU']
        skillDamage = data['skillDamage']
        skillFU = data['skillFU']
        dot = data['dot']
        counter = data['counter']
        attackHeal = data['attackHeal']
        skillHeal = data['skillHeal']
        hot = data['hot']
        bloodSuck = data['bloodSuck']
        shield = data['shield']
        totalDamage = data['totalDamage']
        totalHeal = data['totalHeal']

        self.ws.cell(row, turn * 2 + 2, str(totalDamage))
        self.ws.cell(row, turn * 2 + 4, str(totalHeal))
        if totalDamage > 0:
            msg += '  总伤害：{}'.format(totalDamage)
        if totalHeal > 0:
            msg += '  总治疗：{}'.format(totalHeal)
        if shield > 0:
            msg += '  总护盾：{}'.format(shield)
        if totalDamage > 0 or totalHeal > 0 or shield > 0:
            self.recordBattleMsg(msg)

        msg2 = '伤害占比'
        shzb = ''
        if totalDamage > 0:
            attack = attackDamage + attackFU
            skill = skillDamage + skillFU
            if attack > 0:
                proportion = roundHalfEven(attack / totalDamage * 100)
                if len(shzb) > 0:
                    shzb += '\n'
                shzb += '普攻({}%)'.format(proportion)
                msg2 += '  普攻({}%)'.format(proportion)
            if skill > 0:
                proportion = roundHalfEven(skill / totalDamage * 100)
                if len(shzb) > 0:
                    shzb += '\n'
                shzb += '必杀({}%)'.format(proportion)
                msg2 += '  必杀({}%)'.format(proportion)
            if dot > 0:
                proportion = roundHalfEven(dot / totalDamage * 100)
                if len(shzb) > 0:
                    shzb += '\n'
                shzb += '持续伤害({}%)'.format(proportion)
                msg2 += '  持续伤害({}%)'.format(proportion)
            if counter > 0:
                proportion = roundHalfEven(counter / totalDamage * 100)
                if len(shzb) > 0:
                    shzb += '\n'
                shzb += '反击({}%)'.format(proportion)
                msg2 += '  反击({}%)'.format(proportion)
            self.recordBattleMsg(msg2)
        self.ws.cell(row, turn * 2 + 3, str(shzb))
        zlzb = ''
        msg2 = '治疗占比'
        if totalHeal > 0:
            if attackHeal > 0:
                proportion = roundHalfEven(attackHeal / totalHeal * 100)
                if len(zlzb) > 0:
                    zlzb += '\n'
                zlzb += '普攻({}%)'.format(proportion)
                msg2 += '  普攻({}%)'.format(proportion)
            if skillHeal > 0:
                proportion = roundHalfEven(skillHeal / totalHeal * 100)
                if len(zlzb) > 0:
                    zlzb += '\n'
                zlzb += '必杀({}%)'.format(proportion)
                msg2 += '  必杀({}%)'.format(proportion)
            if hot > 0:
                proportion = roundHalfEven(hot / totalHeal * 100)
                if len(zlzb) > 0:
                    zlzb += '\n'
                zlzb += '持续治疗({}%)'.format(proportion)
                msg2 += '  持续治疗({}%)'.format(proportion)
            if bloodSuck > 0:
                proportion = roundHalfEven(bloodSuck / totalHeal * 100)
                if len(zlzb) > 0:
                    zlzb += '\n'
                zlzb += '吸血({}%)'.format(proportion)
                msg2 += '  吸血({}%)'.format(proportion)
            self.recordBattleMsg(msg2)
        self.ws.cell(row, turn * 2 + 5, str(zlzb))
        return totalDamage

    # 行动
    # 防御/普攻/必杀
    # 结算dot
    # 结算hot
    def action(self, turn=0, cardList: list[ICard] = [], cardList2: list[ICard] = []):
        for role in cardList:
            if role in self.defenseTurn and turn in self.defenseTurn[role]:
                role.defense = True
                event = Event(EventType.defense)
                eventManagerInstance.sendEvent(event)

            if role.defense:
                continue

            isAttack = True

            if role in self.skillTurn:
                if turn in self.skillTurn[role] and role.canSkill():
                    isAttack = False
            else:
                if role.canSkill():
                    isAttack = False

            if isAttack:
                self.doAttack(role, cardList, cardList2)
            else:
                self.doSkill(role, cardList, cardList2)

    # 反击
    def doCounter(self, role: ICard, monster: ICard, cardList2: list[ICard] = []):
        role.doCounter(seizeEnemy(role, cardList2, monster))
        totalDamage = 0
        enemiesBeAttacked = {}
        for record in self.battleListener.findSourceEvent(role, EventType.counter):
            try:
                tempDamage = record.value
                totalDamage += tempDamage
                if record.target in enemiesBeAttacked:
                    tempDamage += enemiesBeAttacked[record.target]
                enemiesBeAttacked[record.target] = tempDamage
            except:
                print('获取反击记录出错')
        role.doBloodSuck(totalDamage)
        for enemy in cardList2:
            if enemy in enemiesBeAttacked:
                if enemiesBeAttacked[enemy] > 0:
                    enemy.beAttacked(enemiesBeAttacked[enemy], False)

    # 必杀
    def doSkill(self, role: ICard, cardList: list[ICard] = [], cardList2: list[ICard] = []):
        role.skillCount = 0
        role.doSkill(seizeEnemy(role, cardList2))
        totalDamage = 0
        enemiesBeAttacked = {}
        for record in self.battleListener.findSourceEvent(role, EventType.skillDamage):
            try:
                tempDamage = record.value
                totalDamage += tempDamage
                if record.target in enemiesBeAttacked:
                    tempDamage += enemiesBeAttacked[record.target]
                enemiesBeAttacked[record.target] = tempDamage
            except:
                print('获取必杀记录出错')
        for record in self.battleListener.findSourceEvent(role, EventType.skillFollowUp):
            try:
                tempDamage = record.value
                totalDamage += tempDamage
                if record.target in enemiesBeAttacked:
                    tempDamage += enemiesBeAttacked[record.target]
                enemiesBeAttacked[record.target] = tempDamage
            except:
                print('获取必杀追击记录出错')
        role.doBloodSuck(totalDamage)
        for enemy in cardList2:
            if enemy in enemiesBeAttacked:
                if enemiesBeAttacked[enemy] > 0:
                    self.doCounter(enemy, role, cardList)
                    enemy.beAttacked(enemiesBeAttacked[enemy], True)

    # 普攻
    def doAttack(self, role: ICard, cardList: list[ICard] = [], cardList2: list[ICard] = []):
        role.doAttack(seizeEnemy(role, cardList2))
        totalDamage = 0
        enemiesBeAttacked = {}
        for record in self.battleListener.findSourceEvent(role, EventType.attackDamage):
            try:
                tempDamage = record.value
                totalDamage += tempDamage
                if record.target in enemiesBeAttacked:
                    tempDamage += enemiesBeAttacked[record.target]
                enemiesBeAttacked[record.target] = tempDamage
            except:
                print('获取普攻记录出错')
        for record in self.battleListener.findSourceEvent(role, EventType.attackFollowUp):
            try:
                tempDamage = record.value
                totalDamage += tempDamage
                if record.target in enemiesBeAttacked:
                    tempDamage += enemiesBeAttacked[record.target]
                enemiesBeAttacked[record.target] = tempDamage
            except:
                print('获取普攻追击记录出错')
        role.doBloodSuck(totalDamage)
        for enemy in cardList2:
            if enemy in enemiesBeAttacked:
                if enemiesBeAttacked[enemy] > 0:
                    self.doCounter(enemy, role, cardList)
                    enemy.beAttacked(enemiesBeAttacked[enemy], True)

    def writeCardInfoInExcel(self):
        writeCardInfoTitleInExcel(self.ws)

        row = 2
        for role in self.team:
            if role.cardName == '临时队友':
                continue
            role.writeCardInfoInExcel(self.ws, row)
            row += 1
        return row

    def exportExcel(self, filePath):
        try:
            if self.wb is not None:
                self.wb.save(filePath)
            success = True
        except:
            success = False
        if success:
            self.wb.close()
            self.wb = None
        return success


class BattleRecordListener(EventListener):
    def __init__(self):
        super(BattleRecordListener, self).__init__('战斗数据记录监听器')
        self.battleRecords = []
        self.currentTurn = 0

    def cleanUp(self):
        self.battleRecords = []

    def receiveEvent(self, arg: Event):
        bs = BattleRecord()
        bs.turn = self.currentTurn
        bs.source = arg.data['source']
        bs.valueType = arg.eventType
        bs.value = arg.data['value']
        bs.target = arg.data['target']
        if 'custom' in arg.data:
            bs.custom = arg.data['custom']
        self.battleRecords.append(bs)

    def findSourceEvent(self, role: ICard, et: EventType, ignoreTurn: bool = False):
        if ignoreTurn:
            return [y for y in self.battleRecords if y.source == role and y.valueType == et]
        else:
            return [y for y in self.battleRecords if
                    y.turn == self.currentTurn and y.source == role and y.valueType == et]

    def findTargetEvent(self, role: ICard, et: EventType, ignoreTurn: bool = False):
        if ignoreTurn:
            return [y for y in self.battleRecords if y.target == role and y.valueType == et]
        else:
            return [y for y in self.battleRecords if
                    y.turn == self.currentTurn and y.target == role and y.valueType == et]

    def findCustomEvent(self, role: ICard, et: EventType, ignoreTurn: bool = False):
        if ignoreTurn:
            return [y for y in self.battleRecords if y.custom == role and y.valueType == et]
        else:
            return [y for y in self.battleRecords if
                    y.turn == self.currentTurn and y.custom == role and y.valueType == et]


class BattleRecord:
    def __init__(self):
        self.source: ICard = None
        self.turn = 0
        self.valueType: EventType = None
        self.value = 0
        self.target: ICard = None
        self.custom = None
