from PyQt5 import QtCore
from PyQt5.QtCore import QSortFilterProxyModel, QModelIndex, QVariant

from RoleCards.enum.cardOccupationEnum import CardOccupation
from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.cardRoleEnum import CardRole
from RoleCards.enum.cardTypeEnum import CardType


class FilterCardModel(QSortFilterProxyModel):
    def __init__(self):
        super(FilterCardModel, self).__init__()
        self.filterRarity: CardRarity = None
        self.filterOccupation: CardOccupation = None
        self.filterRole: CardRole = None
        self.filterType: CardType = None

    def setFilterOccupation(self, _occ: CardOccupation):
        self.filterOccupation = _occ
        self.invalidateFilter()

    def setFilterRarity(self, _rar: CardRarity):
        self.filterRarity = _rar
        self.invalidateFilter()

    def setFilterCardType(self, _cType: CardType):
        self.filterType = _cType
        self.invalidateFilter()

    def setFilterCardRole(self, _cRole: CardRole):
        self.filterRole = _cRole
        self.invalidateFilter()

    def getColumnData(self, source_row: int, source_parent: QModelIndex, columnIndex: int):
        return self.sourceModel().index(source_row, columnIndex, source_parent).data(QtCore.Qt.DisplayRole)

    # 过滤筛选
    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex) -> bool:
        indexRole = 2
        indexRarity = 3
        indexType = 4
        indexOccupation = 5
        columnRole = self.getColumnData(source_row, source_parent, indexRole)
        columnRarity = self.getColumnData(source_row, source_parent, indexRarity)
        columnType = self.getColumnData(source_row, source_parent, indexType)
        columnOccupation = self.getColumnData(source_row, source_parent, indexOccupation)
        result = True
        if self.filterRole is not None:
            if columnRole != self.filterRole.value:
                result = False
        if self.filterRarity is not None:
            if columnRarity != self.filterRarity.value:
                result = False
        if self.filterType is not None:
            if columnType != self.filterType.typeName:
                result = False
        if self.filterOccupation is not None:
            if columnOccupation != self.filterOccupation.occupationName:
                result = False
        return result
