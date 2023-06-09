import datetime
import io
import os
import sys
import tkinter.filedialog
from functools import partial

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QModelIndex, QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication

from Nucarnival.activityRewardHelper import ActivityRewardHelper
from Nucarnival.cardHelper import CardHelper
from Nucarnival.nucarnivalHelper import NucarnivalHelper
from Resource.pteResource import getWelcomeContent, getHelpContent, getUpdateLogContent, getActivityHelpContent
from RoleCards.cards.monster.commonMonster import CommonMonster
from RoleCards.common.card import ICard
from RoleCards.common.cardModel import CardTableModel
from RoleCards.common.filterCardModel import FilterCardModel
from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType
from UiDesign.nucarnivalCalculatorUi import Ui_MainWindow
from UiDesign.validator import IntValidator

cardHelper = CardHelper()
nucarnivalHelper = NucarnivalHelper()
activityRewardHelper = ActivityRewardHelper()


def exportCardList():
    filepath = tkinter.filedialog.asksaveasfilename(
        defaultextension='.xml',
        filetypes=[('XML 文件', '.xml'), ('所有文件', '.*')],
        initialdir='C:\\',
        initialfile='卡牌数据.xml',
        title='导出卡牌数据XML'
    )
    if len(filepath) != 0:
        cardHelper.exportCardList(filepath)


def getIntList(pte: str):
    intList: list[int] = []
    if pte is None or len(pte) <= 0:
        return intList
    for temp in pte.split('\n'):
        for temp2 in temp.split(' '):
            try:
                temp3 = int(temp2)
                intList.append(temp3)
            except:
                print('转Int出错')
    return intList


def getSequenceIntList(pte: str):
    count = 0
    intList: list[int] = []
    if pte is None or len(pte) <= 0:
        return intList
    for temp in pte.split('\n'):
        for temp2 in temp.split(' '):
            if count > 5:
                break
            try:
                temp3 = int(temp2)
                if 1 <= temp3 <= 5 and temp3 not in intList:
                    intList.append(temp3)
                    count += 1
            except:
                print('转Int出错')
    return intList


def getSequenceMap(pte: str):
    sequenceMap = {}
    for temp in pte.split('\n'):
        temp2 = temp.split(':')
        if len(temp2) == 2:
            try:
                turn = int(temp2[0])
            except:
                print('转Int出错')
                continue
            intList: list[int] = getSequenceIntList(temp2[1])
            if len(intList) > 0:
                sequenceMap[turn] = intList
    return sequenceMap


def setFilterRole(fm: FilterCardModel, index: int):
    if fm is not None:
        match index:
            case 0:
                fm.setFilterCardRole(None)
            case 1:
                fm.setFilterCardRole(CardRole.Aster)
            case 2:
                fm.setFilterCardRole(CardRole.Morvay)
            case 3:
                fm.setFilterCardRole(CardRole.Yakumo)
            case 4:
                fm.setFilterCardRole(CardRole.Edmond)
            case 5:
                fm.setFilterCardRole(CardRole.Olivine)
            case 6:
                fm.setFilterCardRole(CardRole.Quincy)
            case 7:
                fm.setFilterCardRole(CardRole.Kuya)
            case 8:
                fm.setFilterCardRole(CardRole.Garu)
            case 9:
                fm.setFilterCardRole(CardRole.Blade)
            case 10:
                fm.setFilterCardRole(CardRole.Dante)
            case 11:
                fm.setFilterCardRole(CardRole.Eiden)
            case 12:
                fm.setFilterCardRole(CardRole.Rei)


def setFilterType(fm: FilterCardModel, ct: CardType):
    if fm is not None:
        fm.setFilterCardType(ct)


def setFilterOccupation(fm: FilterCardModel, occ: CardOccupation):
    if fm is not None:
        fm.setFilterOccupation(occ)


def setFilterRarity(fm: FilterCardModel, rar: CardRarity):
    if fm is not None:
        fm.setFilterRarity(rar)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.m_flag = False
        self.m_Position = None
        self.setMouseTracking(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.currentCard: ICard = None
        self.currentTeam: ICard = None
        self.filterModel = FilterCardModel()
        self.filterModel.setSourceModel(CardTableModel(cardHelper))
        self.filterModel.setDynamicSortFilter(True)
        self.filterModel2 = FilterCardModel()
        self.filterModel2.setSourceModel(CardTableModel(cardHelper))
        self.filterModel2.setDynamicSortFilter(True)

        self.bindValidator()
        self.bindFun()
        self.initWindowData()

        self.show()

    # 初始化窗口的基础数据
    def initWindowData(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", 'Nu:carnival计算工具'))
        self.ui.welcomePTE.setPlainText(_translate("MainWindow", getWelcomeContent()))
        self.ui.helpPTE.setPlainText(_translate("MainWindow", getHelpContent()))
        self.ui.updateLogPTE.setPlainText(_translate("MainWindow", getUpdateLogContent()))
        self.ui.activityHelpPTE.setPlainText(_translate("MainWindow", getActivityHelpContent()))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", "全部"))
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Aster.roleName), CardRole.Aster)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Morvay.roleName), CardRole.Morvay)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Yakumo.roleName), CardRole.Yakumo)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Edmond.roleName), CardRole.Edmond)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Olivine.roleName), CardRole.Olivine)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Quincy.roleName), CardRole.Quincy)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Kuya.roleName), CardRole.Kuya)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Garu.roleName), CardRole.Garu)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Blade.roleName), CardRole.Blade)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Dante.roleName), CardRole.Dante)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Eiden.roleName), CardRole.Eiden)
        self.ui.filterRoleComboBox.addItem(_translate("MainWindow", CardRole.Rei.roleName), CardRole.Rei)

        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", "全部"))
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Aster.roleName), CardRole.Aster)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Morvay.roleName), CardRole.Morvay)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Yakumo.roleName), CardRole.Yakumo)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Edmond.roleName), CardRole.Edmond)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Olivine.roleName), CardRole.Olivine)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Quincy.roleName), CardRole.Quincy)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Kuya.roleName), CardRole.Kuya)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Garu.roleName), CardRole.Garu)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Blade.roleName), CardRole.Blade)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Dante.roleName), CardRole.Dante)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Eiden.roleName), CardRole.Eiden)
        self.ui.filterRoleComboBox_2.addItem(_translate("MainWindow", CardRole.Rei.roleName), CardRole.Rei)

        for i in reversed(range(1, 61)):
            self.ui.lvComboBox.addItem(_translate("MainWindow", str(i)), i)
        for i in range(0, 6):
            self.ui.bondComboBox.addItem(_translate("MainWindow", str(i)), i)
        for i in range(1, 6):
            self.ui.starComboBox.addItem(_translate("MainWindow", str(i)), i)

        self.ui.cardListTable.setModel(self.filterModel)
        self.ui.cardListTable2.setModel(self.filterModel2)
        self.ui.filterGroupBox.hide()
        self.ui.filterGroupBox2.hide()

        today = datetime.date.today()
        self.ui.startDateEdit.setDate(QDate(today.year, today.month, today.day))
        self.ui.endDateEdit.setDate(QDate(today.year, today.month, today.day))
        self.ui.battleCostLineEdit.setText('10')
        self.ui.battlePointLineEdit.setText('30')
        self.ui.tbLineEdit.setText('0')
        self.ui.bbLineEdit.setText('0')
        self.ui.sbLineEdit.setText('0')
        self.ui.currentPointLineEdit.setText('0')
        self.ui.targetPointLineEdit.setText('30000')

    # 绑定各种验证器
    def bindValidator(self):
        intValidator = QIntValidator()
        self.ui.hpLineEdit.setValidator(intValidator)
        self.ui.atkLineEdit.setValidator(intValidator)
        self.ui.currentPointLineEdit.setValidator(intValidator)
        self.ui.targetPointLineEdit.setValidator(intValidator)
        self.ui.tbLineEdit.setValidator(intValidator)
        self.ui.bbLineEdit.setValidator(intValidator)
        self.ui.sbLineEdit.setValidator(intValidator)
        self.ui.battleCostLineEdit.setValidator(intValidator)
        self.ui.battlePointLineEdit.setValidator(intValidator)

    # 绑定各种方法
    def bindFun(self):
        self.ui.idButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.cardListBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.damageCalculatorBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.activityCalBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.helpBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.updateLogBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.openFilterBtn.clicked.connect(
            lambda: self.ui.filterGroupBox.show()
            if self.ui.filterGroupBox.isHidden() else self.ui.filterGroupBox.hide())
        self.ui.openFilterBtn_2.clicked.connect(
            lambda: self.ui.filterGroupBox2.show()
            if self.ui.filterGroupBox2.isHidden() else self.ui.filterGroupBox2.hide())
        self.ui.cardListTable.clicked.connect(self.clickCard)
        self.ui.calCardBtn.clicked.connect(self.calCard)
        self.ui.resetCardBtn.clicked.connect(self.resetCard)
        self.ui.cardListTable2.clicked.connect(self.clickTeamCard)
        self.ui.calDamageBtn.clicked.connect(self.calDamage)
        self.ui.addTeamBtn.clicked.connect(self.addTeam)
        self.ui.removeTeamBtn.clicked.connect(self.removeTeam)
        self.ui.leftTeamBtn.clicked.connect(self.leftTeam)
        self.ui.rightTeamBtn.clicked.connect(self.rightTeam)
        self.ui.team1.clicked.connect(partial(self.clickTeamBtn, 0))
        self.ui.team2.clicked.connect(partial(self.clickTeamBtn, 1))
        self.ui.team3.clicked.connect(partial(self.clickTeamBtn, 2))
        self.ui.team4.clicked.connect(partial(self.clickTeamBtn, 3))
        self.ui.team5.clicked.connect(partial(self.clickTeamBtn, 4))
        self.ui.exportExcelBtn.clicked.connect(self.exportExcel)
        self.ui.clearBattleSetBtn.clicked.connect(self.clearBattleSet)
        self.ui.filterRoleComboBox.currentIndexChanged.connect(partial(setFilterRole, self.filterModel))
        self.ui.filterRoleComboBox_2.currentIndexChanged.connect(partial(setFilterRole, self.filterModel2))

        self.ui.filterOccRadioBtn_All.clicked.connect(partial(setFilterOccupation, self.filterModel, None))
        self.ui.filterOccRadioBtn_Striker.clicked.connect(
            partial(setFilterOccupation, self.filterModel, CardOccupation.Striker))
        self.ui.filterOccRadioBtn_Healer.clicked.connect(
            partial(setFilterOccupation, self.filterModel, CardOccupation.Healer))
        self.ui.filterOccRadioBtn_Guardian.clicked.connect(
            partial(setFilterOccupation, self.filterModel, CardOccupation.Guardian))
        self.ui.filterOccRadioBtn_Support.clicked.connect(
            partial(setFilterOccupation, self.filterModel, CardOccupation.Support))
        self.ui.filterOccRadioBtn_Saboteur.clicked.connect(
            partial(setFilterOccupation, self.filterModel, CardOccupation.Saboteur))

        self.ui.filterOccRadioBtn_All_2.clicked.connect(partial(setFilterOccupation, self.filterModel2, None))
        self.ui.filterOccRadioBtn_Striker_2.clicked.connect(
            partial(setFilterOccupation, self.filterModel2, CardOccupation.Striker))
        self.ui.filterOccRadioBtn_Healer_2.clicked.connect(
            partial(setFilterOccupation, self.filterModel2, CardOccupation.Healer))
        self.ui.filterOccRadioBtn_Guardian_2.clicked.connect(
            partial(setFilterOccupation, self.filterModel2, CardOccupation.Guardian))
        self.ui.filterOccRadioBtn_Support_2.clicked.connect(
            partial(setFilterOccupation, self.filterModel2, CardOccupation.Support))
        self.ui.filterOccRadioBtn_Saboteur_2.clicked.connect(
            partial(setFilterOccupation, self.filterModel2, CardOccupation.Saboteur))

        self.ui.filterRarityRadioBtn_All.clicked.connect(
            partial(setFilterRarity, self.filterModel, None))
        self.ui.filterRarityRadioBtn_SSR.clicked.connect(
            partial(setFilterRarity, self.filterModel, CardRarity.SSR))
        self.ui.filterRarityRadioBtn_SR.clicked.connect(
            partial(setFilterRarity, self.filterModel, CardRarity.SR))
        self.ui.filterRarityRadioBtn_R.clicked.connect(
            partial(setFilterRarity, self.filterModel, CardRarity.R))
        self.ui.filterRarityRadioBtn_N.clicked.connect(
            partial(setFilterRarity, self.filterModel, CardRarity.N))

        self.ui.filterRarityRadioBtn_All_2.clicked.connect(
            partial(setFilterRarity, self.filterModel2, None))
        self.ui.filterRarityRadioBtn_SSR_2.clicked.connect(
            partial(setFilterRarity, self.filterModel2, CardRarity.SSR))
        self.ui.filterRarityRadioBtn_SR_2.clicked.connect(
            partial(setFilterRarity, self.filterModel2, CardRarity.SR))
        self.ui.filterRarityRadioBtn_R_2.clicked.connect(
            partial(setFilterRarity, self.filterModel2, CardRarity.R))
        self.ui.filterRarityRadioBtn_N_2.clicked.connect(
            partial(setFilterRarity, self.filterModel2, CardRarity.N))

        self.ui.filterTypeRadioBtn_All.clicked.connect(
            partial(setFilterType, self.filterModel, None))
        self.ui.filterTypeRadioBtn_Lignt.clicked.connect(
            partial(setFilterType, self.filterModel, CardType.Light))
        self.ui.filterTypeRadioBtn_Dark.clicked.connect(
            partial(setFilterType, self.filterModel, CardType.Dark))
        self.ui.filterTypeRadioBtn_Fire.clicked.connect(
            partial(setFilterType, self.filterModel, CardType.Fire))
        self.ui.filterTypeRadioBtn_Water.clicked.connect(
            partial(setFilterType, self.filterModel, CardType.Water))
        self.ui.filterTypeRadioBtn_Wood.clicked.connect(
            partial(setFilterType, self.filterModel, CardType.Wood))

        self.ui.filterTypeRadioBtn_All_2.clicked.connect(
            partial(setFilterType, self.filterModel2, None))
        self.ui.filterTypeRadioBtn_Lignt_2.clicked.connect(
            partial(setFilterType, self.filterModel2, CardType.Light))
        self.ui.filterTypeRadioBtn_Dark_2.clicked.connect(
            partial(setFilterType, self.filterModel2, CardType.Dark))
        self.ui.filterTypeRadioBtn_Fire_2.clicked.connect(
            partial(setFilterType, self.filterModel2, CardType.Fire))
        self.ui.filterTypeRadioBtn_Water_2.clicked.connect(
            partial(setFilterType, self.filterModel2, CardType.Water))
        self.ui.filterTypeRadioBtn_Wood_2.clicked.connect(
            partial(setFilterType, self.filterModel2, CardType.Wood))

        self.ui.hpLineEdit.textChanged.connect(self.setHp)
        self.ui.atkLineEdit.textChanged.connect(self.setAtk)
        self.ui.lvComboBox.currentIndexChanged.connect(self.setLv)
        self.ui.bondComboBox.currentIndexChanged.connect(self.setBond)
        self.ui.tierComboBox.currentIndexChanged.connect(self.setTier)
        self.ui.starComboBox.currentIndexChanged.connect(self.setStar)
        self.ui.useExpectedValueCheckBox.clicked.connect(self.setUev)
        self.ui.exportCardListBtn.clicked.connect(exportCardList)
        self.ui.loadCardListBtn.clicked.connect(self.loadCardList)

        self.ui.calActivityBtn.clicked.connect(self.calActivity)

    def exportExcel(self):
        filepath = tkinter.filedialog.asksaveasfilename(
            defaultextension='.xls',
            filetypes=[('XLS 工作表', '.xls'), ('XLSX 工作表', '.xlsx'), ('所有文件', '.*')],
            initialdir='C:\\',
            initialfile='伤害模拟结果.xls',
            title='导出伤害模拟结果Excel'
        )
        if len(filepath) != 0:
            if nucarnivalHelper.exportExcel(filepath):
                self.ui.exportExcelBtn.setEnabled(False)

    def calActivity(self):
        activityRewardHelper.startDate = self.ui.startDateEdit.date().toPyDate()
        activityRewardHelper.endDate = self.ui.endDateEdit.date().toPyDate()
        try:
            activityRewardHelper.currentPoint = int(self.ui.currentPointLineEdit.text())
            activityRewardHelper.targetPoint = int(self.ui.targetPointLineEdit.text())
            activityRewardHelper.battleCost = int(self.ui.battleCostLineEdit.text())
            activityRewardHelper.battlePoint = int(self.ui.battlePointLineEdit.text())
            activityRewardHelper.tb = int(self.ui.tbLineEdit.text())
            activityRewardHelper.bb = int(self.ui.bbLineEdit.text())
            activityRewardHelper.sb = int(self.ui.sbLineEdit.text())
        except:
            print('计算活动，转Int失败')

        activityRewardHelper.xyk = self.ui.xykCheckBox.isChecked()
        activityRewardHelper.dyk = self.ui.dykCheckBox.isChecked()
        activityRewardHelper.coin = self.ui.coinCheckBox.isChecked()
        activityRewardHelper.holyWater = self.ui.holyWaterCheckBox.isChecked()
        activityRewardHelper.dailyMission = self.ui.dailyMissionCheckBox.isChecked()
        activityRewardHelper.weeklyMission = self.ui.weeklyMissionCheckBox.isChecked()
        activityRewardHelper.simulation()
        self.ui.activityResultPTE.setPlainText(activityRewardHelper.output.getvalue())

    def loadCardList(self):
        filepath = tkinter.filedialog.askopenfilename(
            defaultextension='.xml',
            filetypes=[('XML 文件', '.xml')],
            initialdir='C:\\',
            title='加载卡牌数据XML'
        )
        if len(filepath) != 0:
            cardHelper.loadCardList(filepath)
            self.ui.cardListTable.update()
            self.ui.cardListTable2.update()
            self.showCardInfo()

    def setUev(self, checked: bool):
        if self.currentCard is not None:
            self.currentCard.useExpectedValue = checked

    def setHp(self, text: str):
        if self.currentCard is not None:
            try:
                _hp = int(text)
                self.currentCard.setHpDirect(_hp)
            except:
                print('设置hp 转Int出错')
            self.ui.cardListTable.update()

    def setAtk(self, text: str):
        if self.currentCard is not None:
            try:
                _atk = int(text)
                self.currentCard.setAtkDirect(_atk)
            except:
                print('设置atk 转Int出错')
            self.ui.cardListTable.update()

    def setLv(self, index: int):
        if self.currentCard is not None:
            self.currentCard.setLv(60 - index)
            self.ui.cardListTable.update()

    def setBond(self, index: int):
        if self.currentCard is not None:
            self.currentCard.setBond(index)
            self.ui.cardListTable.update()

    def setTier(self, index: int):
        if self.currentCard is not None:
            self.currentCard.setTier(index)
            self.ui.cardListTable.update()

    def setStar(self, index: int):
        if self.currentCard is not None:
            self.currentCard.setStar(index + 1)
            self.ui.cardListTable.update()

    def calDamage(self):
        self.setBattleInfo()
        nucarnivalHelper.battleStart()
        self.ui.battleResultPTE.setPlainText(nucarnivalHelper.output.getvalue())
        self.ui.exportExcelBtn.setEnabled(True)

    def clearBattleSet(self):
        self.currentTeam = None
        self.ui.addTeamBtn.setEnabled(False)
        self.ui.removeTeamBtn.setEnabled(False)
        nucarnivalHelper.team.clear()
        self.updateTeam()
        self.ui.defensePTE1.setPlainText('')
        self.ui.defensePTE2.setPlainText('')
        self.ui.defensePTE3.setPlainText('')
        self.ui.defensePTE4.setPlainText('')
        self.ui.defensePTE5.setPlainText('')
        self.ui.skillPTE1.setPlainText('')
        self.ui.skillPTE2.setPlainText('')
        self.ui.skillPTE3.setPlainText('')
        self.ui.skillPTE4.setPlainText('')
        self.ui.skillPTE5.setPlainText('')
        self.ui.actionSequencePTE.setPlainText('')

    def setBattleInfo(self):
        turn = int(self.ui.battleRoundLineEdit.text())
        monsterCount = 1
        nucarnivalHelper.maxTurn = turn
        monsterType = CardType.Light
        if self.ui.monsterTypeRadioBtn_Dark.isChecked():
            monsterType = CardType.Dark
        elif self.ui.monsterTypeRadioBtn_Fire.isChecked():
            monsterType = CardType.Fire
        elif self.ui.monsterTypeRadioBtn_Water.isChecked():
            monsterType = CardType.Water
        elif self.ui.monsterTypeRadioBtn_Wood.isChecked():
            monsterType = CardType.Wood

        nucarnivalHelper.monsters.clear()
        for i in range(0, monsterCount):
            nucarnivalHelper.monsters.append(CommonMonster())
        for monster in nucarnivalHelper.monsters:
            monster.cardType = monsterType

        nucarnivalHelper.defenseTurn = {}
        nucarnivalHelper.skillTurn = {}
        nucarnivalHelper.actionSequence = {}
        dpte1 = getIntList(self.ui.defensePTE1.toPlainText())
        spte1 = getIntList(self.ui.skillPTE1.toPlainText())
        if len(nucarnivalHelper.team) >= 1:
            if len(dpte1) > 0:
                nucarnivalHelper.defenseTurn[nucarnivalHelper.team[0]] = dpte1
            if len(spte1) > 0:
                nucarnivalHelper.skillTurn[nucarnivalHelper.team[0]] = spte1

        dpte2 = getIntList(self.ui.defensePTE2.toPlainText())
        spte2 = getIntList(self.ui.skillPTE2.toPlainText())
        if len(nucarnivalHelper.team) >= 2:
            if len(dpte2) > 0:
                nucarnivalHelper.defenseTurn[nucarnivalHelper.team[1]] = dpte2
            if len(spte2) > 0:
                nucarnivalHelper.skillTurn[nucarnivalHelper.team[1]] = spte2

        dpte3 = getIntList(self.ui.defensePTE3.toPlainText())
        spte3 = getIntList(self.ui.skillPTE3.toPlainText())
        if len(nucarnivalHelper.team) >= 3:
            if len(dpte3) > 0:
                nucarnivalHelper.defenseTurn[nucarnivalHelper.team[2]] = dpte3
            if len(spte3) > 0:
                nucarnivalHelper.skillTurn[nucarnivalHelper.team[2]] = spte3

        dpte4 = getIntList(self.ui.defensePTE4.toPlainText())
        spte4 = getIntList(self.ui.skillPTE4.toPlainText())
        if len(nucarnivalHelper.team) >= 4:
            if len(dpte4) > 0:
                nucarnivalHelper.defenseTurn[nucarnivalHelper.team[3]] = dpte4
            if len(spte4) > 0:
                nucarnivalHelper.skillTurn[nucarnivalHelper.team[3]] = spte4

        dpte5 = getIntList(self.ui.defensePTE5.toPlainText())
        spte5 = getIntList(self.ui.skillPTE5.toPlainText())
        if len(nucarnivalHelper.team) >= 5:
            if len(dpte5) > 0:
                nucarnivalHelper.defenseTurn[nucarnivalHelper.team[4]] = dpte5
            if len(spte5) > 0:
                nucarnivalHelper.skillTurn[nucarnivalHelper.team[4]] = spte5
        aspte = getSequenceMap(self.ui.actionSequencePTE.toPlainText())
        if len(aspte) > 0:
            nucarnivalHelper.actionSequence = aspte

    def calCard(self):
        uev = self.ui.useExpectedValueCheckBox.isChecked()
        lv = 60 - self.ui.lvComboBox.currentIndex()
        bond = self.ui.bondComboBox.currentIndex()
        star = self.ui.starComboBox.currentIndex() + 1
        tier = self.ui.tierComboBox.currentIndex()
        if self.currentCard is not None:
            self.currentCard.setProperties(int(lv), int(star), int(bond), int(tier))
            self.currentCard.useExpectedValue = uev
            self.currentCard.calHpAtk(True)
        self.showCardInfo()
        self.ui.cardListTable.update()

    def resetCard(self):
        if self.currentCard is not None:
            self.currentCard.setProperties(60, 5, 0, 0)
            self.currentCard.useExpectedValue = True
            self.currentCard.setHpAtkDirect(self.currentCard.lv60s5Hp, self.currentCard.lv60s5Atk)
        self.showCardInfo()
        self.ui.cardListTable.update()

    def showCardInfo(self):
        self.ui.hpLineEdit.textChanged.disconnect()
        self.ui.atkLineEdit.textChanged.disconnect()
        self.ui.lvComboBox.currentIndexChanged.disconnect()
        self.ui.bondComboBox.currentIndexChanged.disconnect()
        self.ui.tierComboBox.currentIndexChanged.disconnect()
        self.ui.starComboBox.currentIndexChanged.disconnect()
        self.ui.useExpectedValueCheckBox.clicked.disconnect()
        if self.currentCard is not None:
            self.ui.nameLineEdit.setText(self.currentCard.cardName)
            self.ui.roleLineEdit.setText(self.currentCard.role.roleName)
            self.ui.rarityLineEdit.setText(self.currentCard.rarity.rarityName)
            self.ui.occupationLineEdit.setText(self.currentCard.occupation.occupationName)

            self.ui.hpLineEdit.setText(str(self.currentCard.hp))
            self.ui.atkLineEdit.setText(str(self.currentCard.atk))
            self.ui.useExpectedValueCheckBox.setChecked(self.currentCard.useExpectedValue)
            self.ui.lvComboBox.setCurrentIndex(60 - self.currentCard.lv)
            self.ui.bondComboBox.setCurrentIndex(self.currentCard.bond)
            self.ui.tierComboBox.setCurrentIndex(self.currentCard.tier)
            self.ui.starComboBox.setCurrentIndex(self.currentCard.star - 1)
        self.ui.hpLineEdit.textChanged.connect(self.setHp)
        self.ui.atkLineEdit.textChanged.connect(self.setAtk)
        self.ui.lvComboBox.currentIndexChanged.connect(self.setLv)
        self.ui.bondComboBox.currentIndexChanged.connect(self.setBond)
        self.ui.tierComboBox.currentIndexChanged.connect(self.setTier)
        self.ui.starComboBox.currentIndexChanged.connect(self.setStar)
        self.ui.useExpectedValueCheckBox.clicked.connect(self.setUev)

    def clickCard(self, index):
        row = index.model().mapToSource(index).row()
        self.currentCard = cardHelper.cardList[row]

        _translate = QtCore.QCoreApplication.translate
        self.ui.tierComboBox.disconnect()
        self.ui.tierComboBox.clear()
        if self.currentCard.rarity == CardRarity.N or self.currentCard.rarity == CardRarity.R:
            for i in range(0, 7):
                self.ui.tierComboBox.addItem(_translate("MainWindow", str(i)), i)
        else:
            for i in range(0, 13):
                self.ui.tierComboBox.addItem(_translate("MainWindow", str(i)), i)
        if self.currentCard.rarity == CardRarity.N:
            self.ui.bondComboBox.setEnabled(False)
        else:
            self.ui.bondComboBox.setEnabled(True)
        self.ui.tierComboBox.currentIndexChanged.connect(self.setTier)
        self.showCardInfo()

        self.ui.hpLineEdit.setEnabled(True)
        self.ui.atkLineEdit.setEnabled(True)
        self.ui.useExpectedValueCheckBox.setEnabled(True)
        self.ui.lvComboBox.setEnabled(True)
        self.ui.tierComboBox.setEnabled(True)
        self.ui.starComboBox.setEnabled(True)
        self.ui.calCardBtn.setEnabled(True)
        self.ui.resetCardBtn.setEnabled(True)

    def clickTeamCard(self, index: QModelIndex):
        row = index.model().mapToSource(index).row()
        self.currentTeam = cardHelper.cardList[row]

        if self.currentTeam in nucarnivalHelper.team:
            self.ui.addTeamBtn.setEnabled(False)
            self.ui.removeTeamBtn.setEnabled(True)
            self.ui.leftTeamBtn.setEnabled(True)
            self.ui.rightTeamBtn.setEnabled(True)
            listIndex = nucarnivalHelper.team.index(self.currentTeam)
            self.focusTeamBtn(listIndex + 1)
        else:
            self.ui.addTeamBtn.setEnabled(True)
            self.ui.removeTeamBtn.setEnabled(False)
            self.ui.leftTeamBtn.setEnabled(False)
            self.ui.rightTeamBtn.setEnabled(False)

    def focusTeamBtn(self, index):
        btn = None
        match index:
            case 1:
                btn = self.ui.team1
            case 2:
                btn = self.ui.team2
            case 3:
                btn = self.ui.team3
            case 4:
                btn = self.ui.team4
            case 5:
                btn = self.ui.team5
        if btn is not None:
            btn.setFocus()

    def clickTeamBtn(self, index):
        self.ui.addTeamBtn.setEnabled(False)
        if index < len(nucarnivalHelper.team):
            self.currentTeam = nucarnivalHelper.team[index]
            self.ui.removeTeamBtn.setEnabled(True)
            self.ui.leftTeamBtn.setEnabled(True)
            self.ui.rightTeamBtn.setEnabled(True)
        else:
            self.currentTeam = None
            self.ui.removeTeamBtn.setEnabled(False)
            self.ui.leftTeamBtn.setEnabled(False)
            self.ui.rightTeamBtn.setEnabled(False)

    def updateTeam(self):
        self.updateTeamBtn(1, None)
        self.updateTeamBtn(2, None)
        self.updateTeamBtn(3, None)
        self.updateTeamBtn(4, None)
        self.updateTeamBtn(5, None)
        teamLen = len(nucarnivalHelper.team)
        if teamLen > 5:
            nucarnivalHelper.team.clear()
            teamLen = len(nucarnivalHelper.team)
        if 1 <= teamLen <= 5:
            for i in range(0, teamLen):
                self.updateTeamBtn(i + 1, nucarnivalHelper.team[i])

    def updateTeamBtn(self, index: int, role: ICard):
        btn = None
        match index:
            case 1:
                btn = self.ui.team1
            case 2:
                btn = self.ui.team2
            case 3:
                btn = self.ui.team3
            case 4:
                btn = self.ui.team4
            case 5:
                btn = self.ui.team5
        if role is not None and btn is not None:
            cardText = role.cardName + '\n' + role.nickName + '\n' + role.role.roleName
            btn.setText(cardText)
        elif btn is not None:
            btn.setText("")

    def addTeam(self):
        if len(nucarnivalHelper.team) < 5 and self.currentTeam is not None \
                and self.currentTeam not in nucarnivalHelper.team:
            nucarnivalHelper.team.append(self.currentTeam)
        self.updateTeam()
        if 1 <= len(nucarnivalHelper.team) <= 5:
            self.ui.calDamageBtn.setEnabled(True)

    def removeTeam(self):
        if self.currentTeam is not None and self.currentTeam in nucarnivalHelper.team:
            nucarnivalHelper.team.remove(self.currentTeam)
        self.updateTeam()
        if len(nucarnivalHelper.team) == 0:
            self.ui.calDamageBtn.setEnabled(False)
        self.currentTeam = None
        self.ui.removeTeamBtn.setEnabled(False)

    def leftTeam(self):
        if self.currentTeam is not None and self.currentTeam in nucarnivalHelper.team:
            index = nucarnivalHelper.team.index(self.currentTeam)
            if 0 < index <= 4:
                nucarnivalHelper.team.remove(self.currentTeam)
                nucarnivalHelper.team.insert(index - 1, self.currentTeam)
                self.updateTeam()

    def rightTeam(self):
        if self.currentTeam is not None and self.currentTeam in nucarnivalHelper.team:
            index = nucarnivalHelper.team.index(self.currentTeam)
            if index < len(nucarnivalHelper.team) - 1 and 0 <= index < 4:
                nucarnivalHelper.team.remove(self.currentTeam)
                nucarnivalHelper.team.insert(index + 1, self.currentTeam)
                self.updateTeam()

    # 拖拽∶
    def mousePressEvent(self, event):
        if event.button() - - QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


# 打包
# pyinstaller -F -w -i nucarnivalCalculator.ico nucarnivalCalculator.py
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
