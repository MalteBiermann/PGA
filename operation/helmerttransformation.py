from math import sqrt, atan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt,Punkt_Dic
from datentyp.strecke import Strecke


class HelmertTrans:
    def __init__(self, d_p0, d_p1, l_p1exclude=None):
        dicP0 = d_p0.get_dic()
        dicP1 = d_p1.get_dic()        
        self.__dicP2 = Punkt_Dic()
        self.__tParameter = {}

        if l_p1exclude is not None:
            for e in l_p1exclude:
                dicP1.pop(e, None)

        l_p_ident = []
        for k in dicP0.keys():
            if k in dicP1.keys():
                l_p_ident.append(k)

        y_cog = 0
        x_cog = 0
        Y_cog = 0
        X_cog = 0
        for k in l_p_ident:
            y_cog += dicP0[k].get_y()
            x_cog += dicP0[k].get_x()
            Y_cog += dicP1[k].get_y()
            X_cog += dicP1[k].get_x()

        i = len(l_p_ident)
        y_cog = y_cog / i
        x_cog = x_cog / i
        Y_cog = Y_cog / i
        X_cog = X_cog / i

        PDic0_reduced = {}
        PDic1_reduced = {}
        for k in l_p_ident:
            y_red = dicP0[k].get_y() - y_cog
            x_red = dicP0[k].get_x() - x_cog
            PDic0_reduced.update({k: Punkt(y_red, x_red)})

            Y_red = dicP1[k].get_y() - Y_cog
            X_red = dicP1[k].get_x() - X_cog
            PDic1_reduced.update({k: Punkt(Y_red, X_red)})

        o_nenner = 0
        a_nenner = 0
        o_zähler = 0
        a_zähler = 0
        for k in l_p_ident:
            o_zähler += PDic0_reduced[k].get_x() * PDic1_reduced[k].get_y() -\
                PDic0_reduced[k].get_y() * PDic1_reduced[k].get_x()
            o_nenner += PDic0_reduced[k].get_x()**2 + PDic0_reduced[k].get_y()**2
            
            a_zähler += PDic0_reduced[k].get_x() * PDic1_reduced[k].get_x() +\
                PDic0_reduced[k].get_y() * PDic1_reduced[k].get_y()
            a_nenner += PDic0_reduced[k].get_x()**2 + PDic0_reduced[k].get_y()**2

        a = a_zähler / a_nenner
        o = o_zähler / o_nenner
        maßstab = sqrt(a ** 2 + o ** 2)
        epsilon = atan(o / a)
        Y0 = Y_cog - a * y_cog - o * x_cog
        X0 = X_cog - a * x_cog + o * y_cog
        
        self.__tParameter.update({"m":maßstab})
        self.__tParameter.update({"epsilon":epsilon})
        self.__tParameter.update({"Y0":Y0})
        self.__tParameter.update({"X0":X0})


        dicPTrans = {}
        for k,v in dicP0.items():
            y = v.get_y()
            x = v.get_x()
            id = v.get_id()
            Y = Y0 + a * y + o * x
            X = X0 + a * x - o * y
            pTransformiert = {"Punkt":Punkt(Y,X,id)}
            dicPTrans.update({id:pTransformiert})            
            if k in l_p_ident:
                wy = - Y0 - a*dicP0[k].get_y() - o*dicP0[k].get_x() + dicP1[k].get_y()
                wx = - X0 - a*dicP0[k].get_x() + o*dicP0[k].get_y() + dicP1[k].get_x()
                w = {"y":Strecke.init_länge(wy), "x":Strecke.init_länge(wx)}
                dicPTrans[k].update({"w":w})
        
        self.__dicP2.set_dic(dicPTrans)


    def get_result(self):
        return (self.__dicP2, self.__tParameter)



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

    ht = HelmertTrans(dict_PLQuelle, dict_PLZiel)

    punkte,parameter = ht.get_result()
    punkte = punkte.get_dic()
    for k,v in punkte.items():
        if "w" in v.keys():
            print(k,v["Punkt"], "RK:", v["w"]["y"].länge(), v["w"]["x"].länge())
        else:
            print(k,v["Punkt"])
    print(parameter)
