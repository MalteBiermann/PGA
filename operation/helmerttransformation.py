from math import sqrt, atan
if __name__ == "__main__":
    __package__ = '__operationen__'
    from .datentypen import punkt
#from .datentypen.punkt import Punkt


class HelmertT:
    def __init__(self, d_p0, d_p1):
        y_cog = 0
        x_cog = 0
        Y_cog = 0
        X_cog = 0
        i = 0

        l_p_ident = []
        for k in d_p0.dic.keys():
            if k in d_p1.dic.keys():
                l_p_ident.append(k)

        for k in l_p_ident:
            y_cog += d_p0.dic[k].get_y()
            x_cog += d_p0.dic[k].get_x()
            Y_cog += d_p1.dic[k].get_y()
            X_cog += d_p1.dic[k].get_x()

        i = len(l_p_ident)
        y_cog = y_cog / i
        x_cog = x_cog / i
        Y_cog = Y_cog / i
        X_cog = X_cog / i

        d_p0_red = {}
        d_p1_red = {}
        for k in l_p_ident:
            y = d_p0.dic[k].get_y() - y_cog
            x = d_p0.dic[k].get_x() - x_cog
            d_p0_red.update({k: Punkt(y, x)})

            Y = d_p1.dic[k].get_y() - Y_cog
            X = d_p1.dic[k].get_x() - X_cog
            d_p1_red.update({k: Punkt(Y, X)})

        o_nenner = 0
        a_nenner = 0
        o_zähler = 0
        a_zähler = 0
        for k in l_p_ident:
            o_zähler += (d_p0_red[k].get_x() * d_p1_red[k].get_y() -
                         d_p0_red[k].get_y() * d_p1_red[k].get_x())
            o_nenner += (d_p0_red[k].get_x()**2 + d_p0_red[k].get_x()**2)
            
            a_zähler += (d_p0_red[k].get_x() * d_p1_red[k].get_x() -
                         d_p0_red[k].get_y() * d_p1_red[k].get_y())
            a_nenner += (d_p0_red[k].get_x()**2 + d_p0_red[k].get_x()**2)
        a = a_zähler / a_nenner
        o = o_zähler / o_nenner
        m = sqrt(a ** 2 + o ** 2)
        epsilon = atan(o / a)
        
        

class Dic_P:
    def __init__(self):
        self.dic = {}

    def einlesen(self, liste):
        for l in liste.splitlines():
            nr, y, x = l.split(";")
            p = Punkt(float(y), float(x))
            self.dic.update({nr: p})

    def einlesen_datei(self, datei):
        with open(datei) as fh:
            datei.readline()
            for l in datei.readlines():
                nr, y, x = l.split(";")

                p = Punkt(float(y), float(x))
                self.dic.update({nr: p})


if __name__ == "__main__":
    
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))


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

    dic_p0 = Dic_P()
    dic_p1 = Dic_P()
    #dic_p0.einlesen(str_pl0)
    #dic_p1.einlesen(str_pl1)
    dic_p0.einlesen_datei(str_pl0)
    dic_p1.einlesen_datei(str_pl1)
    ht = HelmertT(dic_p0, dic_p1)
