from RoleCards.common.card import ICard
from RoleCards.enum.cardRarityEnum import CardRarity


class NCard(ICard):
    def __init__(self):
        super(NCard, self).__init__()
        self.rarity = CardRarity.N

    def setProperties(self, _lv, _star, _bond, _tier):
        super(NCard, self).setProperties(_lv, _star, _bond, _tier)
        if self.tier < 0:
            self.tier = 0
        elif self.tier >= 7:
            self.tier = 6

    # 潜能3被动
    def passive_tier_3(self):
        if self.tier >= 3:
            return True
        return False

    # 潜能6被动
    def passive_tier_6(self):
        if self.tier >= 6:
            return True
        return False

    # 探索被动
    def passive_exploration(self, enemy=None):
        pass

    # 激活
    def activeBuffs(self):
        super(NCard, self).activeBuffs()
        self.passive_tier_3()
        self.passive_tier_6()
