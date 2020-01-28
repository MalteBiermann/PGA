from math import acos, sin, cos

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.kreis import Kreis
from datentyp.punkt import Punkt
from datentyp.strecke import Strecke

class Bogenschnitt:
    def __init__(self, k1, k2):
        self.__k1 = k1
        self.__k2 = k2

    def berechne(self):
        s1 = self.__k1.get_r()
        s2 = self.__k2.get_r()

        s, t12 = Strecke(self.__k1.get_mp(), self.__k2.get_mp()).zweiteHA()
        w_a = acos((s1**2 + s**2 - s2**2) / (2 * s * s1))
        
        t1n_a = t12.get_w() + w_a
        t1n_b = t12.get_w() - w_a

        yn_a = self.__k1.get_mp().get_y() + s1 * sin(t1n_a)
        xn_a = self.__k1.get_mp().get_x() + s1 * cos(t1n_a)
        yn_b = self.__k1.get_mp().get_y() + s1 * sin(t1n_b)
        xn_b = self.__k1.get_mp().get_x() + s1 * cos(t1n_b)
        return (Punkt(yn_a,xn_a),Punkt(yn_b,xn_b))

if __name__ == "__main__":
    p1 = Punkt(328.76, 1207.85)
    p2 = Punkt(925.04, 954.33)
    # s1 = Strecke.init_länge2(p1, 294.33)
    # s2 = Strecke.init_länge2(p2, 506.42)

    k1 = Kreis(p1, 294.33)
    k2 = Kreis(p2, 506.42)

    p_res1,p_res2 = Bogenschnitt(k1, k2).berechne()
    print(p_res1, "\n" ,p_res2)