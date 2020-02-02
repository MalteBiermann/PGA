from math import sqrt, atan

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt,Punkt_Dic
from datentyp.strecke import Strecke

class Transformation:
    def __init__(self, d_p0, d_p1, l_p1exclude=None):
        self._dicP0 = d_p0.get_dic()
        self._dicP1 = d_p1.get_dic()        
        self._dicP2 = Punkt_Dic()
        self._tParameter = {}

        if l_p1exclude is not None:
            for e in l_p1exclude:
                self._dicP1.pop(e, None)

        self._l_p_ident = []
        for k in self._dicP0.keys():
            if k in self._dicP1.keys():
                self._l_p_ident.append(k)

        y_cog = 0
        x_cog = 0
        Y_cog = 0
        X_cog = 0
        for k in self._l_p_ident:
            y_cog += self._dicP0[k]["coord"].get_y()
            x_cog += self._dicP0[k]["coord"].get_x()
            Y_cog += self._dicP1[k]["coord"].get_y()
            X_cog += self._dicP1[k]["coord"].get_x()

        i = len(self._l_p_ident)
        y_cog = y_cog / i
        x_cog = x_cog / i
        Y_cog = Y_cog / i
        X_cog = X_cog / i

        self._P0_cog = Punkt(y_cog,x_cog)
        self._P1_cog = Punkt(Y_cog,X_cog)

        self._PDic0_reduced = {}
        self._PDic1_reduced = {}
        for k in self._l_p_ident:
            y_red = self._dicP0[k]["coord"].get_y() - self._P0_cog.get_y()
            x_red = self._dicP0[k]["coord"].get_x() - self._P0_cog.get_x()
            self._PDic0_reduced.update({k: Punkt(y_red, x_red)})

            Y_red = self._dicP1[k]["coord"].get_y() - self._P1_cog.get_y()
            X_red = self._dicP1[k]["coord"].get_x() - self._P1_cog.get_x()
            self._PDic1_reduced.update({k: Punkt(Y_red, X_red)})