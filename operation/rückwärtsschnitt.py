from math import tan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import *
from datentyp.punkt import *
from datentyp.strecke import *

class Rückwärtsschnitt:
    def __init__(self, pA, pB, pM, wAlpha, wBeta):
        self.__pA = pA
        self.__pB = pB
        self.__pM = pM
        self.__wAlpha = wAlpha
        self.__wBeta = wBeta

    def schneiden(self):
        A_y = self.__pA.get_y()
        A_x = self.__pA.get_x()
        B_y = self.__pB.get_y()
        B_x = self.__pB.get_x()
        M_y = self.__pM.get_y()
        M_x = self.__pM.get_x()

        C_y = A_y + (M_x - A_x) * (1/cos(self.__wAlpha.get_w()))
        C_x = A_x - (M_y - A_y) * (1/cos(self.__wAlpha.get_w()))
        D_y = B_y + (B_x - M_x) * (1/cos(self.__wBeta.get_w()))
        D_x = B_x - (B_y - M_y) * (1/cos(self.__wBeta.get_w()))

        s, CD_w = Strecke(Punkt(C_y,C_x),Punkt(D_y,D_x)).zweitegga()

        N_x = C_x + (M_y - C_y + (M_x - C_x) * (1/cos(CD_w.get_w())))
        N_y = C_y + (N_x - C_x) * tan(CD_w.get_w())

        return Punkt(N_y,N_x)


if __name__ == "__main__":
    pA = Punkt(46867.94, 5537.00)
    pB = Punkt(51293.86, 6365.89)
    pM = Punkt(49666.56, 4448.58)

    riwiA = 66.8117
    riwiB = 294.7845
    riwiM = 362.8516
    wAlpha = Winkel(riwiA - riwiM, "gon")
    wBeta = Winkel(riwiB - riwiM, "gon")

    pRes = Rückwärtsschnitt(pA,pB,pM,wAlpha,wBeta).schneiden()
    print(pRes)
