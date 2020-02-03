from math import tan,cos,pi

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import Winkel
from datentyp.punkt import Punkt
from datentyp.strecke import Strecke

class Rückwärtsschnitt:
    def __init__(self, pA, pB, pM, aAlpha, aBeta):
        self.__pA = pA
        self.__pB = pB
        self.__pM = pM
        self.__aAlpha = aAlpha
        self.__aBeta = aBeta
    
    @classmethod
    def init_dir(cls,pA, pB, pM, dirA, dirB, dirM):
        aAlpha = dirA.get_w() - dirM.get_w()
        aBeta = dirB.get_w() - dirM.get_w()
        aAlpha,aBeta = [e + 2*pi if e < 0 else e for e in [aAlpha,aBeta]]
        return cls(pA, pB, pM, Winkel(aAlpha), Winkel(aBeta))


    def schneiden(self):
        A_y = self.__pA.get_y()
        A_x = self.__pA.get_x()
        B_y = self.__pB.get_y()
        B_x = self.__pB.get_x()
        M_y = self.__pM.get_y()
        M_x = self.__pM.get_x()
        alpha = self.__aAlpha.get_w()
        beta = self.__aBeta.get_w()

        dMA_y = A_y - M_y
        dMA_x = A_x - M_x
        dMB_y = B_y - M_y
        dMB_x = B_x - M_x

        tan_MN = (dMA_y * cot(alpha) - dMB_y * cot(beta) + (dMB_x - dMA_x)) /\
            (dMA_x * cot(alpha) - dMB_x * cot(beta) - (dMB_y - dMA_y))

        dMN_x = ((dMA_y + dMA_x * cot(alpha)) * tan_MN + (dMA_x - dMA_y * cot(alpha))) /\
            (1+tan_MN**2)
        dMN_y = dMN_x * tan_MN

        N_y = M_y + dMN_y
        N_x = M_x + dMN_x

        return Punkt(N_y,N_x)

def cot(a):
    return (1/tan(a))




if __name__ == "__main__":
    pA = Punkt(46867.94, 5537.00)
    pM = Punkt(49666.56, 4448.58)    
    pB = Punkt(51293.86, 6365.89)
    riwiA = Winkel(66.8117,"gon")
    riwiM = Winkel(362.8516, "gon")
    riwiB = Winkel(294.7845, "gon")
    # pA = Punkt(209.13, 193.4)
    # pM = Punkt(420.68, 639.27)    
    # pB = Punkt(578.47, 198.38)
    # riwiA = 0.0
    # riwiM = 116.895
    # riwiB = 284.622

    pRes = Rückwärtsschnitt.init_dir(pA,pB,pM,riwiA,riwiB,riwiM).schneiden()
    print(pRes)
