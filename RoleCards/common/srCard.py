from RoleCards.common.card import ICard
from RoleCards.enum.cardRarityEnum import CardRarity


class SRCard(ICard):
    def __init__(self):
        super(SRCard, self).__init__()
        self.rarity = CardRarity.SR

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
        super(SRCard, self).activeBuffs()
        self.passive_tier_6()
        self.passive_tier_12()