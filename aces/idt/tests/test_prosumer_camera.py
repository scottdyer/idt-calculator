# !/usr/bin/env python
"""
Define the unit tests for the :mod:`aces.idt.prosumer_camera` module.
"""

import unittest
from pathlib import Path

import numpy as np
from colour.constants import TOLERANCE_ABSOLUTE_TESTS

from aces.idt import IDTGeneratorProsumerCamera

__author__ = "Colour Developers"
__copyright__ = "Copyright 2018 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "RESOURCES_DIRECTORY",
    "TestIDTGeneratorProsumerCamera",
]

RESOURCES_DIRECTORY = Path(__file__).parent / "resources"


class TestIDTGeneratorProsumerCamera(unittest.TestCase):
    """
    Define :class:`aces.idt.prosumer_camera.IDTGeneratorProsumerCamera`
    class unit tests methods.
    """

    def test_from_archive(self):
        """
        Define :func:`aces.idt.prosumer_camera.IDTGeneratorProsumerCamera.\
test_from_archive` definition unit tests methods.
        """

        idt_generator_1 = IDTGeneratorProsumerCamera.from_archive(
            RESOURCES_DIRECTORY / "synthetic_001.zip", cleanup=True
        )

        np.testing.assert_allclose(
            idt_generator_1.LUT_decoding.table,
            np.array(
                [
                    -0.01754712,
                    -0.01736907,
                    -0.01718998,
                    -0.01700999,
                    -0.01682921,
                    -0.01664774,
                    -0.01646567,
                    -0.01628310,
                    -0.01610008,
                    -0.01591669,
                    -0.01573298,
                    -0.01554900,
                    -0.01536478,
                    -0.01518037,
                    -0.01499580,
                    -0.01481110,
                    -0.01462628,
                    -0.01444136,
                    -0.01425637,
                    -0.01407132,
                    -0.01388621,
                    -0.01370106,
                    -0.01351588,
                    -0.01333066,
                    -0.01314543,
                    -0.01296017,
                    -0.01277491,
                    -0.01258963,
                    -0.01240434,
                    -0.01221904,
                    -0.01203374,
                    -0.01184843,
                    -0.01166312,
                    -0.01147781,
                    -0.01129250,
                    -0.01110719,
                    -0.01092188,
                    -0.01073657,
                    -0.01055125,
                    -0.01036594,
                    -0.01018063,
                    -0.00999532,
                    -0.00981001,
                    -0.00962470,
                    -0.00943938,
                    -0.00925407,
                    -0.00906876,
                    -0.00888345,
                    -0.00869814,
                    -0.00851283,
                    -0.00832751,
                    -0.00814220,
                    -0.00795689,
                    -0.00777158,
                    -0.00758627,
                    -0.00740096,
                    -0.00721565,
                    -0.00703033,
                    -0.00684502,
                    -0.00665971,
                    -0.00647440,
                    -0.00628909,
                    -0.00610378,
                    -0.00591846,
                    -0.00573315,
                    -0.00554784,
                    -0.00536253,
                    -0.00517722,
                    -0.00499191,
                    -0.00480660,
                    -0.00462128,
                    -0.00443597,
                    -0.00425066,
                    -0.00406535,
                    -0.00388004,
                    -0.00369473,
                    -0.00350942,
                    -0.00332411,
                    -0.00313880,
                    -0.00295349,
                    -0.00276818,
                    -0.00258288,
                    -0.00239758,
                    -0.00221228,
                    -0.00202699,
                    -0.00184170,
                    -0.00165642,
                    -0.00147114,
                    -0.00128588,
                    -0.00110062,
                    -0.00091538,
                    -0.00073016,
                    -0.00054496,
                    -0.00035978,
                    -0.00017462,
                    0.00001070,
                    0.00019775,
                    0.00038204,
                    0.00056628,
                    0.00075052,
                    0.00093537,
                    0.00112013,
                    0.00130481,
                    0.00148937,
                    0.00167380,
                    0.00185810,
                    0.00204223,
                    0.00222619,
                    0.00240994,
                    0.00259346,
                    0.00277674,
                    0.00295974,
                    0.00314243,
                    0.00332480,
                    0.00350681,
                    0.00368842,
                    0.00386962,
                    0.00405037,
                    0.00423065,
                    0.00441042,
                    0.00458967,
                    0.00476838,
                    0.00494651,
                    0.00512407,
                    0.00530104,
                    0.00547741,
                    0.00565320,
                    0.00582840,
                    0.00600303,
                    0.00617712,
                    0.00635070,
                    0.00652382,
                    0.00669651,
                    0.00686885,
                    0.00704089,
                    0.00721287,
                    0.00738610,
                    0.00755938,
                    0.00773281,
                    0.00790649,
                    0.00808054,
                    0.00825505,
                    0.00843014,
                    0.00860593,
                    0.00878252,
                    0.00896003,
                    0.00913858,
                    0.00931825,
                    0.00949916,
                    0.00968140,
                    0.00986505,
                    0.01005017,
                    0.01023684,
                    0.01042510,
                    0.01061499,
                    0.01080654,
                    0.01099975,
                    0.01119461,
                    0.01139111,
                    0.01158923,
                    0.01178890,
                    0.01199009,
                    0.01219271,
                    0.01239669,
                    0.01260196,
                    0.01280841,
                    0.01301596,
                    0.01322449,
                    0.01343393,
                    0.01364416,
                    0.01385510,
                    0.01406665,
                    0.01427876,
                    0.01449133,
                    0.01470434,
                    0.01491772,
                    0.01513147,
                    0.01534557,
                    0.01556004,
                    0.01577491,
                    0.01599025,
                    0.01620612,
                    0.01642262,
                    0.01663988,
                    0.01685803,
                    0.01707725,
                    0.01729770,
                    0.01751958,
                    0.01774312,
                    0.01796854,
                    0.01819609,
                    0.01842600,
                    0.01865855,
                    0.01889400,
                    0.01913260,
                    0.01937461,
                    0.01962030,
                    0.01986990,
                    0.02012363,
                    0.02038172,
                    0.02064437,
                    0.02091177,
                    0.02118406,
                    0.02146137,
                    0.02174380,
                    0.02203142,
                    0.02232426,
                    0.02262232,
                    0.02292556,
                    0.02323391,
                    0.02354728,
                    0.02386552,
                    0.02418846,
                    0.02451590,
                    0.02484761,
                    0.02518333,
                    0.02552277,
                    0.02586564,
                    0.02621160,
                    0.02656071,
                    0.02691411,
                    0.02726953,
                    0.02762657,
                    0.02798488,
                    0.02834409,
                    0.02870384,
                    0.02906381,
                    0.02942368,
                    0.02978316,
                    0.03014201,
                    0.03050001,
                    0.03085696,
                    0.03121274,
                    0.03156724,
                    0.03192041,
                    0.03227225,
                    0.03262281,
                    0.03297219,
                    0.03332055,
                    0.03366810,
                    0.03401507,
                    0.03436179,
                    0.03470861,
                    0.03505593,
                    0.03540420,
                    0.03575389,
                    0.03610553,
                    0.03645968,
                    0.03681696,
                    0.03718013,
                    0.03754759,
                    0.03791994,
                    0.03829776,
                    0.03868162,
                    0.03907209,
                    0.03946970,
                    0.03987495,
                    0.04028829,
                    0.04071014,
                    0.04114083,
                    0.04158066,
                    0.04202984,
                    0.04248850,
                    0.04295669,
                    0.04343437,
                    0.04392141,
                    0.04441762,
                    0.04492272,
                    0.04543632,
                    0.04595797,
                    0.04648711,
                    0.04702314,
                    0.04756534,
                    0.04811299,
                    0.04866529,
                    0.04922140,
                    0.04978046,
                    0.05034161,
                    0.05090397,
                    0.05146667,
                    0.05202889,
                    0.05259002,
                    0.05314980,
                    0.05370642,
                    0.05425921,
                    0.05480755,
                    0.05535149,
                    0.05589166,
                    0.05642704,
                    0.05695754,
                    0.05748317,
                    0.05800407,
                    0.05852051,
                    0.05903283,
                    0.05954153,
                    0.06004718,
                    0.06055044,
                    0.06105207,
                    0.06155291,
                    0.06205382,
                    0.06255573,
                    0.06305960,
                    0.06356640,
                    0.06407713,
                    0.06459275,
                    0.06511423,
                    0.06564251,
                    0.06617846,
                    0.06672292,
                    0.06727669,
                    0.06784047,
                    0.06841492,
                    0.06900064,
                    0.06959813,
                    0.07020785,
                    0.07083020,
                    0.07146551,
                    0.07211407,
                    0.07277612,
                    0.07345183,
                    0.07414138,
                    0.07484490,
                    0.07556250,
                    0.07629430,
                    0.07704037,
                    0.07780082,
                    0.07857576,
                    0.07936527,
                    0.08016947,
                    0.08098844,
                    0.08182228,
                    0.08267110,
                    0.08353499,
                    0.08441401,
                    0.08530818,
                    0.08621750,
                    0.08714192,
                    0.08808138,
                    0.08903574,
                    0.09000477,
                    0.09098818,
                    0.09198556,
                    0.09299645,
                    0.09402025,
                    0.09505630,
                    0.09610382,
                    0.09716198,
                    0.09822984,
                    0.09930640,
                    0.10039060,
                    0.10148133,
                    0.10257744,
                    0.10367779,
                    0.10478123,
                    0.10588665,
                    0.10699298,
                    0.10809921,
                    0.10920446,
                    0.11030792,
                    0.11140893,
                    0.11250695,
                    0.11360161,
                    0.11469268,
                    0.11578013,
                    0.11686407,
                    0.11794480,
                    0.11902279,
                    0.12009865,
                    0.12117318,
                    0.12224728,
                    0.12332199,
                    0.12439845,
                    0.12547787,
                    0.12656153,
                    0.12765074,
                    0.12874684,
                    0.12985118,
                    0.13096507,
                    0.13208981,
                    0.13322662,
                    0.13437668,
                    0.13554106,
                    0.13672078,
                    0.13791673,
                    0.13912975,
                    0.14036055,
                    0.14160979,
                    0.14287802,
                    0.14416575,
                    0.14547341,
                    0.14680138,
                    0.14815001,
                    0.14951962,
                    0.15091051,
                    0.15232296,
                    0.15375726,
                    0.15521370,
                    0.15669260,
                    0.15819431,
                    0.15971920,
                    0.16126764,
                    0.16284004,
                    0.16443681,
                    0.16605832,
                    0.16770497,
                    0.16937709,
                    0.17107500,
                    0.17279887,
                    0.17454884,
                    0.17632495,
                    0.17812713,
                    0.17995523,
                    0.18180890,
                    0.18368763,
                    0.18559074,
                    0.18751738,
                    0.18946652,
                    0.19143694,
                    0.19342730,
                    0.19543607,
                    0.19746162,
                    0.19950217,
                    0.20155587,
                    0.20362081,
                    0.20569503,
                    0.20777658,
                    0.20986355,
                    0.21195410,
                    0.21404649,
                    0.21613915,
                    0.21823066,
                    0.22031982,
                    0.22240566,
                    0.22448746,
                    0.22656478,
                    0.22863746,
                    0.23070563,
                    0.23276974,
                    0.23483050,
                    0.23688890,
                    0.23894620,
                    0.24100388,
                    0.24306363,
                    0.24512734,
                    0.24719700,
                    0.24927472,
                    0.25136267,
                    0.25346307,
                    0.25557809,
                    0.25770988,
                    0.25986046,
                    0.26203176,
                    0.26422555,
                    0.26644342,
                    0.26868677,
                    0.27095678,
                    0.27325442,
                    0.27558042,
                    0.27793530,
                    0.28031936,
                    0.28273269,
                    0.28517517,
                    0.28764653,
                    0.29014637,
                    0.29267413,
                    0.29522911,
                    0.29781055,
                    0.30041762,
                    0.30304949,
                    0.30570533,
                    0.30838432,
                    0.31108572,
                    0.31380882,
                    0.31655302,
                    0.31931779,
                    0.32210274,
                    0.32490758,
                    0.32773219,
                    0.33057654,
                    0.33344079,
                    0.33632522,
                    0.33923024,
                    0.34215636,
                    0.34510424,
                    0.34807468,
                    0.35106865,
                    0.35408720,
                    0.35713146,
                    0.36020265,
                    0.36330208,
                    0.36643111,
                    0.36959111,
                    0.37278354,
                    0.37600988,
                    0.37927163,
                    0.38257032,
                    0.38590747,
                    0.38928460,
                    0.39270323,
                    0.39616486,
                    0.39967094,
                    0.40322294,
                    0.40682226,
                    0.41047026,
                    0.41416824,
                    0.41791745,
                    0.42171908,
                    0.42557427,
                    0.42948406,
                    0.43344940,
                    0.43747117,
                    0.44155014,
                    0.44568696,
                    0.44988218,
                    0.45413621,
                    0.45844935,
                    0.46282173,
                    0.46725334,
                    0.47174401,
                    0.47629343,
                    0.48090112,
                    0.48556645,
                    0.49028862,
                    0.49506668,
                    0.49989951,
                    0.50478588,
                    0.50972439,
                    0.51471354,
                    0.51975172,
                    0.52483723,
                    0.52996831,
                    0.53514314,
                    0.54035987,
                    0.54561666,
                    0.55091168,
                    0.55624315,
                    0.56160938,
                    0.56700874,
                    0.57243971,
                    0.57790088,
                    0.58339097,
                    0.58890890,
                    0.59445379,
                    0.60002494,
                    0.60562186,
                    0.61124425,
                    0.61689205,
                    0.62256538,
                    0.62826457,
                    0.63399016,
                    0.63974291,
                    0.64552375,
                    0.65133381,
                    0.65717438,
                    0.66304693,
                    0.66895305,
                    0.67489448,
                    0.68087306,
                    0.68689073,
                    0.69294953,
                    0.69905152,
                    0.70519887,
                    0.71139376,
                    0.71763836,
                    0.72393486,
                    0.73028542,
                    0.73669216,
                    0.74315714,
                    0.74968239,
                    0.75626988,
                    0.76292152,
                    0.76963911,
                    0.77642440,
                    0.78327904,
                    0.79020461,
                    0.79720258,
                    0.80427436,
                    0.81142128,
                    0.81864459,
                    0.82594547,
                    0.83332505,
                    0.84078441,
                    0.84832458,
                    0.85594657,
                    0.86365136,
                    0.87143991,
                    0.87931318,
                    0.88727211,
                    0.89531769,
                    0.90345089,
                    0.91167272,
                    0.91998418,
                    0.92838633,
                    0.93688024,
                    0.94546699,
                    0.95414772,
                    0.96292355,
                    0.97179562,
                    0.98076507,
                    0.98983303,
                    0.99900059,
                    1.00826884,
                    1.01763879,
                    1.02711143,
                    1.03668764,
                    1.04636823,
                    1.05615393,
                    1.06604533,
                    1.07604291,
                    1.08614703,
                    1.09635792,
                    1.10667569,
                    1.11710027,
                    1.12763142,
                    1.13826876,
                    1.14901175,
                    1.15985979,
                    1.17081216,
                    1.18186803,
                    1.19302650,
                    1.20428662,
                    1.21564738,
                    1.22710773,
                    1.23866666,
                    1.25032316,
                    1.26207632,
                    1.27392529,
                    1.28586934,
                    1.29790789,
                    1.31004050,
                    1.32226692,
                    1.33458710,
                    1.34700118,
                    1.35950954,
                    1.37211278,
                    1.38481171,
                    1.39760740,
                    1.41050110,
                    1.42349433,
                    1.43658876,
                    1.44978627,
                    1.46308891,
                    1.47649887,
                    1.49001848,
                    1.50365017,
                    1.51739646,
                    1.53125992,
                    1.54524317,
                    1.55934885,
                    1.57357961,
                    1.58793806,
                    1.60242680,
                    1.61704836,
                    1.63180523,
                    1.64669984,
                    1.66173451,
                    1.67691153,
                    1.69223309,
                    1.70770128,
                    1.72331815,
                    1.73908565,
                    1.75500566,
                    1.77108002,
                    1.78731047,
                    1.80369873,
                    1.82024647,
                    1.83695531,
                    1.85382685,
                    1.87086264,
                    1.88806425,
                    1.90543320,
                    1.92297101,
                    1.94067921,
                    1.95855931,
                    1.97661283,
                    1.99484127,
                    2.01324616,
                    2.03182903,
                    2.05059140,
                    2.06953481,
                    2.08866081,
                    2.10797095,
                    2.12746676,
                    2.14714983,
                    2.16702172,
                    2.18708398,
                    2.20733821,
                    2.22778597,
                    2.24842886,
                    2.26926846,
                    2.29030634,
                    2.31154409,
                    2.33298333,
                    2.35462566,
                    2.37647270,
                    2.39852608,
                    2.42078745,
                    2.44325843,
                    2.46594065,
                    2.48883574,
                    2.51194537,
                    2.53527119,
                    2.55881487,
                    2.58257811,
                    2.60656261,
                    2.63077008,
                    2.65520226,
                    2.67986091,
                    2.70474781,
                    2.72986476,
                    2.75521358,
                    2.78079612,
                    2.80661426,
                    2.83266993,
                    2.85896506,
                    2.88550164,
                    2.91228169,
                    2.93930726,
                    2.96658046,
                    2.99410343,
                    3.02187834,
                    3.04990741,
                    3.07819293,
                    3.10673720,
                    3.13554258,
                    3.16461149,
                    3.19394637,
                    3.22354973,
                    3.25342411,
                    3.28357210,
                    3.31399633,
                    3.34469949,
                    3.37568429,
                    3.40695349,
                    3.43850989,
                    3.47035633,
                    3.50249567,
                    3.53493080,
                    3.56766468,
                    3.60070024,
                    3.63404047,
                    3.66768838,
                    3.70164699,
                    3.73591934,
                    3.77050848,
                    3.80541750,
                    3.84064947,
                    3.87620750,
                    3.91209467,
                    3.94831411,
                    3.98486893,
                    4.02176226,
                    4.05899722,
                    4.09657698,
                    4.13450466,
                    4.17278343,
                    4.21141646,
                    4.25040694,
                    4.28975805,
                    4.32947301,
                    4.36955506,
                    4.41000744,
                    4.45083344,
                    4.49203637,
                    4.53361954,
                    4.57558634,
                    4.61794016,
                    4.66068443,
                    4.70382264,
                    4.74735830,
                    4.79129498,
                    4.83563626,
                    4.88038582,
                    4.92554734,
                    4.97112457,
                    5.01712130,
                    5.06354138,
                    5.11038869,
                    5.15766717,
                    5.20538082,
                    5.25353366,
                    5.30212979,
                    5.35117333,
                    5.40066846,
                    5.45061942,
                    5.50103046,
                    5.55190590,
                    5.60325011,
                    5.65506748,
                    5.70736246,
                    5.76013955,
                    5.81340326,
                    5.86715817,
                    5.92140891,
                    5.97616011,
                    6.03141648,
                    6.08718275,
                    6.14346371,
                    6.20026416,
                    6.25758898,
                    6.31544307,
                    6.37383136,
                    6.43275886,
                    6.49223058,
                    6.55225161,
                    6.61282706,
                    6.67396209,
                    6.73566192,
                    6.79793179,
                    6.86077700,
                    6.92420290,
                    6.98821489,
                    7.05281840,
                    7.11801893,
                    7.18382200,
                    7.25023322,
                    7.31725821,
                    7.38490268,
                    7.45317235,
                    7.52207301,
                    7.59161052,
                    7.66179078,
                    7.73261972,
                    7.80410337,
                    7.87624777,
                    7.94905905,
                    8.02254337,
                    8.09670697,
                    8.17155613,
                    8.24709718,
                    8.32333654,
                    8.40028066,
                    8.47793605,
                    8.55630930,
                    8.63540705,
                    8.71523599,
                    8.79580289,
                    8.87711457,
                    8.95917791,
                    9.04199987,
                    9.12558746,
                    9.20994776,
                    9.29508792,
                    9.38101513,
                    9.46773669,
                    9.55525993,
                    9.64359226,
                    9.73274117,
                    9.82271421,
                    9.91351898,
                    10.00516319,
                    10.09765459,
                    10.19100101,
                    10.28521036,
                    10.38029062,
                    10.47624983,
                    10.57309613,
                    10.67083771,
                    10.76948284,
                    10.86903989,
                    10.96951728,
                    11.07092352,
                    11.17326720,
                    11.27655697,
                    11.38080160,
                    11.48600990,
                    11.59219079,
                    11.69935325,
                    11.80750636,
                    11.91665928,
                    12.02682125,
                    12.13800159,
                    12.25020973,
                    12.36345516,
                    12.47774747,
                    12.59309634,
                    12.70951154,
                    12.82700293,
                    12.94558045,
                    13.06525414,
                    13.18603414,
                    13.30793067,
                    13.43095406,
                    13.55511473,
                    13.68042318,
                    13.80689002,
                    13.93452598,
                    14.06334184,
                    14.19334853,
                    14.32455705,
                    14.45697851,
                    14.59062412,
                    14.72550519,
                    14.86163316,
                    14.99901955,
                    15.13767598,
                    15.27761421,
                    15.41884608,
                    15.56138354,
                    15.70523868,
                    15.85042366,
                    15.99695079,
                    16.14483247,
                    16.29408122,
                    16.44470968,
                    16.59673061,
                    16.75015687,
                    16.90500146,
                    17.06127749,
                    17.21899819,
                    17.37817693,
                    17.53882717,
                    17.70096251,
                    17.86459670,
                    18.02974358,
                    18.19641714,
                    18.36463149,
                    18.53440088,
                    18.70573968,
                    18.87866239,
                    19.05318367,
                    19.22931828,
                    19.40708115,
                    19.58648733,
                    19.76755200,
                    19.95029049,
                    20.13471829,
                    20.32085101,
                    20.50870441,
                    20.69829439,
                    20.88963701,
                    21.08274848,
                    21.27728180,
                    21.47356356,
                    21.67165601,
                    21.87157585,
                    22.07333995,
                    22.27696530,
                    22.48246909,
                    22.68986864,
                    22.89918144,
                    23.11042514,
                    23.32361755,
                    23.53877665,
                    23.75592058,
                    23.97506765,
                    24.19623634,
                    24.41944530,
                    24.64471335,
                    24.87205948,
                    25.10150287,
                    25.33306287,
                    25.56675899,
                    25.80261094,
                    26.04063862,
                    26.28086209,
                    26.52330161,
                    26.76797762,
                    27.01491075,
                    27.26412183,
                    27.51563186,
                    27.76946206,
                    28.02563384,
                    28.28416878,
                    28.54508869,
                    28.80841557,
                    29.07417164,
                    29.34237928,
                    29.61306113,
                    29.88624000,
                    30.16193893,
                    30.44018117,
                    30.72099018,
                    31.00438964,
                    31.29040344,
                    31.57905570,
                    31.87037077,
                    32.16437320,
                    32.46108779,
                    32.76053955,
                    33.06275374,
                    33.36775584,
                    33.67557156,
                    33.98622687,
                    34.29974796,
                    34.61616126,
                    34.93549346,
                    35.25777148,
                    35.58302250,
                    35.91127394,
                    36.24255348,
                    36.57688905,
                    36.91430383,
                    37.25481983,
                    37.59846255,
                    37.94525696,
                    38.29522730,
                    38.64839681,
                    39.00478752,
                    39.36441991,
                    39.72731252,
                    40.09348154,
                    40.46294025,
                    40.83569844,
                    41.21176171,
                    41.59113066,
                    41.97379999,
                    42.35975743,
                    42.74898261,
                    43.14144568,
                    43.53710591,
                    43.93591002,
                    44.33779042,
                    44.74266328,
                    45.15042638,
                    45.56095695,
                    45.97410920,
                    46.38971184,
                    46.80756546,
                    47.22743983,
                    47.64907116,
                    48.07215935,
                    48.49636525,
                    48.92130808,
                ]
            ),
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )

        np.testing.assert_allclose(
            idt_generator_1.M,
            np.array(
                [
                    [0.71091097, 0.20348528, 0.08560375],
                    [0.01379831, 1.02510569, -0.03890399],
                    [-0.10581334, -0.07130598, 1.17711932],
                ]
            ),
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )
        np.testing.assert_allclose(
            idt_generator_1.RGB_w,
            np.array([1.00246918, 1.00000000, 1.00537500]),
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )
        np.testing.assert_allclose(
            idt_generator_1.k,
            1.1831303512964655,
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )

        idt_generator_2 = IDTGeneratorProsumerCamera.from_archive(
            RESOURCES_DIRECTORY / "synthetic_002.zip", cleanup=True
        )

        np.testing.assert_allclose(
            idt_generator_1.M,
            idt_generator_2.M,
            atol=0.025,
        )

        np.testing.assert_allclose(
            idt_generator_1.RGB_w,
            idt_generator_2.RGB_w,
            atol=0.0005,
        )

        np.testing.assert_allclose(
            idt_generator_1.k,
            idt_generator_2.k,
            atol=0.25,
        )

        idt_generator_3 = IDTGeneratorProsumerCamera.from_archive(
            RESOURCES_DIRECTORY / "synthetic_003.zip", cleanup=True
        )

        np.testing.assert_allclose(
            idt_generator_3.M,
            np.array(
                [
                    [0.70683937, 0.19921694, 0.09394369],
                    [0.01383883, 1.01847757, -0.03231640],
                    [-0.11943804, -0.06335993, 1.18279798],
                ]
            ),
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )

        np.testing.assert_allclose(
            idt_generator_3.RGB_w,
            np.array([0.51079662, 1.00000000, 2.00262926]),
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )

        np.testing.assert_allclose(
            idt_generator_3.k,
            1.1842568704786522,
            atol=TOLERANCE_ABSOLUTE_TESTS,
        )


if __name__ == "__main__":
    unittest.main()
