from openpyxl.comments import Comment
from openpyxl.worksheet.worksheet import Worksheet

from Nucarnival.cardHelper import CardHelper
from Nucarnival.nucarnivalHelper import NucarnivalHelper, roundHalfEven
from RoleCards.cards.monster.commonMonster import CommonMonster
from RoleCards.cards.monster.tempTeamMate import TempTeamMate
from RoleCards.common.card import ICard
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from openpyxl.workbook import Workbook

# 模拟角色单人13回合作战能力（以被动在实战中能否吃满配置队友
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


def simulation2(filePath, cardHelper: CardHelper, helper: NucarnivalHelper, calGroupRole: bool):
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

        if x.occupation == CardOccupation.Support or x.occupation == CardOccupation.Guardian \
                or x.occupation == CardOccupation.Healer:
            continue

        needTeamMate = True
        if x.ped == PassiveEffectivenessDifficulty.difficult or x.ped == PassiveEffectivenessDifficulty.veryDifficult:
            needTeamMate = False

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


# 模拟角色单人13回合作战能力
def simulation1(filePath, cardHelper: CardHelper, helper: NucarnivalHelper, needTeamMate: bool, calGroupRole: bool):
    wb = Workbook()

    column = 16
    ws = wb.create_sheet('伤害模拟结果', 0)
    ws2 = wb.create_sheet('伤害模拟结果_ssr5星', 0)
    ws.merge_cells(None, 1, 1, 1, column)
    ws2.merge_cells(None, 1, 1, 1, column)
    title = ''
    if needTeamMate and calGroupRole:
        title = '单人13回合期望伤害模拟_群体_配置虚拟队友被动吃满（例如：实战难以满足的3个艾斯特）'
    elif needTeamMate and calGroupRole is False:
        title = '单人13回合期望伤害模拟_单体_配置虚拟队友被动吃满（例如：实战难以满足的3个艾斯特）'
    elif needTeamMate is False and calGroupRole:
        title = '单人13回合期望伤害模拟_群体_不配置任何队友部分被动无法吃满'
    elif needTeamMate is False and calGroupRole is False:
        title = '单人13回合期望伤害模拟_单体_不配置任何队友部分被动无法吃满'
    ws.cell(1, 1, title)
    ws2.cell(1, 1, title)

    row = 2
    ssrRow = 2
    exportTitle(ws, row)
    exportTitle(ws2, ssrRow)

    for x in cardHelper.cardList:
        if (x.occupation == CardOccupation.Support and x.cardName != '诡夜疾风') \
                or x.occupation == CardOccupation.Healer:
            continue
        if x.isGroup == calGroupRole:
            row += 1
            if x.rarity == CardRarity.SSR:
                ssrRow += 1
                # 5星满潜
                simulation(helper, needTeamMate, ws2, x, ssrRow, 5, 12)

                # 3星满潜
                simulation(helper, needTeamMate, ws, x, row, 3, 12)
            elif x.rarity == CardRarity.SR:
                # 5星满潜
                simulation(helper, needTeamMate, ws, x, row, 5, 12)
            else:
                # 5星满潜
                simulation(helper, needTeamMate, ws, x, row, 5, 6)

    wb.save(filePath)


# 进行模拟
def getDamageProportion(helper: NucarnivalHelper, x: ICard, totalDamage=1):
    msg = ''
    if totalDamage == 0:
        return msg
    if x in helper.damageRecord_attack:
        if helper.damageRecord_attack[x] > 0:
            damageProportion = helper.damageRecord_attack[x] / totalDamage * 100
            damageProportion = roundHalfEven(damageProportion)
            if len(msg) != 0:
                msg += '\n'
            msg += '普攻（' + str(damageProportion) + '%）'
    if x in helper.damageRecord_skill:
        if helper.damageRecord_skill[x] > 0:
            damageProportion = helper.damageRecord_skill[x] / totalDamage * 100
            damageProportion = roundHalfEven(damageProportion)
            if len(msg) != 0:
                msg += '\n'
            msg += '必杀（' + str(damageProportion) + '%）'
    if x in helper.damageRecord_dot:
        if helper.damageRecord_dot[x] > 0:
            damageProportion = helper.damageRecord_dot[x] / totalDamage * 100
            damageProportion = roundHalfEven(damageProportion)
            if len(msg) != 0:
                msg += '\n'
            msg += '持续伤害（' + str(damageProportion) + '%）'
    if x in helper.damageRecord_counter:
        if helper.damageRecord_counter[x] > 0:
            damageProportion = helper.damageRecord_counter[x] / totalDamage * 100
            damageProportion = roundHalfEven(damageProportion)
            if len(msg) != 0:
                msg += '\n'
            msg += '反击（' + str(damageProportion) + '%）'
    return msg


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
    damage = 0
    if x in helper.damageRecord:
        damage = helper.damageRecord[x]
    column = 14
    ws.cell(row, column, damage)
    column += 1
    ws.cell(row, column, getDamageProportion(helper, x, damage))
    column += 1
    if x.rarity == CardRarity.SSR and x.star == 5:
        if damage >= 300000:
            ws.cell(row, column, 'T0')
        elif 275000 <= damage < 300000:
            ws.cell(row, column, 'T1')
        elif 250000 <= damage < 275000:
            ws.cell(row, column, 'T2')
        elif 200000 <= damage < 250000:
            ws.cell(row, column, 'T3')
        else:
            ws.cell(row, column, 'T4')
    elif (x.rarity == CardRarity.SSR and x.star == 3) \
            or (x.rarity == CardRarity.SR and x.star == 5)\
            or (x.rarity == CardRarity.R and x.star == 5):
        if damage >= 200000:
            ws.cell(row, column, 'T0')
        elif 175000 <= damage < 200000:
            ws.cell(row, column, 'T1')
        elif 150000 <= damage < 175000:
            ws.cell(row, column, 'T2')
        elif 100000 <= damage < 150000:
            ws.cell(row, column, 'T3')
        else:
            ws.cell(row, column, 'T4')
    else:
        if damage >= 100000:
            ws.cell(row, column, 'T0')
        elif 80000 <= damage < 100000:
            ws.cell(row, column, 'T1')
        elif 70000 <= damage < 80000:
            ws.cell(row, column, 'T2')
        elif 65000 <= damage < 70000:
            ws.cell(row, column, 'T3')
        else:
            ws.cell(row, column, 'T4')


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


if __name__ == '__main__':
    _helper = NucarnivalHelper()

    _cardHelper = CardHelper()

    # # sr昆 必杀工具人
    # _cardHelper.cardList[30].setProperties(60, 5, 5, 12)
    #
    # # 暗昆 普攻工具人
    # _cardHelper.cardList[19].setProperties(60, 3, 5, 12)
    #
    # # 光狼
    # _cardHelper.cardList[13].setProperties(60, 3, 5, 12)
    # # 暗团
    # _cardHelper.cardList[24].setProperties(60, 3, 5, 12)
    # # sr蛋
    # _cardHelper.cardList[34].setProperties(60, 5, 5, 12)
    # # sr狼
    # _cardHelper.cardList[32].setProperties(60, 5, 5, 12)
    #
    # # 白八
    # _cardHelper.cardList[8].setProperties(60, 3, 5, 12)
    # # 水蛋
    # _cardHelper.cardList[15].setProperties(60, 3, 5, 12)
    #
    # # 火团
    # _cardHelper.cardList[17].setProperties(60, 3, 5, 12)
    #
    # # _helper.skillTurn[_cardHelper.cardList[34]] = [5, 9, 13]
    # _helper.team.append(_cardHelper.cardList[17])
    # # _helper.team.append(_cardHelper.cardList[26])
    # _helper.team.append(_cardHelper.cardList[19])
    # _helper.monsters.append(CommonMonster())
    # _helper.maxTurn = 14
    # _helper.battleStart(True)
    # _helper.exportExcel('C:\\fhs\\python\\模拟.xls')

    # simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_不配置队友.xls', _cardHelper, _helper, False, False)
    # simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_配置队友.xls', _cardHelper, _helper, True, False)
    # simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_不配置队友.xls', _cardHelper, _helper, False, True)
    # simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_配置队友.xls', _cardHelper, _helper, True, True)

    # simulation2('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_模拟实战.xls', _cardHelper, _helper, True)
    # simulation2('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_模拟实战.xls', _cardHelper, _helper, False)
    simulation2('C:\\fhs\\python\\单人13回合期望伤害模拟_群体_模拟实战.xls', _cardHelper, _helper, True)
    simulation2('C:\\fhs\\python\\单人13回合期望伤害模拟_单体_模拟实战.xls', _cardHelper, _helper, False)
