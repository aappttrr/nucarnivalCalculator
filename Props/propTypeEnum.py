import enum

def PropTypes():
    pl = []
    pl.append(PropType.spiritGem)
    pl.append(PropType.sorceryGem)
    pl.append(PropType.essenceContract)
    pl.append(PropType.coin)
    pl.append(PropType.tinyBoost)
    pl.append(PropType.basicBoost)
    pl.append(PropType.strongBoost)
    pl.append(PropType.basicPotential)
    pl.append(PropType.intermediatePotential)
    pl.append(PropType.advancedPotential)
    pl.append(PropType.advancedUpPotential)
    pl.append(PropType.legendaryPotential)
    pl.append(PropType.smallEssenceVial)
    pl.append(PropType.middleEssenceVial)
    pl.append(PropType.bigEssenceVial)
    pl.append(PropType.expressPass)
    pl.append(PropType.key)
    pl.append(PropType.fancyKey)
    pl.append(PropType.basicGift)
    pl.append(PropType.intermediateGift)
    pl.append(PropType.advancedGift)
    pl.append(PropType.ultraGift)
    pl.append(PropType.holyWater_S)
    pl.append(PropType.holyWater_M)
    pl.append(PropType.holyWater_L)
    pl.append(PropType.holyWater_XL)
    pl.append(PropType.crystalCore)
    pl.append(PropType.rawCrystal)
    pl.append(PropType.crystalShards)
    pl.append(PropType.sr_Fragment)
    pl.append(PropType.sr_Role)
    pl.append(PropType.ssr_Fragment)
    pl.append(PropType.ssr_Role)
    pl.append(PropType.background)
    pl.append(PropType.voice)
    return pl


class PropType(enum.Enum):
    spiritGem = '晶灵石', '1晶灵石=1晶灵石'
    sorceryGem = '魔蕴石', '1红钻=600钻（特殊契约）=200钻（直接购买）'
    essenceContract = '魔力契约', '600钻'
    coin = '金币', '1金币=1/280钻（魔法师特权商店）'
    tinyBoost = '微型日月精华（10体力）', '1体力=5/3钻（直接购买）'
    basicBoost = '初级日月精华（30体力）', '1体力=5/3钻（直接购买）'
    strongBoost = '上级日月精华（100体力）', '1体力=5/3钻（直接购买）'
    basicPotential = '初级潜力道具', '1个初级潜力道具=1/6个中级潜力道具（合成）'
    intermediatePotential = '中级潜力道具', '1个中级潜力道具=40钻（魔法师特权商店）'
    advancedPotential = '高级潜力道具', '1个高级潜力道具=80钻（魔法师特权商店）'
    advancedUpPotential = '高级潜力道具（合成）', '1个高级合成潜力道具=600钻（魔法师特权商店）'
    legendaryPotential = '传说潜力道具', '传说潜力道具=2个高级合成+3个中级=1320钻（合成）'
    smallEssenceVial = '小瓶魔力熏香（1蜜话次数）', '1点蜜话点=20钻（直接购买）'
    middleEssenceVial = '中瓶魔力熏香（5蜜话次数）', '1点蜜话点=20钻（直接购买）'
    bigEssenceVial = '大瓶魔力熏香（10蜜话次数）', '1点蜜话点=20钻（直接购买）'
    expressPass = '快速通关券', '1通关券=60钻（直接购买，魔法师特权等级有折扣）'
    key = '钥匙', '1把钥匙=1600钻（神秘商人）'
    fancyKey = '高级钥匙', '1把高级钥匙=5把钥匙=8000钻（合成）'
    basicGift = '初级礼物', '1个初级礼物=0.5个中级礼物=10/6钻'
    intermediateGift = '中级礼物', '1个中级礼物=10/3钻（魔法师特权商店）'
    advancedGift = '高级礼物', '1个高级礼物=10钻（魔法师特权商店）'
    ultraGift = '回忆图画', '1个回忆图画=60钻（魔法师特权商店）'
    holyWater_S = '小型祝福药水', '小型祝福药水：晶灵石=5：4（来源攻略组）'
    holyWater_M = '中型祝福药水', '中型祝福药水：晶灵石=5：8（来源攻略组）'
    holyWater_L = '大型祝福药水', '大型祝福药水=2.5瓶中型祝福药水'
    holyWater_XL = '特大型祝福药水', '1个特大型祝福药水=1/25红钻=8钻（神秘商人）'
    crystalCore = '闪耀晶核', '1个闪耀晶核=60红钻=12000钻（神秘商人）'
    rawCrystal = '晶花原石', '1个晶花原石=45红钻=9000钻（神秘商人）'
    crystalShards = '晶花碎石', '商店无直接出售'
    sr_Fragment = 'SR碎片', '无法衡量'
    sr_Role = 'SR角色', '无法衡量'
    ssr_Fragment = 'SSR碎片', '无法衡量'
    ssr_Role = 'SSR角色', '无法衡量'
    background = '背景图', '无法衡量'
    voice = '限定语音', '无法衡量'

    def __init__(self, _value, des):
        self._typeName = _value
        self._des = des

    @property
    def typeName(self):
        return self._typeName

    @property
    def des(self):
        return self._des