from Props.currencyType import CurrencyType
from Props.gameProp import GameProp
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


# 60钻1通关券（和魔法师特权等级有关）
def converExpressPassToSorceryGem(_ep, mojo: int):
    discount = 0
    match mojo:
        case 2:
            discount = 0.15
        case 3:
            discount = 0.2
        case 4:
            discount = 0.35
        case 5:
            discount = 0.4
        case 6:
            discount = 0.45
        case 7:
            discount = 0.5
        case 8:
            discount = 0.55
        case 9:
            discount = 0.6
        case 10:
            discount = 0.65
        case 11:
            discount = 0.7
        case 12:
            discount = 0.75
        case 13:
            discount = 0.8
        case 14:
            discount = 0.84
        case 15:
            discount = 0.87
    return _ep * 60 * (1 - discount)


# 1600钻一把钥匙
def converKeyToSpiritGem(key):
    return key * 1600


# 1个中级礼物近似于2个初级礼物
def converBasicGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        return gift * 20 / 12 + converVialToSorceryGem(gift, seeAsContract)
    else:
        return gift * 20 / 12


# 20钻6个中级礼物
def converIntermediateGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        return gift * 20 / 6 + converVialToSorceryGem(gift, seeAsContract)
    else:
        return gift * 20 / 6


# 30钻3个高级礼物
def converAdvancedGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        return gift * 10 + converVialToSorceryGem(gift, seeAsContract)
    else:
        return gift * 10


# 200钻1个回忆图画
def converUltraGiftToSpiritGem(gift):
    return gift * 200


# 6个初级潜力道具合成1个中级潜力道具
def converBasicPotentialToSpiritGem(_p):
    return converIntermediatePotentialToSpiritGem(_p / 6)


# 80钻2个中级潜力道具
def converIntermediatePotentialToSpiritGem(_p):
    return _p * 40


# 80钻1个高级潜力道具
def converAdvancedPotentialToSpiritGem(_p):
    return _p * 80


# 高级合成潜力道具=4个中级+4个初级
def converAdvancedUpPotentialToSpiritGem(_p):
    return converIntermediatePotentialToSpiritGem(_p * 4) + converBasicPotentialToSpiritGem(_p * 4)


# 传说潜力道具=2个高级合成+3个中级
def converLegendaryPotentialToSpiritGem(_p):
    return converAdvancedUpPotentialToSpiritGem(_p * 2) + converIntermediatePotentialToSpiritGem(_p * 3)


# 1红钻200/600钻石
def converSorceryGemToSpiritGem(sorceryGem, seeAsContract):
    if seeAsContract:
        return sorceryGem * 600
    else:
        return sorceryGem * 200


# 无折扣最低级魔蕴石购入，74 eCoin=1个魔蕴石
def converSpiritGemToECoin(spiritGem, seeAsContract):
    if seeAsContract:
        return spiritGem / 600 * 74
    else:
        return spiritGem / 200 * 74


class CostPerformanceHelper:
    def __init__(self, name=''):
        self.giftPackName = name
        self.gamePropList: list[GameProp] = []
        self.seeSorceryGemAsContract = False
        self.sorcererMojo: int = 1
        self.price = 0
        self.currencyType: CurrencyType = CurrencyType.eCoin
        self.countVial = False

    def addGameProp(self, _gp:GameProp):
        self.gamePropList.append(_gp)

    def removeGameProp(self, _gp:GameProp):
        if _gp in self.gamePropList:
            self.gamePropList.remove(_gp)

    def calCostPerformance(self, basicSeeSorceryGemAsContract):
        if len(self.gamePropList) == 0 or self.price == 0:
            return 0
        calList: list[GameProp] = []
        for gp in self.gamePropList:
            newGp = self.convertToSpiritGem(gp)
            if newGp is not None:
                calList.append(newGp)
        cost = 0
        for gp in calList:
            cost += gp.number
        cp = 0
        match self.currencyType:
            case CurrencyType.eCoin:
                cp = converSpiritGemToECoin(cost, basicSeeSorceryGemAsContract) / self.price
            case CurrencyType.spiritGem:
                cp = cost / self.price
            case CurrencyType.sorceryGem:
                if basicSeeSorceryGemAsContract:
                    cp = cost / (self.price * 600)
                else:
                    cp = cost / (self.price * 200)
        return cp

    def convertToSpiritGem(self, _gp: GameProp):
        if _gp.propType is None:
            return None
        elif _gp.propType == PropType.spiritGem:
            return _gp
        else:
            match _gp.propType:
                case PropType.sorceryGem:
                    return GameProp(PropType.spiritGem,
                                    converSorceryGemToSpiritGem(_gp.number, self.seeSorceryGemAsContract))
                case PropType.essenceContract:
                    return GameProp(PropType.spiritGem, 600 * _gp.number)
                case PropType.coin:
                    return GameProp(PropType.spiritGem, converCoinToSpiritGem(_gp.number))
                case PropType.tinyBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(_gp.number * 10))
                case PropType.basicBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(_gp.number * 30))
                case PropType.strongBoost:
                    return GameProp(PropType.spiritGem, converEnergyToSpiritGem(_gp.number * 100))
                case PropType.basicPotential:
                    return GameProp(PropType.spiritGem, converBasicPotentialToSpiritGem(_gp.number))
                case PropType.intermediatePotential:
                    return GameProp(PropType.spiritGem, converIntermediatePotentialToSpiritGem(_gp.number))
                case PropType.advancedPotential:
                    return GameProp(PropType.spiritGem, converAdvancedPotentialToSpiritGem(_gp.number))
                case PropType.advancedUpPotential:
                    return GameProp(PropType.spiritGem, converAdvancedUpPotentialToSpiritGem(_gp.number))
                case PropType.legendaryPotential:
                    return GameProp(PropType.spiritGem, converLegendaryPotentialToSpiritGem(_gp.number))
                case PropType.smallEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number, self.seeSorceryGemAsContract))
                case PropType.middleEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number * 5, self.seeSorceryGemAsContract))
                case PropType.bigEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number * 10, self.seeSorceryGemAsContract))
                case PropType.expressPass:
                    return GameProp(PropType.spiritGem, converExpressPassToSorceryGem(_gp.number, self.sorcererMojo))
                case PropType.key:
                    return GameProp(PropType.spiritGem, converKeyToSpiritGem(_gp.number))
                case PropType.basicGift:
                    return GameProp(PropType.spiritGem,
                                    converBasicGiftToSpiritGem(_gp.number, self.countVial,
                                                               self.seeSorceryGemAsContract))
                case PropType.intermediateGift:
                    return GameProp(PropType.spiritGem,
                                    converIntermediateGiftToSpiritGem(_gp.number, self.countVial,
                                                                      self.seeSorceryGemAsContract))
                case PropType.advancedGift:
                    return GameProp(PropType.spiritGem,
                                    converAdvancedGiftToSpiritGem(_gp.number, self.countVial,
                                                                  self.seeSorceryGemAsContract))
                case PropType.ultraGift:
                    return GameProp(PropType.spiritGem, converUltraGiftToSpiritGem(_gp.number))
