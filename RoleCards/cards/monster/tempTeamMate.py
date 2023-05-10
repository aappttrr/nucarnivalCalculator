from RoleCards.common.nCard import NCard


class TempTeamMate(NCard):
    def __init__(self):
        super(TempTeamMate, self).__init__()
        self.cardId = 'TempTeamMate'
        self.cardName = '临时队友'
        self.skillCD = 4

        self.lv60s5Hp = 10000000
        self.lv60s5Atk = 10000
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        self.isSkillGroup = True
        self.isAttackGroup = True

        self.attackHealMagnification = 1

        self.skillHealMagnificationLv1 = 1
        self.skillHealMagnificationLv2 = 1
        self.skillHealMagnificationLv3 = 1

