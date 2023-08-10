from RoleCards.cards.aster.n_aster import NAster
from RoleCards.cards.aster.r_aster import RAster
from RoleCards.cards.aster.scarletFinesse import ScarletFinesse
from RoleCards.cards.aster.sr_aster import SRAster
from RoleCards.cards.blade.crystalAwakening import CrystalAwakening
from RoleCards.cards.blade.lovableEnforcer import LovableEnforcer
from RoleCards.cards.blade.n_Blade import NBlade
from RoleCards.cards.blade.r_Blade import RBlade
from RoleCards.cards.blade.sr_Blade import SRBlade
from RoleCards.cards.blade.explosiveRecall import ExplosiveRecall
from RoleCards.cards.blade.idolApprentice import IdolApprentice
from RoleCards.cards.dante.blazingColiseum import BlazingColiseum
from RoleCards.cards.dante.eternalHanabi import EternalHanabi
from RoleCards.cards.dante.icyEquilibrium import IcyEquilibrium
from RoleCards.cards.dante.n_Dante import NDante
from RoleCards.cards.dante.r_Dante import RDante
from RoleCards.cards.dante.scorchingSun import ScorchingSun
from RoleCards.cards.dante.sr_Dante import SRDante
from RoleCards.cards.edmond.eliteInstructor import EliteInstructor
from RoleCards.cards.edmond.flamingSecret import FlamingSecret
from RoleCards.cards.edmond.knightlyNight import KnightlyNight
from RoleCards.cards.edmond.n_Edmond import NEdmond
from RoleCards.cards.edmond.r_Edmond import REdmond
from RoleCards.cards.edmond.springChaos import SpringChaos
from RoleCards.cards.edmond.sweetAroma import SweetAroma
from RoleCards.cards.edmond.sr_Edmond import SREdmond
from RoleCards.cards.edmond.whiteLover import WhiteLover
from RoleCards.cards.eiden.galacticMist import GalacticMist
from RoleCards.cards.garu.endlessBanquet import EndlessBanquet
from RoleCards.cards.garu.forgottenFruit import ForgottenFruit
from RoleCards.cards.garu.howlingCyclone import HowlingCyclone
from RoleCards.cards.garu.mastersGift import MastersGift
from RoleCards.cards.garu.n_Garu import NGaru
from RoleCards.cards.garu.r_Garu import RGaru
from RoleCards.cards.garu.sr_Garu import SRGaru
from RoleCards.cards.kuya.afternoonDaze import AfternoonDaze
from RoleCards.cards.kuya.aromaticExotica import AromaticExotica
from RoleCards.cards.kuya.fallenLeaves import FallenLeaves
from RoleCards.cards.kuya.n_Kuya import NKuya
from RoleCards.cards.kuya.r_Kuya import RKuya
from RoleCards.cards.kuya.sr_Kuya import SRKuya
from RoleCards.cards.kuya.kitsuneDream import KitsuneDream
from RoleCards.cards.kuya.lakesideSpark import LakesideSpark
from RoleCards.cards.morvay.mauveMayhem import MauveMayhem
from RoleCards.cards.morvay.n_morvay import NMorvay
from RoleCards.cards.morvay.r_morvay import RMorvay
from RoleCards.cards.morvay.sr_morvay import SRMorvay
from RoleCards.cards.olivine.FrostedVirtue import FrostedVirtue
from RoleCards.cards.olivine.aquaBloom import AquaBloom
from RoleCards.cards.olivine.captiveStar import CaptiveStar
from RoleCards.cards.olivine.holyConfession import HolyConfession
from RoleCards.cards.olivine.n_Olivine import NOlivine
from RoleCards.cards.olivine.r_Olivine import ROlivine
from RoleCards.cards.olivine.sr_Olivine import SROlivine
from RoleCards.cards.olivine.radiantAdmiral import RadiantAdmiral
from RoleCards.cards.quincy.ancientCeremony import AncientCeremony
from RoleCards.cards.quincy.arcticWarden import ArcticWarden
from RoleCards.cards.quincy.blossomingLegend import BlossomingLegend
from RoleCards.cards.quincy.buckeyeMiracle import BuckeyeMiracle
from RoleCards.cards.quincy.distantPromise import DistantPromise
from RoleCards.cards.quincy.n_Quincy import NQuincy
from RoleCards.cards.quincy.r_Quincy import RQuincy
from RoleCards.cards.quincy.smokedTimber import SmokedTimber
from RoleCards.cards.quincy.sr_Quincy import SRQuincy
from RoleCards.cards.rei.midnightOwl import MidnightOwl
from RoleCards.cards.rei.n_Rei import NRei
from RoleCards.cards.rei.r_Rei import RRei
from RoleCards.cards.rei.rainyRebirth import RainyRebirth
from RoleCards.cards.rei.sr_Rei import SRRei
from RoleCards.cards.yakumo.cocoaLiqueur import CocoaLiqueur
from RoleCards.cards.yakumo.crimsonPhantom import CrimsonPhantom
from RoleCards.cards.yakumo.darkNova import DarkNova
from RoleCards.cards.yakumo.homecoming import Homecoming
from RoleCards.cards.yakumo.n_Yakumo import NYakumo
from RoleCards.cards.yakumo.oceanBreeze import OceanBreeze
from RoleCards.cards.yakumo.r_Yakumo import RYakumo
from RoleCards.cards.yakumo.sr_Yakumo import SRYakumo
from RoleCards.common.card import ICard
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom.minidom import Document


class CardHelper:
    def __init__(self):
        self.cardList: list[ICard] = []
        self.initCardList()

    def initCardList(self):
        # 艾斯特
        srA = SRAster()
        rA = RAster()
        nA = NAster()
        ssrA = ScarletFinesse()
        self.cardList.append(srA)
        self.cardList.append(rA)
        self.cardList.append(nA)
        self.cardList.append(ssrA)

        # 墨菲
        srM = SRMorvay()
        rM = RMorvay()
        nM = NMorvay()
        ssrM = MauveMayhem()
        self.cardList.append(srM)
        self.cardList.append(rM)
        self.cardList.append(nM)
        self.cardList.append(ssrM)

        # 八云
        srB = SRYakumo()
        rB = RYakumo()
        nB = NYakumo()
        ssrB = Homecoming()
        bqB = CocoaLiqueur()
        xB = OceanBreeze()
        dB = CrimsonPhantom()
        zaoBa = DarkNova()
        self.cardList.append(srB)
        self.cardList.append(rB)
        self.cardList.append(nB)
        self.cardList.append(ssrB)
        self.cardList.append(bqB)
        self.cardList.append(xB)
        self.cardList.append(dB)
        self.cardList.append(zaoBa)

        # 艾德蒙特
        srFT = SREdmond()
        rFT = REdmond()
        nFT = NEdmond()
        ssrFT = KnightlyNight()
        bqFT = WhiteLover()
        hhFT = SweetAroma()
        anFT = EliteInstructor()
        huaFT = SpringChaos()
        xiaFT = FlamingSecret()
        self.cardList.append(srFT)
        self.cardList.append(rFT)
        self.cardList.append(nFT)
        self.cardList.append(ssrFT)
        self.cardList.append(bqFT)
        self.cardList.append(hhFT)
        self.cardList.append(anFT)
        self.cardList.append(huaFT)
        self.cardList.append(xiaFT)

        # 奥利文
        srO = SROlivine()
        rO = ROlivine()
        nO = NOlivine()
        ssrO = HolyConfession()
        hO = AquaBloom()
        xO = RadiantAdmiral()
        dO = FrostedVirtue()
        miAo = CaptiveStar()
        self.cardList.append(srO)
        self.cardList.append(rO)
        self.cardList.append(nO)
        self.cardList.append(ssrO)
        self.cardList.append(hO)
        self.cardList.append(xO)
        self.cardList.append(dO)
        self.cardList.append(miAo)

        # 昆西
        srKX = SRQuincy()
        rKX = RQuincy()
        nKX = NQuincy()
        ssrKx = AncientCeremony()
        dKX = BuckeyeMiracle()
        yKX = DistantPromise()
        dongKX = ArcticWarden()
        srShuiKX = SmokedTimber()
        sanKX = BlossomingLegend()
        self.cardList.append(srKX)
        self.cardList.append(rKX)
        self.cardList.append(nKX)
        self.cardList.append(ssrKx)
        self.cardList.append(dKX)
        self.cardList.append(yKX)
        self.cardList.append(dongKX)
        self.cardList.append(srShuiKX)
        self.cardList.append(sanKX)

        # 玖夜
        srHL = SRKuya()
        rHL = RKuya()
        nHL = NKuya()
        ssrHL = FallenLeaves()
        hHL = KitsuneDream()
        naiHL = LakesideSpark()
        shuiHL = AfternoonDaze()
        xiaHL = AromaticExotica()
        self.cardList.append(srHL)
        self.cardList.append(rHL)
        self.cardList.append(nHL)
        self.cardList.append(ssrHL)
        self.cardList.append(hHL)
        self.cardList.append(naiHL)
        self.cardList.append(shuiHL)
        self.cardList.append(xiaHL)

        # 可尔
        srL = SRGaru()
        rL = RGaru()
        nL = NGaru()
        ssrL = MastersGift()
        gL = EndlessBanquet()
        guaL = HowlingCyclone()
        dunL = ForgottenFruit()
        self.cardList.append(srL)
        self.cardList.append(rL)
        self.cardList.append(nL)
        self.cardList.append(ssrL)
        self.cardList.append(gL)
        self.cardList.append(guaL)
        self.cardList.append(dunL)

        # 布儡
        srBL = SRBlade()
        rBL = RBlade()
        nBL = NBlade()
        ssrBL = ExplosiveRecall()
        xBL = IdolApprentice()
        npBL = LovableEnforcer()
        junBl = CrystalAwakening()
        self.cardList.append(srBL)
        self.cardList.append(rBL)
        self.cardList.append(nBL)
        self.cardList.append(ssrBL)
        self.cardList.append(xBL)
        self.cardList.append(npBL)
        self.cardList.append(junBl)

        # 啖天
        srDT = SRDante()
        rDT = RDante()
        nDT = NDante()
        ssrDT = BlazingColiseum()
        hhDT = EternalHanabi()
        shengDT = IcyEquilibrium()
        xiaDT = ScorchingSun()
        self.cardList.append(srDT)
        self.cardList.append(rDT)
        self.cardList.append(nDT)
        self.cardList.append(ssrDT)
        self.cardList.append(hhDT)
        self.cardList.append(shengDT)
        self.cardList.append(xiaDT)

        # 敛
        srLian = SRRei()
        rLian = RRei()
        nLian = NRei()
        ssrLian = MidnightOwl()
        sanLian = RainyRebirth()
        self.cardList.append(srLian)
        self.cardList.append(rLian)
        self.cardList.append(nLian)
        self.cardList.append(ssrLian)
        self.cardList.append(sanLian)

        # 伊得
        hYD = GalacticMist()
        self.cardList.append(hYD)

        self.cardList.sort(key=lambda x: (x.rarity, x.round, x.role))

    def filterCard(self, _cardId):
        return [x for x in self.cardList if x.cardId == _cardId]

    def loadCardList(self, filepath: str):
        try:
            doc = xml.dom.minidom.parse(filepath)
            if doc is None:
                return False
            root = doc.documentElement
            if root is None:
                return False

            xmlCards = root.getElementsByTagName('card')
            if xmlCards is None:
                return False

            for xmlCard in xmlCards:
                xmlCardId = ''
                if xmlCard.hasAttribute('id'):
                    xmlCardId = xmlCard.getAttribute('id')

                if len(xmlCardId) == 0:
                    continue
                roles = self.filterCard(xmlCardId)
                if roles is None or len(roles) <= 0:
                    continue
                try:
                    hp = xmlCard.getElementsByTagName('hp')[0]
                    hp_text = hp.childNodes[0].data
                    hp_int = int(hp_text)
                    roles[0].setHpDirect(hp_int)
                except:
                    print('转xml出错')

                try:
                    atk = xmlCard.getElementsByTagName('atk')[0]
                    atk_text = atk.childNodes[0].data
                    atk_int = int(atk_text)
                    roles[0].setAtkDirect(atk_int)
                except:
                    print('转xml出错')

                try:
                    lv = xmlCard.getElementsByTagName('lv')[0]
                    lv_text = lv.childNodes[0].data
                    lv_int = int(lv_text)
                    roles[0].setLv(lv_int)
                except:
                    print('转xml出错')

                try:
                    star = xmlCard.getElementsByTagName('star')[0]
                    star_text = star.childNodes[0].data
                    star_int = int(star_text)
                    roles[0].setStar(star_int)
                except:
                    print('转xml出错')

                try:
                    tier = xmlCard.getElementsByTagName('tier')[0]
                    tier_text = tier.childNodes[0].data
                    tier_int = int(tier_text)
                    roles[0].setTier(tier_int)
                except:
                    print('转xml出错')

                try:
                    bond = xmlCard.getElementsByTagName('bond')[0]
                    bond_text = bond.childNodes[0].data
                    bond_int = int(bond_text)
                    roles[0].setBond(bond_int)
                except:
                    print('转xml出错')

                try:
                    uve = xmlCard.getElementsByTagName('uve')[0]
                    uve_text = uve.childNodes[0].data
                    if uve_text == 'True':
                        roles[0].useExpectedValue = True
                    else:
                        roles[0].useExpectedValue = False
                except:
                    print('转bool出错')
        except:
            print('转xml出错')

    def exportCardList(self, filepath: str):
        doc = Document()  # 创建DOM文档对象
        root = doc.createElement('CardList')  # 创建根元素
        doc.appendChild(root)
        for role in self.cardList:
            card = doc.createElement('card')
            root.appendChild(card)
            card.setAttribute('id', role.cardId)

            hp = doc.createElement('hp')
            hp_text = doc.createTextNode(str(role.hp))
            hp.appendChild(hp_text)
            card.appendChild(hp)

            atk = doc.createElement('atk')
            atk_text = doc.createTextNode(str(role.atk))
            atk.appendChild(atk_text)
            card.appendChild(atk)

            lv = doc.createElement('lv')
            lv_text = doc.createTextNode(str(role.lv))
            lv.appendChild(lv_text)
            card.appendChild(lv)

            star = doc.createElement('star')
            star_text = doc.createTextNode(str(role.star))
            star.appendChild(star_text)
            card.appendChild(star)

            tier = doc.createElement('tier')
            tier_text = doc.createTextNode(str(role.tier))
            tier.appendChild(tier_text)
            card.appendChild(tier)

            bond = doc.createElement('bond')
            bond_text = doc.createTextNode(str(role.bond))
            bond.appendChild(bond_text)
            card.appendChild(bond)

            uve = doc.createElement('uve')
            uve_text = doc.createTextNode(str(role.useExpectedValue))
            uve.appendChild(uve_text)
            card.appendChild(uve)

        file = open(filepath, 'w')
        doc.writexml(file, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        file.close()
