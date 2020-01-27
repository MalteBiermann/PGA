from math import pi, sin, cos
from copy import deepcopy

if __name__ == "__main__":
    import sys
    sys.path.append(".")

# from datentyp.strecke import Strecke
# from datentyp.winkel import Winkel

class Punkt:
    def __init__(self, p_y=0, p_x=0):
        self.__y = deepcopy(p_y)
        self.__x = deepcopy(p_x)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_json(self):
        return self.__dict__

    def set_json(self, p_dic):
        for k, v in p_dic.items():
            if(hasattr(self,k)):
                setattr(self, k, v) 

    def __str__(self):
        return str(self.get_y()) + "|" + str(self.get_x())


    def ersteHA(self, p12_s, p12_t):
        y2 = self.__y + (p12_s.länge() * sin(p12_t.get_w()))
        x2 = self.__x + (p12_s.länge() * cos(p12_t.get_w()))
        return Punkt(y2, x2)


if __name__ == "__main__":
    from datentyp.winkel import Winkel
    from datentyp.strecke import Strecke
    import operation.hauptaufgaben

    p1 = Punkt(1, 1)
    p12_t = Winkel(100, "gon")
    s = 1

    p12_s = Strecke.init_länge(s)
    result_p2 = operation.hauptaufgaben.erste(p1, p12_s, p12_t)
    # result_p1 = p0.ersteHA(p1_s, t)
    print("P1:", p1, "Strecke:", s, "Winkel:", p12_t, "P1:", result_p2)


