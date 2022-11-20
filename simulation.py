from openpyxl.comments import Comment
from openpyxl.worksheet.worksheet import Worksheet

from Nucarnival.cardHelper import CardHelper
from Nucarnival.costPerformanceHelper import CostPerformanceHelper
from Nucarnival.nucarnivalHelper import NucarnivalHelper
from Props.currencyType import CurrencyType
from Props.gameProp import GameProp
from Props.propTypeEnum import PropType
from RoleCards.cards.garu.howlingCyclone import HowlingCyclone
from RoleCards.cards.monster.commonMonster import CommonMonster
from RoleCards.cards.monster.tempTeamMate import TempTeamMate
from RoleCards.cards.quincy.ancientCeremony import AncientCeremony
from RoleCards.cards.quincy.distantPromise import DistantPromise
from RoleCards.common.card import ICard
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from openpyxl.workbook import Workbook


# 模拟角色单人13回合作战能力（以被动在实战中能否吃满配置队友
from RoleCards.enum.passiveEffectivenessDifficultyEnum import PassiveEffectivenessDifficulty


def simulation2(filePath, cardHelper: CardHelper, helper: NucarnivalHelper, calGroupRole: bool):
    wb = Workbook()

    ws = wb.create_sheet('伤害模拟结果', 0)
    ws2 = wb.create_sheet('伤害模拟结果_ssr5星', 0)
    ws.merge_cells(None, 1, 1, 1, 12)
    ws2.merge_cells(None, 1, 1, 1, 12)
    title = ''
    if calGroupRole:
        title = '单人13回合期望伤害模拟_群体'
    else:
        title = '单人13回合期望伤害模拟_单体'
    ws.cell(1, 1, title)
    ws2.cell(1, 1, title)
    comment = Comment('如果三星被动实战吃满难易程度是中等及以下，则会配置虚拟队友让其吃满被动；否则将吃不满'
                      '\n但类似HP>90%的被动则都会吃满', '纳萨尔')
    ws.cell(1, 1).comment = comment
    ws2.cell(1, 1).comment = comment

    row = 2
    ssrRow = 2
    exportTitle(ws, row)
    exportTitle(ws2, ssrRow)

    for x in cardHelper.cardList:
        needTeamMate = True
        if x.ped == PassiveEffectivenessDifficulty.difficult or x.ped == PassiveEffectivenessDifficulty.veryDifficult:
            needTeamMate = False

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


# 模拟角色单人13回合作战能力
def simulation1(filePath, cardHelper: CardHelper, helper: NucarnivalHelper, needTeamMate: bool, calGroupRole: bool):
    wb = Workbook()

    ws = wb.create_sheet('伤害模拟结果', 0)
    ws2 = wb.create_sheet('伤害模拟结果_ssr5星', 0)
    ws.merge_cells(None, 1, 1, 1, 12)
    ws2.merge_cells(None, 1, 1, 1, 12)
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
    damage = helper.damageRecord[x]
    ws.cell(row, 12, damage)
    if x.rarity == CardRarity.SSR and x.star == 5:
        if damage >= 300000:
            ws.cell(row, 13, 'T0')
        elif 275000 <= damage < 300000:
            ws.cell(row, 13, 'T1')
        elif 250000 <= damage < 275000:
            ws.cell(row, 13, 'T2')
        elif 200000 <= damage < 250000:
            ws.cell(row, 13, 'T3')
        else:
            ws.cell(row, 13, 'T4')
    else:
        if damage >= 200000:
            ws.cell(row, 13, 'T0')
        elif 175000 <= damage < 200000:
            ws.cell(row, 13, 'T1')
        elif 150000 <= damage < 175000:
            ws.cell(row, 13, 'T2')
        elif 100000 <= damage < 150000:
            ws.cell(row, 13, 'T3')
        else:
            ws.cell(row, 13, 'T4')




# 导出
def export(ws: Worksheet, x: ICard, row):
    ws.cell(row, 1, x.cardName)
    ws.cell(row, 2, x.nickName)
    ws.cell(row, 3, x.rarity.value)
    ws.cell(row, 4, x.role.value)
    ws.cell(row, 5, x.cardType.typeName)
    ws.cell(row, 6, x.occupation.occupationName)
    ws.cell(row, 7, x.star)
    ws.cell(row, 8, x.tier)
    ws.cell(row, 9, x.hp)
    ws.cell(row, 10, x.atk)
    ws.cell(row, 11, x.ped.value)


def exportTitle(ws: Worksheet,row):
    ws.cell(row, 1, '卡')
    ws.cell(row, 2, '昵称')
    ws.cell(row, 3, '稀有度')
    ws.cell(row, 4, '角色')
    ws.cell(row, 5, '属性')
    ws.cell(row, 6, '定位')
    ws.cell(row, 7, '星级')
    ws.cell(row, 8, '潜能')
    ws.cell(row, 9, 'Hp')
    ws.cell(row, 10, 'Atk')
    ws.cell(row, 11, '三星被动实战吃满难易程度')
    ws.cell(row, 12, '13回合单人输出')
    ws.cell(row, 13, '梯度')


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
    elif x.cardName == '骑士副团长':
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

    simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_不配置队友.xls', _cardHelper, _helper, False, False)
    simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_配置队友.xls', _cardHelper, _helper, True, False)
    simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_不配置队友.xls', _cardHelper, _helper, False, True)
    simulation1('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_配置队友.xls', _cardHelper, _helper, True, True)

    simulation2('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_群体_模拟实战.xls', _cardHelper, _helper, True)
    simulation2('E:\\新世界\\战斗模拟\\单人13回合期望伤害模拟_单体_模拟实战.xls', _cardHelper, _helper, False)
