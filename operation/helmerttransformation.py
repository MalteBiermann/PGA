from math import sqrt, atan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt
from datentyp.strecke import Strecke


class HelmertTrans:
    def __init__(self, d_p0, d_p1):
        PDic0 = d_p0.get_dic()
        PDic1 = d_p1.get_dic()        
        self.__PDic2 = Punkt_Dic()
        #self.__maßstab = 1

        l_p_ident = []
        for k in PDic0.keys():
            if k in PDic1.keys():
                l_p_ident.append(k)

        y_cog = 0
        x_cog = 0
        Y_cog = 0
        X_cog = 0
        for k in l_p_ident:
            y_cog += PDic0[k].get_y()
            x_cog += PDic0[k].get_x()
            Y_cog += PDic1[k].get_y()
            X_cog += PDic1[k].get_x()

        i = len(l_p_ident)
        y_cog = y_cog / i
        x_cog = x_cog / i
        Y_cog = Y_cog / i
        X_cog = X_cog / i

        PDic0_reduced = {}
        PDic1_reduced = {}
        for k in l_p_ident:
            y_red = PDic0[k].get_y() - y_cog
            x_red = PDic0[k].get_x() - x_cog
            PDic0_reduced.update({k: Punkt(y_red, x_red)})

            Y_red = PDic1[k].get_y() - Y_cog
            X_red = PDic1[k].get_x() - X_cog
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
        self.__maßstab = sqrt(a ** 2 + o ** 2)
        self.__epsilon = atan(o / a)
        self.__Y0 = Y_cog - a * y_cog - o * x_cog
        self.__X0 = X_cog - a * x_cog + o * y_cog
        
        DicPTrans = {}
        for k,v in PDic0.items():
            y = v.get_y()
            x = v.get_x()
            id = v.get_id()
            Y = self.__Y0 + a * y + o * x
            X = self.__X0 + a * x - o * y
            pTransformiert = Punkt(Y,X,id)
            DicPTrans.update({id:pTransformiert})
        self.__PDic2.set_dic(DicPTrans)

        self.__restklaffen = {}
        for k in l_p_ident:
            wy = - self.__Y0 - a*PDic0[k].get_y() - o*PDic0[k].get_x() + PDic1[k].get_y()
            wx = - self.__X0 - a*PDic0[k].get_x() + o*PDic0[k].get_y() + PDic1[k].get_x()
            w = {"y":Strecke.init_länge(wy), "x":Strecke.init_länge(wx)}
            self.__restklaffen.update({k: w})
            
        


    def get_result(self):
        return self.__PDic2


class Punkt_Dic:
    def __init__(self):
        self.__Pdic = {}

    def get_dic(self):
        return self.__Pdic

    def set_dic(self,d):
        self.__Pdic = d

    def einlesenListe(self, liste, decSep=".",valSep=";"):
        for l in liste.splitlines():
            if decSep != ".":
                l = l.replace(decSep,".")
            try:
                nr, y, x = l.split(valSep)
                p = Punkt(float(y), float(x), nr)
                self.__Pdic.update({nr: p})
            except:
                pass
            

    def einlesenDatei(self, datei):
        with open(datei) as fh:
            lines = fh.readlines()
            self.einlesenListe(lines)



if __name__ == "__main__":

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

#     str_pl1 = """1 32504989.727 5895259.877
# 2 32505415.520 5895362.202
# 3 32505468.158 5895140.821
# 4 32505733.235 5895238.530"""

#     str_pl0 = """1 56.054 263.191
# 2 237.438 387.810
# 3 302.635 294.019
# 4 409.606 387.495
# 5 481.762 378.895"""

    dict_Punktliste1 = Punkt_Dic()
    dict_Punktliste1.einlesenListe(str_pl0,".",";")

    dict_Punktliste2 = Punkt_Dic()
    dict_Punktliste2.einlesenListe(str_pl1,".",";")

    # dic_p0.einlesen_datei(str_pl0)
    # dic_p1.einlesen_datei(str_pl1)
    ht = HelmertTrans(dict_Punktliste1, dict_Punktliste2)

    d = ht.get_result().get_dic()
    for k,v in d.items():
        print(k,v)
