from RoleCards.cards.aster.n_aster import NAster
from RoleCards.cards.aster.r_aster import RAster
from RoleCards.cards.aster.sr_aster import SRAster
from RoleCards.cards.blade.n_Blade import NBlade
from RoleCards.cards.blade.r_Blade import RBlade
from RoleCards.cards.blade.sr_Blade import SRBlade
from RoleCards.cards.blade.explosiveRecall import ExplosiveRecall
from RoleCards.cards.blade.idolApprentice import IdolApprentice
from RoleCards.cards.dante.blazingColiseum import BlazingColiseum
from RoleCards.cards.dante.eternalHanabi import EternalHanabi
from RoleCards.cards.dante.n_Dante import NDante
from RoleCards.cards.dante.r_Dante import RDante
from RoleCards.cards.dante.sr_Dante import SRDante
from RoleCards.cards.edmond.knightlyNight import KnightlyNight
from RoleCards.cards.edmond.n_Edmond import NEdmond
from RoleCards.cards.edmond.r_Edmond import REdmond
from RoleCards.cards.edmond.sweetAroma import SweetAroma
from RoleCards.cards.edmond.sr_Edmond import SREdmond
from RoleCards.cards.edmond.whiteLover import WhiteLover
from RoleCards.cards.garu.endlessBanquet import EndlessBanquet
from RoleCards.cards.garu.howlingCyclone import HowlingCyclone
from RoleCards.cards.garu.mastersGift import MastersGift
from RoleCards.cards.garu.n_Garu import NGaru
from RoleCards.cards.garu.r_Garu import RGaru
from RoleCards.cards.garu.sr_Garu import SRGaru
from RoleCards.cards.kuya.fallenLeaves import FallenLeaves
from RoleCards.cards.kuya.n_Kuya import NKuya
from RoleCards.cards.kuya.r_Kuya import RKuya
from RoleCards.cards.kuya.sr_Kuya import SRKuya
from RoleCards.cards.kuya.kitsuneDream import KitsuneDream
from RoleCards.cards.kuya.lakesideSpark import LakesideSpark
from RoleCards.cards.morvay.n_morvay import NMorvay
from RoleCards.cards.morvay.r_morvay import RMorvay
from RoleCards.cards.morvay.sr_morvay import SRMorvay
from RoleCards.cards.olivine.aquaBloom import AquaBloom
from RoleCards.cards.olivine.holyConfession import HolyConfession
from RoleCards.cards.olivine.n_Olivine import NOlivine
from RoleCards.cards.olivine.r_Olivine import ROlivine
from RoleCards.cards.olivine.sr_Olivine import SROlivine
from RoleCards.cards.olivine.radiantAdmiral import RadiantAdmiral
from RoleCards.cards.quincy.ancientCeremony import AncientCeremony
from RoleCards.cards.quincy.buckeyeMiracle import BuckeyeMiracle
from RoleCards.cards.quincy.distantPromise import DistantPromise
from RoleCards.cards.quincy.n_Quincy import NQuincy
from RoleCards.cards.quincy.r_Quincy import RQuincy
from RoleCards.cards.quincy.sr_Quincy import SRQuincy
from RoleCards.cards.yakumo.cocoaLiqueur import CocoaLiqueur
from RoleCards.cards.yakumo.crimsonPhantom import CrimsonPhantom
from RoleCards.cards.yakumo.homecoming import Homecoming
from RoleCards.cards.yakumo.n_Yakumo import NYakumo
from RoleCards.cards.yakumo.oceanBreeze import OceanBreeze
from RoleCards.cards.yakumo.r_Yakumo import RYakumo
from RoleCards.cards.yakumo.sr_Yakumo import SRYakumo
from RoleCards.common.card import ICard


class CardHelper:
    def __init__(self):
        self.cardList: list[ICard] = []
        self.initCardList()

    def initCardList(self):
        # 艾斯特
        srA = SRAster()
        self.cardList.append(srA)
        rA = RAster()
        self.cardList.append(rA)
        nA = NAster()
        self.cardList.append(nA)

        # 墨菲
        srM = SRMorvay()
        self.cardList.append(srM)
        rM = RMorvay()
        self.cardList.append(rM)
        nM = NMorvay()
        self.cardList.append(nM)

        # 八云
        srB = SRYakumo()
        self.cardList.append(srB)
        rB = RYakumo()
        self.cardList.append(rB)
        nB = NYakumo()
        self.cardList.append(nB)
        ssrB = Homecoming()
        self.cardList.append(ssrB)
        bqB = CocoaLiqueur()
        self.cardList.append(bqB)
        xB = OceanBreeze()
        self.cardList.append(xB)
        dB = CrimsonPhantom()
        self.cardList.append(dB)

        # 艾德蒙特
        srFT = SREdmond()
        self.cardList.append(srFT)
        rFT = REdmond()
        self.cardList.append(rFT)
        nFT = NEdmond()
        self.cardList.append(nFT)
        ssrFT = KnightlyNight()
        self.cardList.append(ssrFT)
        bqFT = WhiteLover()
        self.cardList.append(bqFT)
        hhFT = SweetAroma()
        self.cardList.append(hhFT)

        # 奥利文
        srO = SROlivine()
        self.cardList.append(srO)
        rO = ROlivine()
        self.cardList.append(rO)
        nO = NOlivine()
        self.cardList.append(nO)
        ssrO = HolyConfession()
        self.cardList.append(ssrO)
        hO = AquaBloom()
        self.cardList.append(hO)
        xO = RadiantAdmiral()
        self.cardList.append(xO)

        # 昆西
        srKX = SRQuincy()
        self.cardList.append(srKX)
        rKX = RQuincy()
        self.cardList.append(rKX)
        nKX = NQuincy()
        self.cardList.append(nKX)
        ssrKx = AncientCeremony()
        self.cardList.append(ssrKx)
        dKX = BuckeyeMiracle()
        self.cardList.append(dKX)
        yKX = DistantPromise()
        self.cardList.append(yKX)

        # 玖夜
        srHL = SRKuya()
        self.cardList.append(srHL)
        rHL = RKuya()
        self.cardList.append(rHL)
        nHL = NKuya()
        self.cardList.append(nHL)
        ssrHL = FallenLeaves()
        self.cardList.append(ssrHL)
        hHL = KitsuneDream()
        self.cardList.append(hHL)
        nHL = LakesideSpark()
        self.cardList.append(nHL)

        # 可尔
        srL = SRGaru()
        self.cardList.append(srL)
        rL = RGaru()
        self.cardList.append(rL)
        nL = NGaru()
        self.cardList.append(nL)
        ssrL = MastersGift()
        self.cardList.append(ssrL)
        gL = EndlessBanquet()
        self.cardList.append(gL)
        guaL = HowlingCyclone()
        self.cardList.append(guaL)

        # 布儡
        srBL = SRBlade()
        self.cardList.append(srBL)
        rBL = RBlade()
        self.cardList.append(rBL)
        nBL = NBlade()
        self.cardList.append(nBL)
        ssrBL = ExplosiveRecall()
        self.cardList.append(ssrBL)
        xBL = IdolApprentice()
        self.cardList.append(xBL)

        # 啖天
        srDT = SRDante()
        self.cardList.append(srDT)
        rDT = RDante()
        self.cardList.append(rDT)
        nDT = NDante()
        self.cardList.append(nDT)
        ssrDT = BlazingColiseum()
        self.cardList.append(ssrDT)
        hhDT = EternalHanabi()
        self.cardList.append(hhDT)

    def filterCard(self, _cardName):
        return [x for x in self.cardList if x.cardName == _cardName]
