from RoleCards.common.nCard import NCard
from RoleCards.enum.cardTypeEnum import CardType


class CommonMonster(NCard):
    def __init__(self):
        super(CommonMonster, self).__init__()
        self.cardId = 'CommonMonster'
        self.cardName = '普通怪'
        self.skillCD = 4

        self.lv60s5Hp = 10000000
        self.lv60s5Atk = 100
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

        self.isSkillGroup = True
        self.isAttackGroup = True

        self.attackMagnification = 1

        self.skillMagnificationLv1 = 1
        self.skillMagnificationLv2 = 1
        self.skillMagnificationLv3 = 1
