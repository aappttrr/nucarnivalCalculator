from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QVariant

from Nucarnival.cardHelper import CardHelper


class CardTableModel(QAbstractTableModel):
    def __init__(self, _cardHelper: CardHelper):
        super(CardTableModel, self).__init__()
        self.cardHelper = _cardHelper

    def rowCount(self, parent):
        return len(self.cardHelper.cardList)

    def columnCount(self, parent):
        return 12

    def data(self, index, role):
        row = index.row()
        column = index.column()

        if role == QtCore.Qt.DisplayRole:
            card = self.cardHelper.cardList[row]
            displayValue = ''
            match column:
                case 0:
                    displayValue = card.cardName
                case 1:
                    displayValue = card.nickName
                case 2:
                    displayValue = card.role.roleName
                case 3:
                    displayValue = card.rarity.rarityName
                case 4:
                    displayValue = card.cardType.typeName
                case 5:
                    displayValue = card.occupation.occupationName
                case 6:
                    displayValue = card.hp
                case 7:
                    displayValue = card.atk
                case 8:
                    displayValue = card.lv
                case 9:
                    displayValue = card.star
                case 10:
                    displayValue = card.tier
                case 11:
                    displayValue = card.bond
            return displayValue

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == 1:
            displayValue = ''
            match section:
                case 0:
                    displayValue = '名称'
                case 1:
                    displayValue = '昵称'
                case 2:
                    displayValue = '角色'
                case 3:
                    displayValue = '稀有度'
                case 4:
                    displayValue = '类型'
                case 5:
                    displayValue = '定位'
                case 6:
                    displayValue = 'Hp'
                case 7:
                    displayValue = 'Atk'
                case 8:
                    displayValue = '等级'
                case 9:
                    displayValue = '星级'
                case 10:
                    displayValue = '潜力'
                case 11:
                    displayValue = '蜜话'
            return displayValue
        else:
            return super(CardTableModel, self).headerData(section, orientation, role)
