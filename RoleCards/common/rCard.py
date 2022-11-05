from RoleCards.enum.cardRarityEnum import CardRarity
from RoleCards.enum.tierType import TierType
from card import ICard


class RCard(ICard):
    def __init__(self):
        super(RCard, self).__init__()
        self.rarity = CardRarity.R
        self.tierType = TierType.RandN

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
    def passive_exploration(self):
        pass

    # 激活
    def activeBuffs(self):
        super(RCard, self).activeBuffs()
        self.passive_tier_3()
        self.passive_tier_6()

