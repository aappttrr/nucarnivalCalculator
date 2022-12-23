from Nucarnival.costPerformanceHelper import CostPerformanceHelper
from Props.currencyType import CurrencyType
from Props.gameProp import GameProp
from Props.propTypeEnum import PropType, PropTypes
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


# 商店礼包
def shopGiftPacks(gps: list[CostPerformanceHelper]):
    xyk = CostPerformanceHelper('小月卡')
    xyk.addGameProp(GameProp(PropType.sorceryGem, 3))
    xyk.addGameProp(GameProp(PropType.basicBoost, 60))
    xyk.currencyType = CurrencyType.eCoin
    xyk.price = 224
    gps.append(xyk)

    dyk = CostPerformanceHelper('大月卡')
    dyk.addGameProp(GameProp(PropType.sorceryGem, 8))
    dyk.addGameProp(GameProp(PropType.spiritGem, 3000))
    dyk.addGameProp(GameProp(PropType.strongBoost, 30))
    dyk.currencyType = CurrencyType.eCoin
    dyk.price = 599
    gps.append(dyk)

    lxyyb = CostPerformanceHelper('旅行应援包')
    lxyyb.addGameProp(GameProp(PropType.spiritGem, 500))
    lxyyb.addGameProp(GameProp(PropType.strongBoost, 10))
    lxyyb.currencyType = CurrencyType.eCoin
    lxyyb.price = 374
    gps.append(lxyyb)

    ctlxyyb = CostPerformanceHelper('长途旅行应援包')
    ctlxyyb.addGameProp(GameProp(PropType.sorceryGem, 6))
    ctlxyyb.addGameProp(GameProp(PropType.basicBoost, 20))
    ctlxyyb.currencyType = CurrencyType.eCoin
    ctlxyyb.price = 374
    gps.append(ctlxyyb)

    xsjqclb = CostPerformanceHelper('新世界启程礼包')
    xsjqclb.addGameProp(GameProp(PropType.essenceContract, 5))
    xsjqclb.addGameProp(GameProp(PropType.coin, 30000))
    xsjqclb.addGameProp(GameProp(PropType.holyWater_S, 30))
    xsjqclb.currencyType = CurrencyType.eCoin
    xsjqclb.price = 299
    gps.append(xsjqclb)

    zfyyb = CostPerformanceHelper('祝福应援礼包')
    zfyyb.addGameProp(GameProp(PropType.spiritGem, 2000))
    zfyyb.addGameProp(GameProp(PropType.coin, 100000))
    zfyyb.addGameProp(GameProp(PropType.holyWater_S, 60))
    zfyyb.addGameProp(GameProp(PropType.holyWater_M, 20))
    zfyyb.currencyType = CurrencyType.eCoin
    zfyyb.price = 674
    gps.append(zfyyb)

    qlkfyylb = CostPerformanceHelper('潜力开发应援礼包')
    qlkfyylb.addGameProp(GameProp(PropType.spiritGem, 1000))
    qlkfyylb.addGameProp(GameProp(PropType.coin, 300000))
    qlkfyylb.addGameProp(GameProp(PropType.basicPotential, 98))
    qlkfyylb.addGameProp(GameProp(PropType.intermediatePotential, 40))
    # 未完成
    qlkfyylb.currencyType = CurrencyType.eCoin
    qlkfyylb.price = 1199
    gps.append(qlkfyylb)

    yslb = CostPerformanceHelper('钥匙礼包（烈焰情深等）')
    yslb.addGameProp(GameProp(PropType.essenceContract, 10))
    yslb.addGameProp(GameProp(PropType.fancyKey, 1))
    yslb.addGameProp(GameProp(PropType.ultraGift, 60))
    yslb.currencyType = CurrencyType.eCoin
    yslb.price = 4224
    gps.append(yslb)

    tmjy = CostPerformanceHelper('甜蜜记忆')
    tmjy.addGameProp(GameProp(PropType.essenceContract, 8))
    tmjy.addGameProp(GameProp(PropType.key, 5))
    tmjy.addGameProp(GameProp(PropType.ultraGift, 30))
    tmjy.currencyType = CurrencyType.eCoin
    tmjy.price = 1675
    gps.append(tmjy)
    return gps


# 主线礼包
def chapterGiftPacks(gps: list[CostPerformanceHelper]):
    c1lb = CostPerformanceHelper('欢庆第1章突破')
    c1lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c1lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c1lb.currencyType = CurrencyType.eCoin
    c1lb.price = 1049
    gps.append(c1lb)

    c1lbsp = CostPerformanceHelper('欢庆第1章突破SP')
    c1lbsp.addGameProp(GameProp(PropType.spiritGem, 3000))
    c1lbsp.addGameProp(GameProp(PropType.sr_Fragment, 40))
    c1lbsp.addGameProp(GameProp(PropType.holyWater_M, 10))
    c1lbsp.currencyType = CurrencyType.eCoin
    c1lbsp.price = 4224
    gps.append(c1lbsp)

    c2lb = CostPerformanceHelper('欢庆第2章突破')
    c2lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c2lb.addGameProp(GameProp(PropType.sr_Fragment, 24))
    c2lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c2lb.currencyType = CurrencyType.eCoin
    c2lb.price = 2249
    gps.append(c2lb)

    c2lbsp = CostPerformanceHelper('欢庆第2章突破SP')
    c2lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c2lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c2lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c2lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c2lbsp.currencyType = CurrencyType.eCoin
    c2lbsp.price = 7499
    gps.append(c2lbsp)

    c3lb = CostPerformanceHelper('欢庆第3章突破')
    c3lb.addGameProp(GameProp(PropType.essenceContract, 5))
    c3lb.addGameProp(GameProp(PropType.spiritGem, 150))
    c3lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c3lb.addGameProp(GameProp(PropType.intermediatePotential, 5))
    c3lb.currencyType = CurrencyType.eCoin
    c3lb.price = 674
    gps.append(c3lb)

    c3lbsp = CostPerformanceHelper('欢庆第3章突破SP')
    c3lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c3lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c3lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c3lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c3lbsp.currencyType = CurrencyType.eCoin
    c3lbsp.price = 7499
    gps.append(c3lbsp)

    c4lb = CostPerformanceHelper('欢庆第4章突破')
    c4lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c4lb.addGameProp(GameProp(PropType.sr_Fragment, 6))
    c4lb.addGameProp(GameProp(PropType.holyWater_L, 10))
    c4lb.addGameProp(GameProp(PropType.advancedGift, 5))
    c4lb.currencyType = CurrencyType.eCoin
    c4lb.price = 1724
    gps.append(c4lb)

    c4lbsp = CostPerformanceHelper('欢庆第4章突破SP')
    c4lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c4lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c4lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c4lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c4lbsp.currencyType = CurrencyType.eCoin
    c4lbsp.price = 7499
    gps.append(c4lbsp)

    c5lb = CostPerformanceHelper('欢庆第5章突破')
    c5lb.addGameProp(GameProp(PropType.essenceContract, 5))
    c5lb.addGameProp(GameProp(PropType.spiritGem, 300))
    c5lb.currencyType = CurrencyType.eCoin
    c5lb.price = 674
    gps.append(c5lb)

    c5lbsp = CostPerformanceHelper('欢庆第5章突破SP')
    c5lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c5lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c5lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c5lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c5lbsp.currencyType = CurrencyType.eCoin
    c5lbsp.price = 7499
    gps.append(c5lbsp)

    c6lb = CostPerformanceHelper('欢庆第6章突破')
    c6lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c6lb.addGameProp(GameProp(PropType.sr_Fragment, 6))
    c6lb.addGameProp(GameProp(PropType.intermediatePotential, 3))
    c6lb.currencyType = CurrencyType.eCoin
    c6lb.price = 1724
    gps.append(c6lb)

    c6lbsp = CostPerformanceHelper('欢庆第6章突破SP')
    c6lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c6lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c6lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c6lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c6lbsp.currencyType = CurrencyType.eCoin
    c6lbsp.price = 7499
    gps.append(c6lbsp)

    c7lb = CostPerformanceHelper('欢庆第7章突破')
    c7lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c7lb.addGameProp(GameProp(PropType.spiritGem, 1500))
    c7lb.addGameProp(GameProp(PropType.holyWater_M, 10))
    c7lb.addGameProp(GameProp(PropType.intermediatePotential, 5))
    c7lb.currencyType = CurrencyType.eCoin
    c7lb.price = 1724
    gps.append(c7lb)

    c7lbsp = CostPerformanceHelper('欢庆第7章突破SP')
    c7lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c7lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c7lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c7lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c7lbsp.currencyType = CurrencyType.eCoin
    c7lbsp.price = 7499
    gps.append(c7lbsp)

    c8lb = CostPerformanceHelper('欢庆第8章突破')
    c8lb.addGameProp(GameProp(PropType.essenceContract, 5))
    c8lb.addGameProp(GameProp(PropType.holyWater_M, 20))
    c8lb.addGameProp(GameProp(PropType.intermediatePotential, 5))
    c8lb.currencyType = CurrencyType.eCoin
    c8lb.price = 674
    gps.append(c8lb)

    c8lbsp = CostPerformanceHelper('欢庆第8章突破SP')
    c8lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c8lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c8lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c8lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c8lbsp.currencyType = CurrencyType.eCoin
    c8lbsp.price = 7499
    gps.append(c8lbsp)

    c9lb = CostPerformanceHelper('欢庆第9章突破')
    c9lb.addGameProp(GameProp(PropType.essenceContract, 10))
    c9lb.addGameProp(GameProp(PropType.holyWater_L, 10))
    c9lb.addGameProp(GameProp(PropType.advancedPotential, 5))
    c9lb.currencyType = CurrencyType.eCoin
    c9lb.price = 1724
    gps.append(c9lb)

    c9lbsp = CostPerformanceHelper('欢庆第9章突破SP')
    c9lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c9lbsp.addGameProp(GameProp(PropType.ssr_Role, 1))
    c9lbsp.addGameProp(GameProp(PropType.ssr_Fragment, 10))
    c9lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c9lbsp.currencyType = CurrencyType.eCoin
    c9lbsp.price = 7499
    gps.append(c9lbsp)

    c10lb = CostPerformanceHelper('第10章迎战礼包')
    c10lb.addGameProp(GameProp(PropType.spiritGem, 2000))
    c10lb.addGameProp(GameProp(PropType.holyWater_L, 30))
    c10lb.addGameProp(GameProp(PropType.coin, 300000))
    c10lb.addGameProp(GameProp(PropType.strongBoost, 10))
    c10lb.currencyType = CurrencyType.eCoin
    c10lb.price = 1225
    gps.append(c10lb)

    c10lbsp = CostPerformanceHelper('第10章迎战礼包SP')
    c10lbsp.addGameProp(GameProp(PropType.essenceContract, 30))
    c10lbsp.addGameProp(GameProp(PropType.crystalCore, 1))
    c10lbsp.addGameProp(GameProp(PropType.holyWater_L, 20))
    c10lbsp.currencyType = CurrencyType.eCoin
    c10lbsp.price = 6000
    gps.append(c10lbsp)

    c10lb_2 = CostPerformanceHelper('第10章征战礼包')
    c10lb_2.addGameProp(GameProp(PropType.spiritGem, 2000))
    c10lb_2.addGameProp(GameProp(PropType.holyWater_L, 30))
    c10lb_2.addGameProp(GameProp(PropType.coin, 200000))
    c10lb_2.addGameProp(GameProp(PropType.strongBoost, 20))
    c10lb_2.currencyType = CurrencyType.eCoin
    c10lb_2.price = 1724
    gps.append(c10lb_2)
    return gps


# 常见活动礼包
def activityGiftPacks(gps: list[CostPerformanceHelper]):
    # birthdaylb = CostPerformanceHelper('生日礼包')
    # birthdaylb.addGameProp(GameProp(PropType.spiritGem, 1000))
    # birthdaylb.addGameProp(GameProp(PropType.bigEssenceVial, 20))
    # birthdaylb.addGameProp(GameProp(PropType.ultraGift, 40))
    # birthdaylb.currencyType = CurrencyType.eCoin
    # birthdaylb.price = 1450
    # gps.append(birthdaylb)

    hdlb1 = CostPerformanceHelper('常见活动礼包1（暖冬祈愿）')
    hdlb1.addGameProp(GameProp(PropType.essenceContract, 5))
    hdlb1.addGameProp(GameProp(PropType.coin, 50000))
    hdlb1.currencyType = CurrencyType.eCoin
    hdlb1.price = 345
    gps.append(hdlb1)

    hdlb2 = CostPerformanceHelper('常见活动礼包2（白霭歌颂）')
    hdlb2.addGameProp(GameProp(PropType.essenceContract, 15))
    hdlb2.addGameProp(GameProp(PropType.coin, 100000))
    hdlb2.addGameProp(GameProp(PropType.basicBoost, 20))
    hdlb2.currencyType = CurrencyType.eCoin
    hdlb2.price = 1450
    gps.append(hdlb2)

    hdlb3 = CostPerformanceHelper('常见活动礼包3（瑞雪庆贺）')
    hdlb3.addGameProp(GameProp(PropType.spiritGem, 1000))
    hdlb3.addGameProp(GameProp(PropType.essenceContract, 30))
    hdlb3.addGameProp(GameProp(PropType.basicBoost, 30))
    hdlb3.currencyType = CurrencyType.eCoin
    hdlb3.price = 2979
    gps.append(hdlb3)

    # hdlb4 = CostPerformanceHelper('常见活动礼包4（星夜细语）')
    # hdlb4.addGameProp(GameProp(PropType.spiritGem, 1000))
    # hdlb4.addGameProp(GameProp(PropType.essenceContract, 10))
    # hdlb4.addGameProp(GameProp(PropType.coin, 100000))
    # hdlb4.currencyType = CurrencyType.eCoin
    # hdlb4.price = 1245
    # gps.append(hdlb4)
    #
    # hdlb5 = CostPerformanceHelper('常见活动礼包5（星夜行歌）')
    # hdlb5.addGameProp(GameProp(PropType.spiritGem, 3000))
    # hdlb5.addGameProp(GameProp(PropType.essenceContract, 25))
    # hdlb5.addGameProp(GameProp(PropType.coin, 300000))
    # hdlb5.currencyType = CurrencyType.eCoin
    # hdlb5.price = 2979
    # gps.append(hdlb5)

    bglb = CostPerformanceHelper('背景图礼包（心荡共鸣、雪季之礼、冬景巡游）')
    bglb.addGameProp(GameProp(PropType.essenceContract, 10))
    bglb.addGameProp(GameProp(PropType.coin, 300000))
    bglb.addGameProp(GameProp(PropType.background, 1))
    bglb.currencyType = CurrencyType.eCoin
    bglb.price = 1660
    gps.append(bglb)

    rwlb = CostPerformanceHelper('晶花原石礼包（雪色祝福）')
    rwlb.addGameProp(GameProp(PropType.essenceContract, 50))
    rwlb.addGameProp(GameProp(PropType.rawCrystal, 1))
    rwlb.currencyType = CurrencyType.eCoin
    rwlb.price = 6920
    gps.append(rwlb)

    xclb = CostPerformanceHelper('春报新愿')
    xclb.addGameProp(GameProp(PropType.spiritGem, 2023))
    xclb.addGameProp(GameProp(PropType.essenceContract, 10))
    xclb.currencyType = CurrencyType.eCoin
    xclb.price = 620
    gps.append(xclb)


def sorceryGemGiftPacks(gps: list[CostPerformanceHelper]):
    sglb = CostPerformanceHelper('1个魔蕴石')
    sglb.addGameProp(GameProp(PropType.sorceryGem, 1))
    sglb.currencyType = CurrencyType.eCoin
    sglb.price = 74
    gps.append(sglb)

    sglb2 = CostPerformanceHelper('5个魔蕴石')
    sglb2.addGameProp(GameProp(PropType.sorceryGem, 5))
    sglb2.currencyType = CurrencyType.eCoin
    sglb2.price = 369
    gps.append(sglb2)

    sglb3 = CostPerformanceHelper('9个魔蕴石')
    sglb3.addGameProp(GameProp(PropType.sorceryGem, 9))
    sglb3.currencyType = CurrencyType.eCoin
    sglb3.price = 660
    gps.append(sglb3)

    sglb4 = CostPerformanceHelper('20个魔蕴石')
    sglb4.addGameProp(GameProp(PropType.sorceryGem, 20))
    sglb4.currencyType = CurrencyType.eCoin
    sglb4.price = 1465
    gps.append(sglb4)

    sglb5 = CostPerformanceHelper('50个魔蕴石')
    sglb5.addGameProp(GameProp(PropType.sorceryGem, 50))
    sglb5.currencyType = CurrencyType.eCoin
    sglb5.price = 3659
    gps.append(sglb5)

    sglb6 = CostPerformanceHelper('100个魔蕴石')
    sglb6.addGameProp(GameProp(PropType.sorceryGem, 100))
    sglb6.currencyType = CurrencyType.eCoin
    sglb6.price = 7298
    gps.append(sglb6)

    sglb_sp = CostPerformanceHelper('1个魔蕴石（首次）')
    sglb_sp.addGameProp(GameProp(PropType.sorceryGem, 1))
    sglb_sp.addGameProp(GameProp(PropType.spiritGem, 200))
    sglb_sp.currencyType = CurrencyType.eCoin
    sglb_sp.price = 74
    gps.append(sglb_sp)

    sglb2_sp = CostPerformanceHelper('5个魔蕴石（首次）')
    sglb2_sp.addGameProp(GameProp(PropType.sorceryGem, 5))
    sglb2_sp.addGameProp(GameProp(PropType.spiritGem, 1000))
    sglb2_sp.currencyType = CurrencyType.eCoin
    sglb2_sp.price = 369
    gps.append(sglb2_sp)

    sglb3_sp = CostPerformanceHelper('9个魔蕴石（首次）')
    sglb3_sp.addGameProp(GameProp(PropType.sorceryGem, 9))
    sglb3_sp.addGameProp(GameProp(PropType.spiritGem, 1800))
    sglb3_sp.currencyType = CurrencyType.eCoin
    sglb3_sp.price = 660
    gps.append(sglb3_sp)

    sglb4_sp = CostPerformanceHelper('20个魔蕴石（首次）')
    sglb4_sp.addGameProp(GameProp(PropType.sorceryGem, 20))
    sglb4_sp.addGameProp(GameProp(PropType.spiritGem, 4000))
    sglb4_sp.currencyType = CurrencyType.eCoin
    sglb4_sp.price = 1465
    gps.append(sglb4_sp)

    sglb5_sp = CostPerformanceHelper('50个魔蕴石（首次）')
    sglb5_sp.addGameProp(GameProp(PropType.sorceryGem, 50))
    sglb5_sp.addGameProp(GameProp(PropType.spiritGem, 10000))
    sglb5_sp.currencyType = CurrencyType.eCoin
    sglb5_sp.price = 3659
    gps.append(sglb5_sp)

    sglb6_sp = CostPerformanceHelper('100个魔蕴石（首次）')
    sglb6_sp.addGameProp(GameProp(PropType.sorceryGem, 100))
    sglb6_sp.addGameProp(GameProp(PropType.spiritGem, 20000))
    sglb6_sp.currencyType = CurrencyType.eCoin
    sglb6_sp.price = 7298
    gps.append(sglb6_sp)


def initGiftPacks():
    gps: list[CostPerformanceHelper] = []
    shopGiftPacks(gps)
    chapterGiftPacks(gps)
    activityGiftPacks(gps)
    return gps


def exportGiftPacks(ws, title, gps: list[CostPerformanceHelper], needSort=False):
    ws.merge_cells(None, 1, 1, 1, 7)
    ws.cell(1, 1, title)
    row = 2
    ws.cell(row, 1, '礼包')
    ws.cell(row, 2, '物品')
    ws.cell(row, 3, '个数')
    ws.cell(row, 4, '物品等价晶灵石')
    ws.cell(row, 5, '价格（ECoin）')
    ws.cell(row, 6, '基础性价比')
    ws.cell(row, 7, '最优性价比')

    for giftPack in gps:
        giftPack.calCostPerformance()

    if needSort:
        gps.sort(key=lambda x: x.bestCP, reverse=True)

    row += 1
    for giftPack in gps:
        gprow = row
        for prop in giftPack.gamePropList:
            ws.cell(row, 2, prop.propType.typeName)
            ws.cell(row, 3, prop.number)
            result = ''
            if prop in giftPack.basicCPMap:
                result = str(giftPack.basicCPMap[prop].number)
            if prop in giftPack.bestCPMap and prop.propType == PropType.sorceryGem:
                result += '（' + str(giftPack.bestCPMap[prop].number) + '）'
            ws.cell(row, 4, result)
            row += 1
        ws.merge_cells(None, gprow, 1, row - 1, 1)
        ws.cell(gprow, 1, giftPack.giftPackName)

        ws.merge_cells(None, gprow, 5, row - 1, 5)
        ws.cell(gprow, 5, giftPack.price)

        ws.merge_cells(None, gprow, 6, row - 1, 6)
        ws.cell(gprow, 6, str(giftPack.basicCP))
        ws.merge_cells(None, gprow, 7, row - 1, 7)
        result = str(giftPack.bestCP)
        if giftPack.bestCP != giftPack.bestCP2:
            result += '（' + str(giftPack.bestCP2) + '）'
        ws.cell(gprow, 7, result)


def exportAllGiftPacks(filePath):
    wb = Workbook()
    ws = wb.active
    ws.title = '礼包物品性价比计算'
    ws.merge_cells(None, 1, 1, 1, 2)
    ws.merge_cells(None, 2, 1, 2, 2)
    ws.merge_cells(None, 3, 1, 3, 2)
    ws.merge_cells(None, 4, 1, 4, 2)
    ws.merge_cells(None, 5, 1, 5, 2)
    ws.merge_cells(None, 6, 1, 6, 2)
    ws.cell(1, 1, '游戏内各礼包性价比计算')
    ws.cell(2, 1, '所有物品均转为晶灵石后计算（详细请见以下物品转换）')
    ws.cell(3, 1, '部分物品无法直接购买难以定价，例如角色碎片，这些为0晶灵石')
    ws.cell(4, 1, '性价比=礼包物品总价值晶灵石/ecoin')
    ws.cell(5, 1, '基础性价比只考虑抽卡（晶灵石/魔蕴石/魔力契约），其他算为0收益')
    ws.cell(6, 1, '最优性价比考虑所有物品的收益，括号内是魔蕴石转换600晶灵石时的性价比')

    row = 7
    ws.merge_cells(None, row, 1, row, 2)
    ws.cell(row, 1, '物品转换')
    row += 1
    for pt in PropTypes():
        ws.cell(row, 1, pt.typeName)
        ws.cell(row, 2, pt.des)
        row += 1

    ws2 = wb.create_sheet('商店礼包')
    gps: list[CostPerformanceHelper] = []
    shopGiftPacks(gps)
    exportGiftPacks(ws2, '商店礼包', gps)

    ws3 = wb.create_sheet('主线礼包')
    gps: list[CostPerformanceHelper] = []
    chapterGiftPacks(gps)
    exportGiftPacks(ws3, '主线礼包', gps)

    ws4 = wb.create_sheet('活动礼包')
    gps: list[CostPerformanceHelper] = []
    activityGiftPacks(gps)
    exportGiftPacks(ws4, '活动礼包', gps)

    ws5 = wb.create_sheet('魔蕴石购入')
    gps: list[CostPerformanceHelper] = []
    sorceryGemGiftPacks(gps)
    exportGiftPacks(ws5, '魔蕴石购入', gps)

    wb.save(filePath)
    wb.close()


if __name__ == '__main__':
    exportAllGiftPacks('E:\\新世界\\性价比\\性价比计算.xls')
