from RoleCards.cards.aster.familiar_aster import FamiliarAster
from RoleCards.cards.blade.eDroid import EDroid
from RoleCards.cards.blade.explosiveRecall import ExplosiveRecall
from RoleCards.cards.blade.idolApprentice import IdolApprentice
from RoleCards.cards.dante.blazingColiseum import BlazingColiseum
from RoleCards.cards.dante.eternalHanabi import EternalHanabi
from RoleCards.cards.dante.sunLord import SunLord
from RoleCards.cards.edmond.knightlyNight import KnightlyNight
from RoleCards.cards.edmond.sweetAroma import SweetAroma
from RoleCards.cards.edmond.viceCaptain import ViceCaptain
from RoleCards.cards.edmond.whiteLover import WhiteLover
from RoleCards.cards.garu.endlessBanquet import EndlessBanquet
from RoleCards.cards.garu.howlingCyclone import HowlingCyclone
from RoleCards.cards.garu.mastersGift import MastersGift
from RoleCards.cards.garu.wildWolf import WildWolf
from RoleCards.cards.kuya.fallenLeaves import FallenLeaves
from RoleCards.cards.kuya.foxyRogue import FoxyRogue
from RoleCards.cards.kuya.kitsuneDream import KitsuneDream
from RoleCards.cards.kuya.lakesideSpark import LakesideSpark
from RoleCards.cards.morvay.familiar_morvay import FamiliarMorvay
from RoleCards.cards.olivine.aquaBloom import AquaBloom
from RoleCards.cards.olivine.holyConfession import HolyConfession
from RoleCards.cards.olivine.manOfGod import ManOfGod
from RoleCards.cards.olivine.radiantAdmiral import RadiantAdmiral
from RoleCards.cards.quincy.ancientCeremony import AncientCeremony
from RoleCards.cards.quincy.buckeyeMiracle import BuckeyeMiracle
from RoleCards.cards.quincy.distantPromise import DistantPromise
from RoleCards.cards.quincy.forestGuardian import ForestGuardian
from RoleCards.cards.yakumo.cocoaLiqueur import CocoaLiqueur
from RoleCards.cards.yakumo.crimsonPhantom import CrimsonPhantom
from RoleCards.cards.yakumo.homecoming import Homecoming
from RoleCards.cards.yakumo.oceanBreeze import OceanBreeze
from RoleCards.cards.yakumo.shadowSerpent import ShadowSerpent
from RoleCards.common.card import ICard




class CardHelper:
    def __init__(self):
        self.initCardList()

    def initCardList(self):
        self.cardList: list[ICard] = []

        # 艾斯特
        srA = FamiliarAster()
        self.cardList.append(srA)

        # 墨菲
        srM = FamiliarMorvay()
        self.cardList.append(srM)

        # 八云
        srB = ShadowSerpent()
        self.cardList.append(srB)
        ssrB = Homecoming()
        self.cardList.append(ssrB)
        bqB = CocoaLiqueur()
        self.cardList.append(bqB)
        xB = OceanBreeze()
        self.cardList.append(xB)
        dB = CrimsonPhantom()
        self.cardList.append(dB)

        # 艾德蒙特
        srFT = ViceCaptain()
        self.cardList.append(srFT)
        ssrFT = KnightlyNight()
        self.cardList.append(ssrFT)
        bqFT = WhiteLover()
        self.cardList.append(bqFT)
        hhFT = SweetAroma()
        self.cardList.append(hhFT)

        # 奥利文
        srO = ManOfGod()
        self.cardList.append(srO)
        ssrO = HolyConfession()
        self.cardList.append(ssrO)
        hO = AquaBloom()
        self.cardList.append(hO)
        xO = RadiantAdmiral()
        self.cardList.append(xO)

        # 昆西
        srKX = ForestGuardian()
        self.cardList.append(srKX)
        ssrKx = AncientCeremony()
        self.cardList.append(ssrKx)
        dKX = BuckeyeMiracle()
        self.cardList.append(dKX)
        yKX = DistantPromise()
        self.cardList.append(yKX)

        # 玖夜
        srHL = FoxyRogue()
        self.cardList.append(srHL)
        ssrHL = FallenLeaves()
        self.cardList.append(ssrHL)
        hHL = KitsuneDream()
        self.cardList.append(hHL)
        nHL = LakesideSpark()
        self.cardList.append(nHL)

        # 可尔
        srL = WildWolf()
        self.cardList.append(srL)
        ssrL = MastersGift()
        self.cardList.append(ssrL)
        gL = EndlessBanquet()
        self.cardList.append(gL)
        guaL = HowlingCyclone()
        self.cardList.append(guaL)

        # 布儡
        srBL = EDroid()
        self.cardList.append(srBL)
        ssrBL = ExplosiveRecall()
        self.cardList.append(ssrBL)
        xBL = IdolApprentice()
        self.cardList.append(xBL)

        # 啖天
        srDT = SunLord()
        self.cardList.append(srDT)
        ssrDT = BlazingColiseum()
        self.cardList.append(ssrDT)
        hhDT = EternalHanabi()
        self.cardList.append(hhDT)

    def filterCard(self, _cardName):
        return [x for x in self.cardList if x.cardName == _cardName]
