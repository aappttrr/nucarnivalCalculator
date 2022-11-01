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

    def skill(self, enemy, printInfo=False):
        self.skillCount = 0
        for role in self.teamMate:
            role.beHealed(2, True)
        return 0

    def attack(self, enemy, printInfo=False):
        for role in self.teamMate:
            role.beHealed(1, True)
        return 0
