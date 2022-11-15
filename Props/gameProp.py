from Props.propTypeEnum import PropType


# 200钻120体力
def converEnergyToSpiritGem(energy):
    return energy * 200 / 120

# 50钻14000金币
def converCoinToSpiritGem(coin):
    return coin * 50 / 14000

# 1红钻10点蜜话点
def converVialToSorceryGem(vial, seeAsContract):
    return converSorceryGemToSpiritGem(vial / 10, seeAsContract)

# 1红钻200/600钻石
def converSorceryGemToSpiritGem(sorceryGem, seeAsContract):
    if seeAsContract:
        return sorceryGem * 600
    else:
        return sorceryGem * 200

class GameProp:
    def __init__(self, _propType: PropType, _number):
        self.propType: PropType = _propType
        self.number = _number
        self.seeSorceryGemAsContract = False

    def convertToSpiritGem(self):
        if self.propType is None:
            return None
        elif self.propType == PropType.spiritGem:
            return self
        else:
            match self.propType:
                case PropType.sorceryGem:
                    return GameProp(PropType.spiritGem,
                                    converSorceryGemToSpiritGem(self.number, self.seeSorceryGemAsContract))
                case PropType.essenceContract:
                    return GameProp(PropType.spiritGem, 600 * self.number)
                case PropType.coin:
                    return GameProp(PropType.spiritGem, converCoinToSpiritGem(self.number))
                case PropType.tinyBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(self.number * 10))
                case PropType.basicBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(self.number * 30))
                case PropType.strongBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(self.number * 100))
                case PropType.basicPotential:
                    pass
                case PropType.intermediatePotential:
                    pass
                case PropType.advancedPotential:
                    pass
                case PropType.advancedUpPotential:
                    pass
                case PropType.legendaryPotential:
                    pass
                case PropType.smallEssenceVial:
                    return GameProp(PropType.spiritGem, converVialToSorceryGem(1, self.seeSorceryGemAsContract))
                case PropType.middleEssenceVial:
                    pass
                case PropType.bigEssenceVial:
                    pass
                case PropType.expressPass:
                    pass
                case PropType.key:
                    pass
                case PropType.basicGift:
                    pass
                case PropType.intermediateGift:
                    pass
                case PropType.advancedGift:
                    pass
                case PropType.ultraGift:
                    pass
