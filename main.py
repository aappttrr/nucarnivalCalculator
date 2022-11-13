import io
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication

from Nucarnival.cardHelper import CardHelper
from Nucarnival.nucarnivalHelper import NucarnivalHelper
from RoleCards.cards.monster.commonMonster import CommonMonster
from RoleCards.common.card import ICard
from RoleCards.common.cardModel import CardTableModel
from RoleCards.enum.cardTypeEnum import CardType
from UiDesign.nucarnivalCalculatorUi import Ui_MainWindow
from UiDesign.validator import IntValidator

cardHelper = CardHelper()
nucarnivalHelper = NucarnivalHelper()
nucarnivalHelper.monsters.append(CommonMonster())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.currentCard: ICard = None
        self.currentTeam: ICard = None

        intValidator = QIntValidator()
        self.ui.hpLineEdit.setValidator(intValidator)
        self.ui.atkLineEdit.setValidator(intValidator)

        lvValidator = IntValidator(1, 60)
        self.ui.lvLineEdit.setValidator(lvValidator)

        tierValidator = IntValidator(0, 12)
        self.ui.tierLineEdit.setValidator(tierValidator)

        starValidator = IntValidator(1, 5)
        self.ui.starLineEdit.setValidator(starValidator)

        bondValidator = IntValidator(0, 5)
        self.ui.bondLineEdit.setValidator(bondValidator)

        roundValidator = IntValidator(1, 50)
        self.ui.battleRoundLineEdit.setValidator(roundValidator)

        self.ui.idButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.cardListBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.damageCalculatorBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.helpBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.updateLogBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.cardListTable.clicked.connect(self.clickCard)
        self.ui.calCardBtn.clicked.connect(self.calCard)
        self.ui.saveCardBtn.clicked.connect(self.saveCard)
        self.ui.resetCardBtn.clicked.connect(self.resetCard)
        self.ui.cardListTable2.clicked.connect(self.clickTeamCard)
        self.ui.calDamageBtn.clicked.connect(self.calDamage)
        self.ui.addTeamBtn.clicked.connect(self.addTeam)
        self.ui.removeTeamBtn.clicked.connect(self.removeTeam)
        self.ui.team1.clicked.connect(self.clickTeamBtn1)
        self.ui.team2.clicked.connect(self.clickTeamBtn2)
        self.ui.team3.clicked.connect(self.clickTeamBtn3)
        self.ui.team4.clicked.connect(self.clickTeamBtn4)
        self.ui.team5.clicked.connect(self.clickTeamBtn5)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.cardListTable.setModel(CardTableModel(cardHelper))
        self.ui.cardListTable2.setModel(CardTableModel(cardHelper))

        self.show()

    def calDamage(self):
        self.setBattleInfo()
        nucarnivalHelper.battleStart()
        self.ui.battleResultPTE.setPlainText(nucarnivalHelper.output.getvalue())
        self.ui.exportExcelBtn.setEnabled(True)

    def setBattleInfo(self):
        turn = int(self.ui.battleRoundLineEdit.text())
        nucarnivalHelper.maxTurn = turn
        monsterType = CardType.Light
        match self.ui.monsterTypeComboBox.currentIndex():
            case 0:
                monsterType = CardType.Light
            case 1:
                monsterType = CardType.Dark
            case 2:
                monsterType = CardType.Fire
            case 3:
                monsterType = CardType.Water
            case 4:
                monsterType = CardType.Wood
        for monster in nucarnivalHelper.monsters:
            monster.type = monsterType

    def calCard(self):
        uev = self.ui.useExpectedValueCheckBox.isChecked()
        lv = self.ui.lvLineEdit.text()
        bond = self.ui.bondLineEdit.text()
        star = self.ui.starLineEdit.text()
        tier = self.ui.tierLineEdit.text()
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

    def saveCard(self):
        hp = self.ui.hpLineEdit.text()
        atk = self.ui.atkLineEdit.text()
        uev = self.ui.useExpectedValueCheckBox.isChecked()
        lv = self.ui.lvLineEdit.text()
        bond = self.ui.bondLineEdit.text()
        star = self.ui.starLineEdit.text()
        tier = self.ui.tierLineEdit.text()
        if self.currentCard is not None:
            self.currentCard.setProperties(int(lv), int(star), int(bond), int(tier))
            self.currentCard.useExpectedValue = uev
            self.currentCard.setHpAtkDirect(int(hp), int(atk))
        self.showCardInfo()
        self.ui.cardListTable.update()

    def showCardInfo(self):
        if self.currentCard is not None:
            self.ui.nameLineEdit.setText(self.currentCard.cardName)
            self.ui.roleLineEdit.setText(self.currentCard.role.value)
            self.ui.rarityLineEdit.setText(self.currentCard.rarity.value)
            self.ui.occupationLineEdit.setText(self.currentCard.occupation.occupationName)

            self.ui.hpLineEdit.setText(str(self.currentCard.hp))
            self.ui.atkLineEdit.setText(str(self.currentCard.atk))
            self.ui.useExpectedValueCheckBox.setChecked(self.currentCard.useExpectedValue)
            self.ui.lvLineEdit.setText(str(self.currentCard.lv))
            self.ui.bondLineEdit.setText(str(self.currentCard.bond))
            self.ui.tierLineEdit.setText(str(self.currentCard.tier))
            self.ui.starLineEdit.setText(str(self.currentCard.star))

    def clickCard(self, index):
        row = index.row()
        self.currentCard = cardHelper.cardList[row]

        self.showCardInfo()

        self.ui.hpLineEdit.setEnabled(True)
        self.ui.atkLineEdit.setEnabled(True)
        self.ui.useExpectedValueCheckBox.setEnabled(True)
        self.ui.lvLineEdit.setEnabled(True)
        self.ui.bondLineEdit.setEnabled(True)
        self.ui.tierLineEdit.setEnabled(True)
        self.ui.starLineEdit.setEnabled(True)
        self.ui.calCardBtn.setEnabled(True)
        self.ui.resetCardBtn.setEnabled(True)
        self.ui.saveCardBtn.setEnabled(True)

    def clickTeamCard(self, index):
        row = index.row()
        self.currentTeam = cardHelper.cardList[row]

        if self.currentTeam in nucarnivalHelper.team:
            self.ui.addTeamBtn.setEnabled(False)
            self.ui.removeTeamBtn.setEnabled(True)
            listIndex = nucarnivalHelper.team.index(self.currentTeam)
            self.focusTeamBtn(listIndex + 1)
        else:
            self.ui.addTeamBtn.setEnabled(True)
            self.ui.removeTeamBtn.setEnabled(False)

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

    def clickTeamBtn1(self):
        self.clickTeamBtn(0)

    def clickTeamBtn2(self):
        self.clickTeamBtn(1)

    def clickTeamBtn3(self):
        self.clickTeamBtn(2)

    def clickTeamBtn4(self):
        self.clickTeamBtn(3)

    def clickTeamBtn5(self):
        self.clickTeamBtn(4)

    def clickTeamBtn(self, index):
        self.ui.addTeamBtn.setEnabled(False)
        if index <= len(nucarnivalHelper.team):
            self.currentTeam = nucarnivalHelper.team[index-1]
            self.ui.removeTeamBtn.setEnabled(True)
        else:
            self.currentTeam = None
            self.ui.removeTeamBtn.setEnabled(False)

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
            cardText = role.cardName + '\n' + role.nickName + '\n' + role.role.value
            btn.setText(cardText)
        elif btn is not None:
            btn.setText("")

    def addTeam(self):
        if len(nucarnivalHelper.team) < 5 and self.currentTeam is not None:
            nucarnivalHelper.team.append(self.currentTeam)
        self.updateTeam()
        if 1 <= len(nucarnivalHelper.team) <= 5:
            self.ui.calDamageBtn.setEnabled(True)

    def removeTeam(self):
        if self.currentTeam is not None:
            nucarnivalHelper.team.remove(self.currentTeam)
        self.updateTeam()
        if len(nucarnivalHelper.team) == 0:
            self.ui.calDamageBtn.setEnabled(False)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())
