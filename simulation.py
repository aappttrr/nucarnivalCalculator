from openpyxl.comments import Comment
from openpyxl.worksheet.worksheet import Worksheet

from Nucarnival.cardHelper import CardHelper
from Nucarnival.nucarnivalHelper import NucarnivalHelper, roundHalfEven
from RoleCards.cards.monster.commonMonster import CommonMonster
from RoleCards.cards.monster.tempTeamMate import TempTeamMate
from RoleCards.common.card import ICard, writeCardInfoTitleInExcel
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from openpyxl.workbook import Workbook
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


def simulationCombat(filePath, cardHelper: CardHelper, helper: NucarnivalHelper, calGroupRole: bool,
                     forceTeamMate: bool = False):
    wb = Workbook()

    column = 16
    ws1 = wb.create_sheet('伤害模拟结果_ssr1星', 0)
    ws2 = wb.create_sheet('伤害模拟结果_ssr3星', 0)
    ws3 = wb.create_sheet('伤害模拟结果_ssr5星', 0)
    ws1.merge_cells(None, 1, 1, 1, column)
    ws2.merge_cells(None, 1, 1, 1, column)
    ws3.merge_cells(None, 1, 1, 1, column)
    title = ''
    if calGroupRole:
        title = '单人13回合期望伤害模拟_群体'
    else:
        title = '单人13回合期望伤害模拟_单体'
    ws1.cell(1, 1, title)
    ws2.cell(1, 1, title)
    ws3.cell(1, 1, title)
    comment = Comment('如果三星被动实战吃满难易程度是中等及以下，则会配置虚拟队友让其吃满被动；否则将吃不满'
                      '\n但类似HP>90%的被动则都会吃满', '纳萨尔')
    ws1.cell(1, 1).comment = comment
    ws2.cell(1, 1).comment = comment
    ws3.cell(1, 1).comment = comment

    row1 = 2
    row2 = 2
    row3 = 2
    exportTitle(ws1, row1)
    exportTitle(ws2, row2)
    exportTitle(ws3, row3)

    for x in cardHelper.cardList:
        if x.rarity == CardRarity.N:
            continue

        # if x.occupation == CardOccupation.Support or x.occupation == CardOccupation.Guardian \
        #         or x.occupation == CardOccupation.Healer:
        #     continue

        needTeamMate = True
        if x.ped == PassiveEffectivenessDifficulty.difficult or x.ped == PassiveEffectivenessDifficulty.veryDifficult:
            needTeamMate = False
        if forceTeamMate:
            needTeamMate = True

        if x.isGroup == calGroupRole:
            row1 += 1
            row2 += 1
            if x.rarity == CardRarity.SSR:
                # 1星6潜
                simulation(helper, needTeamMate, ws1, x, row1, 1, 6)

                # 3星满潜
                simulation(helper, needTeamMate, ws2, x, row2, 3, 12)

                row3 += 1
                # 5星满潜
                simulation(helper, needTeamMate, ws3, x, row3, 5, 12)
            elif x.rarity == CardRarity.SR:
                # 3星6潜
                simulation(helper, needTeamMate, ws1, x, row1, 3, 6)

                # 5星满潜
                simulation(helper, needTeamMate, ws2, x, row2, 5, 12)
            else:
                # 3星3潜
                simulation(helper, needTeamMate, ws1, x, row1, 3, 3)

                # 5星满潜
                simulation(helper, needTeamMate, ws2, x, row2, 5, 6)

    wb.save(filePath)


# 进行模拟
def getDamageProportion(helper: NucarnivalHelper, x: ICard, data):
    msg = ''
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
    totalDamage = data['totalDamage']
    totalHeal = data['totalHeal']

    if totalDamage == 0:
        return msg
    if totalDamage > 0:
        attack = attackDamage + attackFU
        skill = skillDamage + skillFU
        if attack > 0:
            proportion = roundHalfEven(attack / totalDamage * 100)
            if len(msg) > 0:
                msg += '\n'
            msg += '普攻({}%)'.format(proportion)
        if skill > 0:
            proportion = roundHalfEven(skill / totalDamage * 100)
            if len(msg) > 0:
                msg += '\n'
            msg += '必杀({}%)'.format(proportion)
        if dot > 0:
            proportion = roundHalfEven(dot / totalDamage * 100)
            if len(msg) > 0:
                msg += '\n'
            msg += '持续伤害({}%)'.format(proportion)
        if counter > 0:
            proportion = roundHalfEven(counter / totalDamage * 100)
            if len(msg) > 0:
                msg += '\n'
            msg += '反击({}%)'.format(proportion)
    return msg


def getRank(x: ICard, damage=0):
    rank = ''
    if x.isGroup:
        if x.rarity == CardRarity.SSR and x.star == 5:
            if damage >= 150000:
                rank = 'T0'
            elif 100000 <= damage < 150000:
                rank = 'T1'
            else:
                rank = 'T2'
        elif (x.rarity == CardRarity.SSR and x.star == 3) \
                or (x.rarity == CardRarity.SR and x.star == 5) \
                or (x.rarity == CardRarity.R and x.star == 5):
            if damage >= 85000:
                rank = 'T0'
            elif 80000 <= damage < 85000:
                rank = 'T1'
            else:
                rank = 'T2'
        else:
            if damage >= 30000:
                rank = 'T0'
            elif 20000 <= damage < 30000:
                rank = 'T1'
            else:
                rank = 'T2'
    else:
        if x.rarity == CardRarity.SSR and x.star == 5:
            if damage >= 300000:
                rank = 'T0'
            elif 275000 <= damage < 300000:
                rank = 'T1'
            elif 250000 <= damage < 275000:
                rank = 'T2'
            elif 200000 <= damage < 250000:
                rank = 'T3'
            else:
                rank = 'T4'
        elif (x.rarity == CardRarity.SSR and x.star == 3) \
                or (x.rarity == CardRarity.SR and x.star == 5) \
                or (x.rarity == CardRarity.R and x.star == 5):
            if damage >= 200000:
                rank = 'T0'
            elif 175000 <= damage < 200000:
                rank = 'T1'
            elif 150000 <= damage < 175000:
                rank = 'T2'
            elif 100000 <= damage < 150000:
                rank = 'T3'
            else:
                rank = 'T4'
        else:
            if damage >= 100000:
                rank = 'T0'
            elif 80000 <= damage < 100000:
                rank = 'T1'
            elif 70000 <= damage < 80000:
                rank = 'T2'
            elif 65000 <= damage < 70000:
                rank = 'T3'
            else:
                rank = 'T4'
    return rank


def simulation(helper: NucarnivalHelper, needTeamMate: bool, ws: Worksheet, x: ICard, row, _star, _tier):
    x.setProperties(60, _star, 5, _tier)
    x.calHpAtk()
    export(ws, x, row)

    helper.clearUp()
    if needTeamMate:
        similationTeamMate(helper, x)

    helper.team.append(x)
    helper.monsters.append(CommonMonster())
    helper.maxTurn = 13
    helper.battleStart(False)
    data = helper.getTotalResult(x)
    column = 14
    ws.cell(row, column, data['totalDamage'])
    column += 1
    ws.cell(row, column, getDamageProportion(helper, x, data))
    column += 1
    ws.cell(row, column, getRank(x, data['totalDamage']))


# 导出
def export(ws: Worksheet, x: ICard, row):
    ws.cell(row, 1, x.cardName)
    ws.cell(row, 2, x.nickName)
    ws.cell(row, 3, x.role.value)
    ws.cell(row, 4, x.rarity.value)
    ws.cell(row, 5, x.cardType.typeName)
    ws.cell(row, 6, x.occupation.occupationName)
    ws.cell(row, 7, x.lv)
    ws.cell(row, 8, x.star)
    ws.cell(row, 9, x.tier)
    ws.cell(row, 10, x.bond)
    ws.cell(row, 11, x.hp)
    ws.cell(row, 12, x.atk)
    ws.cell(row, 13, x.ped.value)


def exportTitle(ws: Worksheet, row):
    ws.cell(row, 1, '卡')
    ws.cell(row, 2, '昵称')
    ws.cell(row, 3, '角色')
    ws.cell(row, 4, '稀有度')
    ws.cell(row, 5, '类型')
    ws.cell(row, 6, '定位')
    ws.cell(row, 7, '等级')
    ws.cell(row, 8, '星级')
    ws.cell(row, 9, '潜力')
    ws.cell(row, 10, '蜜话')
    ws.cell(row, 11, 'Hp')
    ws.cell(row, 12, 'Atk')
    ws.cell(row, 13, '三星被动实战吃满难易程度')
    ws.cell(row, 14, '13回合单人输出')
    ws.cell(row, 15, '输出占比')
    ws.cell(row, 16, '梯度')


# 配置模拟队友
def similationTeamMate(helper: NucarnivalHelper, x: ICard):
    if x.cardName == '爵士册封之夜' or x.cardName == '追逐悠远之约':
        mate = TempTeamMate()
        mate.occupation = CardOccupation.Striker
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.occupation = CardOccupation.Striker
        helper.team.append(mate2)
    elif x.cardName == '化形宴，飘落叶' or x.cardName == '诡秘妖狐':
        mate = TempTeamMate()
        mate.role = CardRole.Kuya
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Kuya
        helper.team.append(mate2)
    elif x.cardName == '来自主人的新礼物' or x.cardName == '流浪小狼':
        mate = TempTeamMate()
        mate.role = CardRole.Garu
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Garu
        helper.team.append(mate2)
    elif x.cardName == '战斗人偶与回忆' or x.cardName == '魔人偶':
        mate = TempTeamMate()
        mate.role = CardRole.Blade
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Blade
        helper.team.append(mate2)
    elif x.cardName == '白色恋人':
        mate = TempTeamMate()
        mate.role = CardRole.Yakumo
        helper.team.append(mate)
    elif x.cardName == '七叶之花的奇迹':
        mate = TempTeamMate()
        mate.occupation = CardOccupation.Support
        helper.team.append(mate)
    elif x.cardName == '华宴夜未央':
        mate = TempTeamMate()
        mate.role = CardRole.Kuya
        helper.team.append(mate)
    elif x.cardName == '偶像实习':
        mate = TempTeamMate()
        mate.role = CardRole.Yakumo
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Olivine
        helper.team.append(mate2)
    elif x.cardName == '永不消散的焰火' or x.cardName == '太阳城主':
        mate = TempTeamMate()
        mate.role = CardRole.Dante
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Dante
        helper.team.append(mate2)
    elif x.cardName == '初露芬芳的甜味':
        mate = TempTeamMate()
        helper.team.append(mate)
    elif x.cardName == '使魔-艾斯特':
        mate = TempTeamMate()
        mate.role = CardRole.Morvay
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Aster
        helper.team.append(mate2)
        mate3 = TempTeamMate()
        mate3.role = CardRole.Aster
        helper.team.append(mate3)
    elif x.cardName == '骑士副团长' or x.cardName == '专属指导':
        mate = TempTeamMate()
        mate.role = CardRole.Edmond
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Edmond
        helper.team.append(mate2)
    elif x.cardName == '古森守护者':
        mate = TempTeamMate()
        mate.role = CardRole.Quincy
        helper.team.append(mate)
        mate2 = TempTeamMate()
        mate2.role = CardRole.Quincy
        helper.team.append(mate2)


def banguaiSimulation(filepath, cardHelper: CardHelper, helper: NucarnivalHelper):
    wb = Workbook()
    ws = wb.active
    ws.title = '角色属性'
    writeCardInfoTitleInExcel(ws)

    # sr昆 必杀工具人 30
    # 暗昆 普攻工具人 19
    # sr墨菲 26

    # 光狼 13
    # 暗团 24
    # sr蛋 34
    # sr狼 32

    # 白八 8
    # 水蛋 15
    # 火团 17
    cList = [30, 19]
    banguaiList = [13, 24, 34, 32, 8, 15, 17]
    skillList = [13, 24, 34, 32, 8, 15]
    attackList = [13, 24, 34, 32, 17]
    row = 2
    for i in cList:
        role = cardHelper.cardList[i]
        if role.rarity == CardRarity.SSR:
            role.setProperties(60, 3, 5, 12)
        else:
            role.setProperties(60, 5, 5, 12)
        role.calHpAtk(True)
        role.writeCardInfoInExcel(ws, row)
        row += 1

    for i in banguaiList:
        role = cardHelper.cardList[i]
        if role.rarity == CardRarity.SSR:
            role.setProperties(60, 3, 5, 12)
        else:
            role.setProperties(60, 5, 5, 12)
        role.calHpAtk(True)
        role.writeCardInfoInExcel(ws, row)
        row += 1

    ws2 = wb.create_sheet('必杀队伍', 1)
    row = 0

    helper.maxTurn = 13
    helper.monsters.append(CommonMonster())

    helper.skillTurn[cardHelper.cardList[32]] = [7, 13]

    helper.team.clear()
    helper.team.append(cardHelper.cardList[30])
    helper.battleStart(False)
    row = saveBattleResult(ws2, helper, row)

    for i in skillList:
        helper.team.clear()
        helper.team.append(cardHelper.cardList[i])
        if i == 24:
            helper.team.append(cardHelper.cardList[26])
        helper.team.append(cardHelper.cardList[30])
        helper.battleStart(False)
        row = saveBattleResult(ws2, helper, row)

    ws3 = wb.create_sheet('普攻队伍', 2)
    row = 0
    helper.skillTurn.clear()
    helper.maxTurn = 14
    helper.skillTurn[cardHelper.cardList[34]] = [5, 9, 13]
    helper.skillTurn[cardHelper.cardList[32]] = [6, 10, 14]

    helper.team.clear()
    helper.team.append(cardHelper.cardList[19])
    helper.battleStart(False)
    row = saveBattleResult(ws3, helper, row)
    for i in attackList:
        helper.team.clear()
        helper.team.append(cardHelper.cardList[i])
        if i == 24:
            helper.team.append(cardHelper.cardList[26])
        helper.team.append(cardHelper.cardList[19])
        helper.battleStart(False)
        row = saveBattleResult(ws3, helper, row)
    wb.save(filepath)


def saveBattleResult(targetWs: Worksheet, helper: NucarnivalHelper, row: int):
    row += 1
    row2 = len(helper.team) + 3
    mt = helper.maxTurn
    for i in range(0, len(helper.team) + 2):
        for column in range(1, mt + 4):
            cellValue = helper.ws.cell(row2, column).value
            if cellValue is not None:
                targetWs.cell(row, column, cellValue)
        row2 += 1
        row += 1
    return row


if __name__ == '__main__':
    _helper = NucarnivalHelper()

    _cardHelper = CardHelper()

    # banguaiSimulation('C:\\fhs\\python\\半拐模拟2.xls', _cardHelper, _helper)

    simulationCombat('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_模拟实战.xls', _cardHelper, _helper, True)
    simulationCombat('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_模拟实战.xls', _cardHelper, _helper, False)
    # simulationCombat('C:\\fhs\\python\\单人13回合期望伤害模拟_群体_模拟实战2.xls', _cardHelper, _helper, True)
    # simulationCombat('C:\\fhs\\python\\单人13回合期望伤害模拟_单体_模拟实战2.xls', _cardHelper, _helper, False)
