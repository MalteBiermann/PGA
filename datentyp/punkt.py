from math import pi, sin, cos
from copy import deepcopy
import json

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import Winkel

class Punkt:
    def __init__(self, p_y=0, p_x=0, pId=""):
        self.__y = deepcopy(p_y)
        self.__x = deepcopy(p_x)
        self.__pId = deepcopy(pId)

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def get_id(self):
        return self.__pId

    def set_y(self, y):
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_id(self, pId):
        self.__pId = pId

    def get_json(self):
        return self.__dict__

    def set_json(self, p_dic):
        for k, v in p_dic.items():
            if(hasattr(self,k)):
                setattr(self, k, v) 
    
    @classmethod
    def init_json(cls, d):
        return cls(d["_Punkt__y"], d["_Punkt__x"], d["_Punkt__pId"])

    def __str__(self):
        return self.get_id() + ": " + str(self.get_y()) + "|" + str(self.get_x())

    def ersteHA(self, p12_s, p12_t):
        y2 = self.__y + (p12_s.länge() * sin(p12_t.get_w()))
        x2 = self.__x + (p12_s.länge() * cos(p12_t.get_w()))
        return Punkt(y2, x2)


class Punkt_Dic:
    def __init__(self):
        self.__Pdic = {}

    def get_dic(self):
        return self.__Pdic

    def set_dic(self,d):
        self.__Pdic = d

    def clear(self):
        self.__Pdic.clear()

    def addPoint(self,p):
        pId = p.get_id()
        self.__Pdic.update({pId: {"coord":p}})

    def getPointCoord(self, pId):
        return self.__Pdic[pId]["coord"]

    def setAttribute(self,pId,a):
        self.__Pdic[pId].update(a)
    
    def getAttribute(self,pId,a):
        return self.__Pdic[pId][a]

    def einlesenListe(self, liste, sepDec=".",sepVal=";"):
        for l in liste.splitlines():
            if sepDec != ".":
                l = l.replace(sepDec,".")
            try:
                pId, y, x = l.split(sepVal)
                p = Punkt(float(y), float(x), pId)
                self.addPoint(p)
            except:
                pass

    def einlesenDatei(self, filepath, sepDec=".",sepVal=";"):
        with open(filepath) as fh:
            lines = fh.read()
            self.einlesenListe(lines,sepDec,sepVal)

    def get_json(self):
        return self.__dict__

    def set_json(self, p_dic):
        for k, v in p_dic.items():
            if(hasattr(self, k)):
                if (isinstance(v, dict)):
                    objekt = getattr(self,k)
                    objekt.set_json(v)
                else:
                    setattr(self, k, v)

    def from_json(self, d):
        from datentyp.strecke import Strecke
        pd = {}
        for v in d.values():
            for k1, v1 in v.items():
                pd.update({k1:{}})
                for k2, v2 in v1.items():   #Transformationen
                    if k2 == "coord":
                        c = {"coord": Punkt.init_json(v2)}
                        pd[k1].update(c)
                    elif k2 == "w":
                        pd[k1].update({"w":Punkt.init_json(v2)})
                    elif k2 == "beta":
                        pd[k1].update({"beta":Winkel.init_json(v2)})
                    elif k2 == "r":
                        pd[k1].update({"r":Winkel.init_json(v2)})
                    elif k2 == "s_vor":
                        pd[k1].update({"s_vor":Strecke.init_jsonKoor(v2)})
        self.set_dic(pd)

    def from_jsonPoly(self, d):
        from datentyp.strecke import Strecke
        pd = {}
        for k,v in d.items():
            pd.update({k:{}})
            for k1, v1 in v.items():
                if k1 == "coord":
                    c = {"coord": Punkt.init_json(v1)}
                    pd[k].update(c)
                elif k1 == "w":
                    pd[k].update({"w":Punkt.init_json(v1)})
                elif k1 == "beta":
                    pd[k].update({"beta":Winkel.init_json(v1)})
                elif k1 == "t_n":
                    pd[k].update({"t_n":Winkel.init_json(v1)})
                elif k1 == "t_0":
                    pd[k].update({"t_0":Winkel.init_json(v1)})
                elif k1 == "r":
                    pd[k].update({"r":Winkel.init_json(v1)})
                elif k1 == "s_vor":
                    pd[k].update({"s_vor":Strecke.init_jsonKoor(v1)})
        self.set_dic(pd)


if __name__ == "__main__":
    from datentyp.winkel import Winkel
    from datentyp.strecke import Strecke

    p1 = Punkt(1, 1,"Test")
    p12_t = Winkel(100, "gon")
    s = 1
    p12_s = Strecke.init_länge(s)
    result_p2 = p1.ersteHA(p12_s, p12_t)
    #print("P1:", p1, "Strecke:", s, "Winkel:", p12_t, "P1:", result_p2)

    jp = json.dumps(p1, default=lambda objekt: objekt.get_json(),sort_keys=True, indent=4)
    print(jp)
    p_j = Punkt.init_json(json.loads(jp))
    print(p_j)

    pDic = Punkt_Dic()
    pDic.addPoint(p1)
    pDic.addPoint(Punkt(10,10,"test2"))
    pDic.setAttribute("Test",{"w":Punkt(0.1,0.1,"w")})
    j_pd = json.dumps(pDic, default=lambda obj: obj.get_json(),sort_keys=True, indent=4)
    print(j_pd)

    pd_j = Punkt_Dic()
    pd_j.from_json(json.loads(j_pd))
    print(pd_j)



