from Nucarnival.costPerformanceHelper import CostPerformanceHelper
from Props.currencyType import CurrencyType
from Props.gameProp import GameProp
from Props.propTypeEnum import PropType

def initGiftPacks():
    giftPacks: list[CostPerformanceHelper] = []
    xyk = CostPerformanceHelper('小月卡')
    xyk.addGameProp(GameProp(PropType.sorceryGem, 3))
    xyk.addGameProp(GameProp(PropType.basicBoost, 60))
    xyk.currencyType = CurrencyType.eCoin
    xyk.price = 224
    giftPacks.append(xyk)

    dyk = CostPerformanceHelper('大月卡')
    dyk.addGameProp(GameProp(PropType.sorceryGem, 8))
    dyk.addGameProp(GameProp(PropType.spiritGem, 3000))
    dyk.addGameProp(GameProp(PropType.strongBoost, 30))
    dyk.currencyType = CurrencyType.eCoin
    dyk.price = 599
    giftPacks.append(dyk)

    lxyyb = CostPerformanceHelper('旅行应援包')
    lxyyb.addGameProp(GameProp(PropType.spiritGem, 500))
    lxyyb.addGameProp(GameProp(PropType.strongBoost, 10))
    lxyyb.currencyType = CurrencyType.eCoin
    lxyyb.price = 374
    giftPacks.append(lxyyb)

    ctlxyyb = CostPerformanceHelper('长途旅行应援包')
    ctlxyyb.addGameProp(GameProp(PropType.sorceryGem, 6))
    ctlxyyb.addGameProp(GameProp(PropType.basicBoost, 20))
    ctlxyyb.currencyType = CurrencyType.eCoin
    ctlxyyb.price = 374
    giftPacks.append(ctlxyyb)

    xsjqclb = CostPerformanceHelper('新世界启程礼包')
    xsjqclb.addGameProp(GameProp(PropType.essenceContract, 5))
    xsjqclb.addGameProp(GameProp(PropType.coin, 30000))
    xsjqclb.addGameProp(GameProp(PropType.holyWater_S, 30))
    xsjqclb.currencyType = CurrencyType.eCoin
    xsjqclb.price = 299
    giftPacks.append(xsjqclb)

    zfyyb = CostPerformanceHelper('祝福应援礼包')
    zfyyb.addGameProp(GameProp(PropType.spiritGem, 2000))
    zfyyb.addGameProp(GameProp(PropType.coin, 100000))
    zfyyb.addGameProp(GameProp(PropType.holyWater_S, 60))
    zfyyb.addGameProp(GameProp(PropType.holyWater_M, 20))
    zfyyb.currencyType = CurrencyType.eCoin
    zfyyb.price = 674
    giftPacks.append(zfyyb)

    qlkfyylb = CostPerformanceHelper('潜力开发应援礼包')
    qlkfyylb.addGameProp(GameProp(PropType.spiritGem, 1000))
    qlkfyylb.addGameProp(GameProp(PropType.coin, 300000))
    # 未完成
    qlkfyylb.currencyType = CurrencyType.eCoin
    qlkfyylb.price = 1199
    giftPacks.append(qlkfyylb)

    yslb = CostPerformanceHelper('钥匙礼包（烈焰情深等）')
    yslb.addGameProp(GameProp(PropType.essenceContract, 10))
    yslb.addGameProp(GameProp(PropType.key, 1))
    yslb.addGameProp(GameProp(PropType.ultraGift, 60))
    yslb.currencyType = CurrencyType.eCoin
    yslb.price = 4224
    giftPacks.append(yslb)

    tmjy = CostPerformanceHelper('甜蜜记忆')
    tmjy.addGameProp(GameProp(PropType.essenceContract, 6))
    tmjy.addGameProp(GameProp(PropType.key, 5))
    tmjy.addGameProp(GameProp(PropType.ultraGift, 30))
    tmjy.currencyType = CurrencyType.eCoin
    tmjy.price = 1675
    giftPacks.append(tmjy)
    
    srlb = CostPerformanceHelper('生日礼包')
    srlb.addGameProp(GameProp(PropType.spiritGem, 1000))
    srlb.addGameProp(GameProp(PropType.bigEssenceVial, 20))
    srlb.addGameProp(GameProp(PropType.ultraGift, 40))
    srlb.currencyType = CurrencyType.eCoin
    srlb.price = 1450
    giftPacks.append(srlb)
    
    # 主线礼包
    c1lb = CostPerformanceHelper('欢庆第1章突破')
    c1lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c1lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c1lb.currencyType = CurrencyType.eCoin
    c1lb.price = 1049
    giftPacks.append(c1lb)

    c2lb = CostPerformanceHelper('欢庆第2章突破')
    c2lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c2lb.addGameProp(GameProp(PropType.SR_Fragment, 24))
    c2lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c2lb.currencyType = CurrencyType.eCoin
    c2lb.price = 2249
    giftPacks.append(c2lb)
    
    c3lb = CostPerformanceHelper('欢庆第3章突破')
    c3lb.addGameProp(GameProp(PropType.essenceContract, 5))
    c3lb.addGameProp(GameProp(PropType.spiritGem, 150))
    c3lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c3lb.addGameProp(GameProp(PropType.intermediatePotential, 5))
    c3lb.currencyType = CurrencyType.eCoin
    c3lb.price = 674
    giftPacks.append(c3lb)
    
    c4lb = CostPerformanceHelper('欢庆第4章突破')
    c4lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c2lb.addGameProp(GameProp(PropType.SR_Fragment, 6))
    c4lb.addGameProp(GameProp(PropType.holyWater_L, 10))
    c4lb.addGameProp(GameProp(PropType.advancedGift, 5))
    c4lb.currencyType = CurrencyType.eCoin
    c4lb.price = 1724
    giftPacks.append(c4lb)
    
    # 常见活动礼包
    hdlb4 = CostPerformanceHelper('常见活动礼包4')
    hdlb4.addGameProp(GameProp(PropType.spiritGem, 1000))
    hdlb4.addGameProp(GameProp(PropType.essenceContract, 10))
    hdlb4.addGameProp(GameProp(PropType.coin, 100000))
    hdlb4.currencyType = CurrencyType.eCoin
    hdlb4.price = 1245
    giftPacks.append(hdlb4)
    
    hdlb5 = CostPerformanceHelper('常见活动礼包5')
    hdlb5.addGameProp(GameProp(PropType.spiritGem, 3000))
    hdlb5.addGameProp(GameProp(PropType.essenceContract, 25))
    hdlb5.addGameProp(GameProp(PropType.coin, 300000))
    hdlb5.currencyType = CurrencyType.eCoin
    hdlb5.price = 2979
    giftPacks.append(hdlb5)
    
    return giftPacks

if __name__ == '__main__':
    giftPacks = initGiftPacks()
    
    


