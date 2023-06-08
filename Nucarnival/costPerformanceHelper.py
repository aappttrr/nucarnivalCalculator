from Props.gameProp import GameProp
from Props.propTypeEnum import PropType
from Common.ncRound import roundHalfEven


# 120体力=200钻
# 1体力=5/3钻
def converEnergyToSpiritGem(energy):
    result = energy * 5 / 3
    return round(result)


# 14000金币=50钻
# 1金币=1/280钻
def converCoinToSpiritGem(coin):
    result = coin / 280
    return round(result)


# 10点蜜话点=1红钻=200钻
# 1点蜜话点=20钻
def converVialToSorceryGem(vial):
    result = vial * 20
    return round(result)


# 1通关券=60钻（和魔法师特权等级有关）
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


# 1把钥匙=1600钻
def converKeyToSpiritGem(key):
    result = key * 1600
    return round(result)


# 1把高级钥匙=5把钥匙=8000钻
def converFancyKeyToSpiritGem(key):
    result = key * 8000
    return round(result)


# 2个初级礼物近似于1个中级礼物
# 1个初级礼物=0.5个中级礼物=10/6钻
def converBasicGiftToSpiritGem(gift):
    result = gift * 10 / 6
    return round(result)


# 6个中级礼物=20钻
# 1个中级礼物=10/3钻
def converIntermediateGiftToSpiritGem(gift):
    result = gift * 10 / 3
    return round(result)


# 3个高级礼物=30钻
# 1个高级礼物=10钻
def converAdvancedGiftToSpiritGem(gift):
    result = gift * 10
    return round(result)


# 1个高级礼物礼盒=60高级礼物=600钻
def converAdvancedGiftPkgToSpiritGem(giftPkg):
    result = giftPkg * 600
    return round(result)


# 3个回忆图画=180钻
# 1个回忆图画=60钻
def converUltraGiftToSpiritGem(gift):
    result = gift * 60
    return round(result)


# 6个初级潜力道具合成1个中级潜力道具
# 1个初级潜力道具 =40/6钻=20/3钻
def converBasicPotentialToSpiritGem(_p):
    result = _p * 20 / 3
    return round(result)


# 2个中级潜力道具=80钻
# 1个中级潜力道具=40钻
def converIntermediatePotentialToSpiritGem(_p):
    result = _p * 40
    return round(result)


# 1个中级潜力道具礼盒=5个中级潜力道具=200钻
def converIntermediatePotentialPkgToSpiritGem(_p):
    result = _p * 200
    return round(result)


# 1个高级潜力道具=80钻
def converAdvancedPotentialToSpiritGem(_p):
    result = _p * 80
    return round(result)


# 1个高级合成潜力道具=600钻
def converAdvancedUpPotentialToSpiritGem(_p):
    result = _p * 600
    return round(result)


# 传说潜力道具=2个高级合成+3个中级=2*600+3*40钻=1320钻
def converLegendaryPotentialToSpiritGem(_p):
    result = _p * 1320
    return round(result)


# 1红钻200/600钻石
def converSorceryGemToSpiritGem(sorceryGem, seeAsContract):
    if seeAsContract:
        result = sorceryGem * 600
    else:
        result = sorceryGem * 200
    return round(result)


# 1个晶花原石=45红钻=45*200钻=9000钻
def converRawCrystalToSpiritGem(crystal):
    result = crystal * 9000
    return round(result)


# 1个闪耀晶核=60红钻=60*200钻=12000钻
def converCrystalCoreToSpiritGem(crystal):
    result = crystal * 12000
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


# 25个特大型=1红钻=200钻
# 1个特大型=8钻
def converHolyWaterXLToSpiritGem(hw):
    result = hw * 8
    return round(result)


class CostPerformanceHelper:
    def __init__(self, name=''):
        self.giftPackName = name
        self.gamePropList: list[GameProp] = []
        self.sorcererMojo: int = 5
        self.price = 0
        self.basicCP = 0
        self.bestCP = 0
        self.bestCP2 = 0
        self.basicCPMap = {}
        self.bestCPMap = {}

    def converGamePropList(self):
        self.basicCPMap = {}
        self.bestCPMap = {}
        for gp in self.gamePropList:
            newGp = self.convertToSpiritGem(gp, False)
            self.basicCPMap[gp] = newGp
            if gp.propType == PropType.sorceryGem:
                newGp2 = self.convertToSpiritGem(gp, True)
                self.bestCPMap[gp] = newGp2

    def addGameProp(self, _gp: GameProp):
        self.gamePropList.append(_gp)

    def removeGameProp(self, _gp: GameProp):
        if _gp in self.gamePropList:
            self.gamePropList.remove(_gp)

    def calBasicCostPerformance(self):
        cost = 0
        for gp in self.basicCPMap:
            newGp = None
            if gp.propType == PropType.sorceryGem \
                    or gp.propType == PropType.essenceContract or gp.propType == PropType.spiritGem:
                if gp in self.basicCPMap:
                    newGp = self.basicCPMap[gp]
            if newGp is not None:
                cost += newGp.number
        cp = cost / self.price
        self.basicCP = roundHalfEven(cp)

    def calBestCostPerformance(self):
        cost = 0
        for gp in self.basicCPMap:
            newGp = None
            if gp in self.basicCPMap:
                newGp = self.basicCPMap[gp]
            if newGp is not None:
                cost += newGp.number
        cp = cost / self.price
        self.bestCP = roundHalfEven(cp)

    def calBestCostPerformance2(self):
        cost = 0
        for gp in self.basicCPMap:
            newGp = None
            if gp.propType == PropType.sorceryGem and gp in self.bestCPMap:
                newGp = self.bestCPMap[gp]
            elif gp in self.basicCPMap:
                newGp = self.basicCPMap[gp]
            if newGp is not None:
                cost += newGp.number
        cp = cost / self.price
        self.bestCP2 = roundHalfEven(cp)

    def calCostPerformance(self):
        self.converGamePropList()
        self.calBasicCostPerformance()
        self.calBestCostPerformance()
        self.calBestCostPerformance2()

    def convertToSpiritGem(self, _gp: GameProp, seeSorceryGemAsContract=False):
        if _gp.propType is None:
            return None
        elif _gp.propType == PropType.spiritGem:
            return _gp
        else:
            match _gp.propType:
                case PropType.sorceryGem:
                    return GameProp(PropType.spiritGem,
                                    converSorceryGemToSpiritGem(_gp.number, seeSorceryGemAsContract))
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
                case PropType.intermediatePotentialPkg:
                    return GameProp(PropType.spiritGem, converIntermediatePotentialPkgToSpiritGem(_gp.number))
                case PropType.advancedPotential:
                    return GameProp(PropType.spiritGem, converAdvancedPotentialToSpiritGem(_gp.number))
                case PropType.advancedUpPotential:
                    return GameProp(PropType.spiritGem, converAdvancedUpPotentialToSpiritGem(_gp.number))
                case PropType.legendaryPotential:
                    return GameProp(PropType.spiritGem, converLegendaryPotentialToSpiritGem(_gp.number))
                case PropType.smallEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number))
                case PropType.middleEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number * 5))
                case PropType.bigEssenceVial:
                    return GameProp(PropType.spiritGem,
                                    converVialToSorceryGem(_gp.number * 10))
                case PropType.expressPass:
                    return GameProp(PropType.spiritGem, converExpressPassToSorceryGem(_gp.number, self.sorcererMojo))
                case PropType.key:
                    return GameProp(PropType.spiritGem, converKeyToSpiritGem(_gp.number))
                case PropType.fancyKey:
                    return GameProp(PropType.spiritGem, converFancyKeyToSpiritGem(_gp.number))
                case PropType.basicGift:
                    return GameProp(PropType.spiritGem,
                                    converBasicGiftToSpiritGem(_gp.number))
                case PropType.intermediateGift:
                    return GameProp(PropType.spiritGem,
                                    converIntermediateGiftToSpiritGem(_gp.number))
                case PropType.advancedGift:
                    return GameProp(PropType.spiritGem,
                                    converAdvancedGiftToSpiritGem(_gp.number))
                case PropType.advancedGiftPkg:
                    return GameProp(PropType.spiritGem,
                            converAdvancedGiftPkgToSpiritGem(_gp.number))
                case PropType.ultraGift:
                    return GameProp(PropType.spiritGem, converUltraGiftToSpiritGem(_gp.number))
                case PropType.rawCrystal:
                    return GameProp(PropType.spiritGem,
                                    converRawCrystalToSpiritGem(_gp.number))
                case PropType.crystalCore:
                    return GameProp(PropType.spiritGem,
                                    converCrystalCoreToSpiritGem(_gp.number))
                case PropType.holyWater_S:
                    return GameProp(PropType.spiritGem, converHolyWaterSToSpiritGem(_gp.number))
                case PropType.holyWater_M:
                    return GameProp(PropType.spiritGem, converHolyWaterMToSpiritGem(_gp.number))
                case PropType.holyWater_L:
                    return GameProp(PropType.spiritGem, converHolyWaterLToSpiritGem(_gp.number))
                case PropType.holyWater_XL:
                    return GameProp(PropType.spiritGem,
                                    converHolyWaterXLToSpiritGem(_gp.number))
                case _:
                    return GameProp(PropType.spiritGem, 0)
