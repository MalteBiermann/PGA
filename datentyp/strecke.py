from copy import deepcopy
from math import sqrt, atan2, pi
import json

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import Winkel
from datentyp.punkt import Punkt

class Strecke:
    def __init__(self, p0=None, p1=None, p0_status=False, p1_status=False):
        if(p0 is None):
            p0 = Punkt()
        else:
            self.p0 = deepcopy(p0)

        if(p1 is None):
            p1 = Punkt()
        else:
            self.p1 = deepcopy(p1)

    @classmethod
    def init_länge(cls, l):
        p0 = Punkt()
        p1 = Punkt(0, l)
        return cls(p0, p1, False, False)

    @classmethod
    def init_länge2(cls, p0, l):
        p1 = Punkt(p0.get_y(), p0.get_x() + l)
        return cls(p0, p1, True, False)

    @classmethod
    def init_koor(cls, p0_y, p0_x, p1_y, p1_x):
        p0 = Punkt(p0_y, p0_x)
        p1 = Punkt(p1_y, p1_x)
        return cls(p0, p1, True, True)

    def subtrahiere(self):
        dy = self.p1.get_y() - self.p0.get_y()
        dx = self.p1.get_x() - self.p0.get_x()
        return dy,dx

    def länge(self):
        dy,dx = self.subtrahiere()
        return sqrt((dy ** 2 + dx ** 2))

    def zweiteHA(self):
        dy,dx = self.subtrahiere()
        t = atan2(dy, dx)
        if t < 0:
            t = 2*pi + t
        return self.länge(), Winkel(t, "rad")

    def __str__(self):
        return "Strecke: P0: " + str(self.p0) + " nach P1: " + str(self.p1)

    def get_json(self):
        return self.__dict__

    def set_json(self, p_dic):
        for k, v in p_dic.items():
            if(hasattr(self, k)):
                if (isinstance(v,dict)):
                    objekt = getattr(self,k)
                    objekt.set_json(v)
                else:
                    setattr(self, k, v)

    @classmethod
    def init_jsonKoor(cls, d):
        p0 = Punkt.init_json(d["p0"])
        p1 = Punkt.init_json(d["p1"])
        return cls(p0,p1)



if __name__ == "__main__":

    p0 = Punkt(0, 0)
    p1 = Punkt(0, 2)

    s = Strecke(p0, p1)
    d, t = s.zweiteHA()
    print(s, d, t)

    # s1 = Strecke.init_länge(3)
    # s2 = Strecke.init_länge2(p1, 3)
    # s3 = Strecke.init_koor(1.2, 3.4, 5.6, 7.8)
    # print(s1, "\t", s2, "\t", s3)

    #print(json.dumps(s, default=lambda objekt: objekt.get_json(),sort_keys=True, indent=4))

    jstr = """
{
    "p0": {
        "_Punkt__pId": "",
        "_Punkt__x": 0,
        "_Punkt__y": 0
    },
    "p1": {
        "_Punkt__pId": "",
        "_Punkt__x": 2,
        "_Punkt__y": 0
    }

}"""
    s = Strecke()
    s.set_json(json.loads(jstr))
    print(s)
