from RoleCards.common.nCard import NCard
from RoleCards.enum.cardTypeEnum import CardType


class CommonMonster(NCard):
    def __init__(self):
        super(CommonMonster, self).__init__()
        self.cardId = 'CommonMonster'
        self.cardName = '普通怪'
        self.skillCD = 4

        self.lv60s5Hp = 10000000
        self.lv60s5Atk = 1
        self.hp = self.lv60s5Hp
        self.atk = self.lv60s5Atk

    def skill(self, enemy, printInfo=False):
        self.skillCount = 0

        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 2,  False, True)

        return damage

    def attack(self, enemy, printInfo=False):
        currentAtk = self.getCurrentAtk()
        damage = self.calDamage(currentAtk, 1, True, False)

        return damage
