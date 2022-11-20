from Props.currencyType import CurrencyType
from Props.gameProp import GameProp
from Props.propTypeEnum import PropType
from decimal import Decimal


# 200钻120体力
def converEnergyToSpiritGem(energy):
    result = energy / 120 * 200
    return round(result)


# 50钻14000金币
def converCoinToSpiritGem(coin):
    result = coin / 14000 * 50
    return round(result)


# 1红钻10点蜜话点
def converVialToSorceryGem(vial, seeAsContract):
    result = converSorceryGemToSpiritGem(vial / 10, seeAsContract)
    return round(result)


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
    result = _ep * 60 * (1 - discount)
    return round(result)


# 1600钻一把钥匙
def converKeyToSpiritGem(key):
    result = key * 1600
    return round(result)


# 5把钥匙合成一把高级钥匙
def converFancyKeyToSpiritGem(key):
    result = converKeyToSpiritGem(key) * 5
    return round(result)


# 1个中级礼物近似于2个初级礼物
def converBasicGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        result = gift * 20 / 12 + converVialToSorceryGem(gift, seeAsContract)
    else:
        result = gift * 20 / 12
    return round(result)


# 20钻6个中级礼物
def converIntermediateGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        result = gift * 20 / 6 + converVialToSorceryGem(gift, seeAsContract)
    else:
        result = gift * 20 / 6
    return round(result)


# 30钻3个高级礼物
def converAdvancedGiftToSpiritGem(gift, countVial, seeAsContract):
    if countVial:
        result = gift * 10 + converVialToSorceryGem(gift, seeAsContract)
    else:
        result = gift * 10
    return round(result)


# 180钻3个回忆图画
def converUltraGiftToSpiritGem(gift):
    result = gift * 60
    return round(result)


# 6个初级潜力道具合成1个中级潜力道具
def converBasicPotentialToSpiritGem(_p):
    result = converIntermediatePotentialToSpiritGem(_p / 6)
    return round(result)


# 80钻2个中级潜力道具
def converIntermediatePotentialToSpiritGem(_p):
    result = _p * 40
    return round(result)


# 80钻1个高级潜力道具
def converAdvancedPotentialToSpiritGem(_p):
    result = _p * 80
    return round(result)


# 600钻一个高级合成潜力道具
def converAdvancedUpPotentialToSpiritGem(_p):
    result = _p * 600
    return round(result)


# 传说潜力道具=2个高级合成+3个中级
def converLegendaryPotentialToSpiritGem(_p):
    result = converAdvancedUpPotentialToSpiritGem(_p * 2) + converIntermediatePotentialToSpiritGem(_p * 3)
    return round(result)


# 1红钻200/600钻石
def converSorceryGemToSpiritGem(sorceryGem, seeAsContract):
    if seeAsContract:
        result = sorceryGem * 600
    else:
        result = sorceryGem * 200
    return round(result)


# 74 eCoin=1个魔蕴石
def converECoinToSpiritGem(ecoin, seeAsContract):
    result = converSorceryGemToSpiritGem(ecoin / 74, seeAsContract)
    return round(result)


# 45红钻1个晶花原石
def converRawCrystalToSpiritGem(crystal, seeAsContract):
    result = converSorceryGemToSpiritGem(45, seeAsContract)
    return round(result)


# 60红钻1个闪耀晶核
def converCrystalCoreToSpiritGem(crystal, seeAsContract):
    result = converSorceryGemToSpiritGem(60, seeAsContract)
    return round(result)


# 攻略组，小型：晶灵石 = 5：4
def converHolyWaterSToSpiritGem(hw):
    result = hw / 5 * 4
    return round(result)


# 攻略组，中型：晶灵石 = 5：8
def converHolyWaterMToSpiritGem(hw):
    result = hw / 5 * 8
    return round(result)


# 大型等于2.5瓶中型
def converHolyWaterLToSpiritGem(hw):
    result = converHolyWaterMToSpiritGem(hw * 2.5)
    return round(result)


# 1红钻25个特大型
def converHolyWaterXLToSpiritGem(hw, seeAsContract):
    result = converSorceryGemToSpiritGem(hw / 25, seeAsContract)
    return round(result)


def roundHalfEven(value):
    return float(Decimal(value).quantize(Decimal("0.01"), rounding='ROUND_HALF_EVEN'))


class CostPerformanceHelper:
    def __init__(self, name=''):
        self.giftPackName = name
        self.gamePropList: list[GameProp] = []
        self.seeSorceryGemAsContract = False
        self.sorcererMojo: int = 5
        self.price = 0
        self.currencyType: CurrencyType = CurrencyType.eCoin
        self.countVial = False
        self.calMap = {}
        self.basicCP = 0
        self.bestCP = 0

    def addGameProp(self, _gp: GameProp):
        self.gamePropList.append(_gp)

    def removeGameProp(self, _gp: GameProp):
        if _gp in self.gamePropList:
            self.gamePropList.remove(_gp)

    def calBasicCostPerformance(self, doConver=True):
        self.seeSorceryGemAsContract = True
        if doConver:
            self.converGamePropList()
        self.basicCP = self.calCostPerformance(True)

    def calBestCostPerformance(self, doConver=True):
        self.seeSorceryGemAsContract = True
        if doConver:
            self.converGamePropList()
        self.bestCP = self.calCostPerformance(False)

    def converGamePropList(self):
        self.calMap = {}
        for gp in self.gamePropList:
            newGp = self.convertToSpiritGem(gp)
            if newGp is not None:
                self.calMap[gp] = newGp

    def calCostPerformance(self, basicSeeSorceryGemAsContract):
        if len(self.gamePropList) == 0 or self.price == 0:
            return 0
        if len(self.calMap) == 0:
            self.converGamePropList()

        cost = 0
        for gp in self.calMap:
            cost += self.calMap[gp].number
        cp = 0
        match self.currencyType:
            case CurrencyType.eCoin:
                cp = cost / converECoinToSpiritGem(self.price, basicSeeSorceryGemAsContract)
            case CurrencyType.spiritGem:
                cp = cost / self.price
            case CurrencyType.sorceryGem:
                cp = cost / converSorceryGemToSpiritGem(self.price, basicSeeSorceryGemAsContract)
        return roundHalfEven(cp)

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
                case PropType.fancyKey:
                    return GameProp(PropType.spiritGem, converFancyKeyToSpiritGem(_gp.number))
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
                case PropType.rawCrystal:
                    return GameProp(PropType.spiritGem,
                                    converRawCrystalToSpiritGem(_gp.number, self.seeSorceryGemAsContract))
                case PropType.crystalCore:
                    return GameProp(PropType.spiritGem,
                                    converCrystalCoreToSpiritGem(_gp.number, self.seeSorceryGemAsContract))
                case PropType.holyWater_S:
                    return GameProp(PropType.spiritGem, converHolyWaterSToSpiritGem(_gp.number))
                case PropType.holyWater_M:
                    return GameProp(PropType.spiritGem, converHolyWaterMToSpiritGem(_gp.number))
                case PropType.holyWater_L:
                    return GameProp(PropType.spiritGem, converHolyWaterLToSpiritGem(_gp.number))
                case PropType.holyWater_XL:
                    return GameProp(PropType.spiritGem,
                                    converHolyWaterXLToSpiritGem(_gp.number, self.seeSorceryGemAsContract))
                case _:
                    return GameProp(PropType.spiritGem, 0)
