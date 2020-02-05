from math import sqrt, atan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt,Punkt_Dic
from datentyp.strecke import Strecke
from operation.transformation import Transformation


class AffinTrans(Transformation):
    def __init__(self, d_p0, d_p1, l_p1exclude=None):
        super().__init__(d_p0, d_p1, l_p1exclude=None)

        xX = yX = xy = xY = yY = yy = xx = 0
        for k in self._l_p_ident:
            xX += self._PDic0_reduced[k].get_x() * self._PDic1_reduced[k].get_x()
            yX += self._PDic0_reduced[k].get_y() * self._PDic1_reduced[k].get_x()
            xy += self._PDic0_reduced[k].get_x() * self._PDic0_reduced[k].get_y()
            xY += self._PDic0_reduced[k].get_x() * self._PDic1_reduced[k].get_y()
            yY += self._PDic0_reduced[k].get_y() * self._PDic1_reduced[k].get_y()
            yy += self._PDic0_reduced[k].get_y()**2
            xx += self._PDic0_reduced[k].get_x()**2
        N = xx * yy - xy**2

        a1 = (xX * yy - yX * xy) / N
        a2 = (xX * xy - yX * xx) / N
        a3 = (yY * xx - xY * xy) / N
        a4 = (xY * yy - yY * xy) / N

        m_X = sqrt(a1**2 + a4**2)
        m_Y = sqrt(a2**2 + a3**2)
        alpha = atan(a4/a1)
        beta = atan(a2/a3)

        Y0 = self._P1_cog.get_y() - a3 * self._P0_cog.get_y() - a4 * self._P0_cog.get_x()
        X0 = self._P1_cog.get_x() - a1 * self._P0_cog.get_x() + a2 * self._P0_cog.get_y()
        
        self._tParameter.update({"m_X": m_X})
        self._tParameter.update({"m_Y":m_Y})
        self._tParameter.update({"rot_X":alpha})
        self._tParameter.update({"rot_Y":beta})
        self._tParameter.update({"Y0":Y0})
        self._tParameter.update({"X0":X0})

        dicPTrans = {}
        for k,v in self._dicP0.items():
            y = v["coord"].get_y()
            x = v["coord"].get_x()
            pId = v["coord"].get_id()
            Y = Y0 + a3 * y + a4 * x
            X = X0 + a1 * x - a2 * y
            pTransformiert = {"coord":Punkt(Y,X,pId)}
            dicPTrans.update({pId:pTransformiert})            
            if k in self._l_p_ident:
                wy = - Y0 - a3*self._dicP0[k]["coord"].get_y() - a4*self._dicP0[k]["coord"].get_x() + self._dicP1[k]["coord"].get_y()
                wx = - X0 - a1*self._dicP0[k]["coord"].get_x() + a2*self._dicP0[k]["coord"].get_y() + self._dicP1[k]["coord"].get_x()
                w = {"y":Strecke.init_länge(wy), "x":Strecke.init_länge(wx)}
                dicPTrans[k].update({"w":w})
        
        self._dicP2.set_dic(dicPTrans)


    def get_result(self):
        return (self._dicP2, self._tParameter)

if __name__ == "__main__":
    dict_PLQuelle = Punkt_Dic()
    dict_PLZiel = Punkt_Dic()

#     str_pl0 = """101;-916.300;6078.720
# 102;3331.420;6492.430
# 103;6016.760;4370.940
# 104;4423.710;657.010
# 105;1618.100;2680.170
# 106;-1276.080;2735.320
# 2096;5091.510;2158.040
# 2097;3186.120;1252.510
# 2098;1110.210;2278.210
# 2099;3820.710;2787.190
# 3000;47.010;2999.400
# 3001;-797.190;1799.200"""

#     str_pl1 = """101;36935.000;26360.170
# 102;41132.120;27133.890
# 103;43988.310;25248.460
# 104;42717.270;21412.310
# 105;39749.540;23189.310
# 106;36861.190;22997.880"""
#    dict_PLQuelle.einlesenListe(str_pl0,".",";")
#    dict_PLZiel.einlesenListe(str_pl1,".",";")

    dict_PLQuelle.einlesenDatei("testdata/helmert_source.csv", sepDec=".", sepVal=";")
    dict_PLZiel.einlesenDatei("testdata/helmert_destination.csv", sepDec=".", sepVal=";")

    punkte,parameter = AffinTrans(dict_PLQuelle, dict_PLZiel).get_result()

    punkte = punkte.get_dic()
    for k,v in punkte.items():
        if "w" in v.keys():
            print(k,v["coord"], "RK:", v["w"]["y"].länge(), v["w"]["x"].länge())
        else:
            print(k,v["coord"])
    print(parameter)