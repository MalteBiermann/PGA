from math import sqrt, atan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt,Punkt_Dic
from datentyp.strecke import Strecke
from operation.transformation import Transformation


class HelmertTrans(Transformation):
    def __init__(self, d_p0, d_p1, l_p1exclude=None):
        super().__init__(d_p0, d_p1, l_p1exclude=None)

        nenner = 0
        o_zähler = 0
        a_zähler = 0
        for k in self._l_p_ident:
            o_zähler += self._PDic0_reduced[k].get_x() * self._PDic1_reduced[k].get_y() -\
                self._PDic0_reduced[k].get_y() * self._PDic1_reduced[k].get_x()
            nenner += self._PDic0_reduced[k].get_x()**2 + self._PDic0_reduced[k].get_y()**2
            a_zähler += self._PDic0_reduced[k].get_x() * self._PDic1_reduced[k].get_x() +\
                self._PDic0_reduced[k].get_y() * self._PDic1_reduced[k].get_y()

        a = a_zähler / nenner
        o = o_zähler / nenner
        maßstab = sqrt(a ** 2 + o ** 2)
        epsilon = atan(o / a)
        Y0 = self._P1_cog.get_y() - a * self._P0_cog.get_y() - o * self._P0_cog.get_x()
        X0 = self._P1_cog.get_x() - a * self._P0_cog.get_x() + o * self._P0_cog.get_y()
        
        self._tParameter.update({"m":maßstab})
        self._tParameter.update({"epsilon":epsilon})
        self._tParameter.update({"Y0":Y0})
        self._tParameter.update({"X0":X0})


        dicPTrans = {}
        for k,v in self._dicP0.items():
            y = v["coord"].get_y()
            x = v["coord"].get_x()
            id = v["coord"].get_id()
            Y = Y0 + a * y + o * x
            X = X0 + a * x - o * y
            pTransformiert = {"coord":Punkt(Y,X,id)}
            dicPTrans.update({id:pTransformiert})            
            if k in self._l_p_ident:
                wy = - Y0 - a*self._dicP0[k]["coord"].get_y() - o*self._dicP0[k]["coord"].get_x() + self._dicP1[k]["coord"].get_y()
                wx = - X0 - a*self._dicP0[k]["coord"].get_x() + o*self._dicP0[k]["coord"].get_y() + self._dicP1[k]["coord"].get_x()
                w = {"y":Strecke.init_länge(wy), "x":Strecke.init_länge(wx)}
                dicPTrans[k].update({"w":w})
        
        self._dicP2.set_dic(dicPTrans)


    def get_result(self):
        return (self._dicP2, self._tParameter)



if __name__ == "__main__":
    dict_PLQuelle = Punkt_Dic()
    dict_PLZiel = Punkt_Dic()

    str_pl0 = """101;-916.300;6078.720
102;3331.420;6492.430
103;6016.760;4370.940
104;4423.710;657.010
105;1618.100;2680.170
106;-1276.080;2735.320
2096;5091.510;2158.040
2097;3186.120;1252.510
2098;1110.210;2278.210
2099;3820.710;2787.190
3000;47.010;2999.400
3001;-797.190;1799.200"""

    str_pl1 = """101;36935.000;26360.170
102;41132.120;27133.890
103;43988.310;25248.460
104;42717.270;21412.310
105;39749.540;23189.310
106;36861.190;22997.880"""
#    dict_PLQuelle.einlesenListe(str_pl0,".",";")
#    dict_PLZiel.einlesenListe(str_pl1,".",";")

    dict_PLQuelle.einlesenDatei("testdata/helmert1.csv", decSep=".", valSep=";")
    dict_PLZiel.einlesenDatei("testdata/helmert2.csv", decSep=".", valSep=";")

    punkte,parameter = HelmertTrans(dict_PLQuelle, dict_PLZiel).get_result()

    punkte = punkte.get_dic()
    for k,v in punkte.items():
        if "w" in v.keys():
            print(k,v["coord"], "RK:", v["w"]["y"].länge(), v["w"]["x"].länge())
        else:
            print(k,v["coord"])
    print(parameter)
