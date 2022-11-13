from RoleCards.common.card import ICard
from RoleCards.enum.cardRarityEnum import CardRarity


class SSRCard(ICard):
    def __init__(self):
        super(SSRCard, self).__init__()
        self.rarity = CardRarity.SSR

    def setProperties(self, _lv, _star, _bond, _tier):
        super(SSRCard, self).setProperties(_lv, _star, _bond, _tier)
        if self.tier < 0:
            self.tier = 0
        elif self.tier >= 13:
            self.tier = 12

    # 潜能6被动
    def passive_tier_6(self):
        if self.tier >= 6:
            return True
        return False

    # 潜能12被动
    def passive_tier_12(self):
        if self.tier >= 12:
            return True
        return False

    # 激活
    def activeBuffs(self):
        super(SSRCard, self).activeBuffs()
        self.passive_tier_6()
        self.passive_tier_12()
