from RoleCards.common.ssrCard import SSRCard
from RoleCards.enum.cardRoleEnum import CardRole


class EliteInstructor(SSRCard):
    def __init__(self):
        super(EliteInstructor, self).__init__()
        self.cardId = 'EliteInstructor'
        self.cardName = '专属指导'
        self.nickName = '教师团'
        self.role = CardRole.Edmond
        # self.cardType = CardType.Light
        # self.occupation = CardOccupation.Striker
        # self.tierType = TierType.Attack
        # self.skillCD = 3
        # self.ped = PassiveEffectivenessDifficulty.veryDifficult
        #
        # self.lv60s5Hp = 6937
        # self.lv60s5Atk = 2277
        # self.hp = self.lv60s5Hp
        # self.atk = self.lv60s5Atk
