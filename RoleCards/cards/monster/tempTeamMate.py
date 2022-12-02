from RoleCards.common.nCard import NCard


class TempTeamMate(NCard):
    def __init__(self):
        super(TempTeamMate, self).__init__()
        self.cardId = 'TempTeamMate'
        self.cardName = '临时队友'
        self.skillCD = 4

        self.lv60s5Hp = 10000000
        self.lv60s5Atk = 1
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    def skillHeal(self, enemy):
        return 2

    def attackHeal(self, enemy, printInfo=False):
        return 2
