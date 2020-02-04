from math import tan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.strecke import Strecke
from datentyp.punkt import Punkt
from datentyp.winkel import Winkel


class Vorwärtsschnitt:
    def __init__(self, p1, p2, p3, p4, tPhi, tPsi):
        self.__p1 = p1
        self.__p2 = p2
        self.__p3 = p3
        self.__p4 = p4
        self.__tPhi = tPhi
        self.__tPsi = tPsi

    def schneiden(self):
        p1_y = self.__p1.get_y()
        p1_x = self.__p1.get_x()
        p2_y = self.__p2.get_y()
        p2_x = self.__p2.get_x()

        t_41 = Strecke(self.__p1, self.__p4).zweiteHA()[1].get_w()
        t_1N = t_41 + self.__tPhi.get_w()
        tan_1N = tan(t_1N)

        t_23 = Strecke(self.__p2, self.__p3).zweiteHA()[1].get_w()
        t_2N = t_23 + self.__tPsi.get_w()
        tan_2N = tan(t_2N)

        pN_x = p1_x + ((p2_y - p1_y) - (p2_x - p1_x) * tan_2N) / (tan_1N - tan_2N)
        pN_y = p1_y + (pN_x - p1_x) * tan_1N

        return Punkt(pN_y, pN_x)


if __name__ == "__main__":
    p1 = Punkt(24681.92, 90831.87)
    p4 = Punkt(23231.58, 91422.92)
    p2 = Punkt(24877.72, 89251.09)
    p3 = Punkt(22526.65, 89150.52)
    tPhi = Winkel(331.6174, "gon")
    tPsi = Winkel(60.7510, "gon")
    pN = Vorwärtsschnitt(p1, p2, p3, p4, tPhi, tPsi).schneiden()
    print(pN)
