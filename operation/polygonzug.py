from math import pi, sin, cos
import json

if __name__ == "__main__":
    import sys
    sys.path.append(".")
    
from datentyp.polygon import Polygon
from datentyp.winkel import Winkel
from datentyp.punkt import Punkt
from datentyp.strecke import Strecke

class Polygonzug():  # Traverse
    def __init__(self):
        self.__polygon = Polygon()
        self.__parameter = {}

    def berechnePolygonzug(self):
        t_0 = Strecke(self.__polygon.get_PpointbyNr(0)["coord"], self.__polygon.get_PpointbyNr(1)["coord"]).zweiteHA()[1]
        self.__polygon.update_PpointAttributebyNr(0, {"t_0": t_0})
        t_n = Strecke(self.__polygon.get_PpointbyNr(-2)["coord"], self.__polygon.get_PpointbyNr(-1)["coord"]).zweiteHA()[1]
        self.__polygon.update_PpointAttributebyNr(-2, {"t_n": t_n})

        # w_beta
        n = self.__polygon.get_counter()-2  # Anzahl Messstandpunkte 5:(p0...p6)-2
        beta_summe = 0
        for i in range(1, n+1):  # testdata: Standpunkt p1...p6
            beta_summe += self.__polygon.get_PpointbyNr(i)["beta"].get_w()

        w_beta = self.__polygon.get_PpointbyNr(-2)["t_n"].get_w() - (self.__polygon.get_PpointbyNr(0)["t_0"].get_w() + beta_summe - (n*pi))
        if w_beta > pi:
            w_beta = 2*pi - w_beta
        w_beta = Winkel(w_beta)
        w_beta_n = Winkel(w_beta.get_w() / n)

        # r
        for i in range(1, n+1):  # testdata: Standpunkt p1...p6
            beta = self.__polygon.get_PpointbyNr(i)["beta"].get_w()
            if i == 1:
                r = self.__polygon.get_PpointbyNr(0)["t_0"].get_w() + beta + w_beta_n.get_w() + pi
            else:
                r = self.__polygon.get_PpointbyNr(i-1)["r"].get_w() + beta + w_beta_n.get_w() + pi
            if r < (2*pi):
                r += 2*pi
            elif r > (2*pi):
                r -= 2*pi
            self.__polygon.update_PpointAttributebyNr(i, {"r": Winkel(r)})

        # dy, dx Koordinatenunterschiede
        dy_summe = 0
        dx_summe = 0
        s_summe = 0
        for i in range(1, n):    # testdata: Standpunkt p1...p4
            s = self.__polygon.get_PpointbyNr(i)["s_vor"].länge()
            dy = s * sin(self.__polygon.get_PpointbyNr(i)["r"].get_w())
            dx = s * cos(self.__polygon.get_PpointbyNr(i)["r"].get_w())
            dy_summe += dy
            dx_summe += dx
            self.__polygon.update_PpointAttributebyNr(i, {"dy": dy})
            self.__polygon.update_PpointAttributebyNr(i, {"dx": dx})
            s_summe += s

        # w_y, w_x Koordinatenabschlussverbesserung
        w_y = (self.__polygon.get_PpointbyNr(-2)["coord"].get_y() - self.__polygon.get_PpointbyNr(1)["coord"].get_y()) - dy_summe
        w_x = (self.__polygon.get_PpointbyNr(-2)["coord"].get_x() - self.__polygon.get_PpointbyNr(1)["coord"].get_x()) - dx_summe
        w_y_s = (w_y / s_summe)
        w_x_s = (w_x / s_summe)

        # y,x Koordinaten
        for i in range(1, n-1):  # testdata: Standpunkt p1...p3
            s = self.__polygon.get_PpointbyNr(i)["s_vor"].länge()
            dy = self.__polygon.get_PpointbyNr(i)["dy"]
            dx = self.__polygon.get_PpointbyNr(i)["dx"]
            v_y = w_y_s * s
            v_x = w_x_s * s
            y = self.__polygon.get_PpointbyNr(i)["coord"].get_y() + dy + v_y
            x = self.__polygon.get_PpointbyNr(i)["coord"].get_x() + dx + v_x
            self.__polygon.update_PpointAttributebyNr(i+1, {"coord": Punkt(y, x)})
        self.__parameter.update({"w_beta":w_beta, "w_y":w_y, "w_x":w_x})

    def berechneRingpolygon(self):  # Für Außenwinkel
        n = self.__polygon.get_counter()    # testdata: 6:(p1...p6)
        beta_summe = 0
        s_summe = 0
        for pId in self.__polygon.get_pIdList():
            beta_summe += self.__polygon.get_PpointbyPId(pId)["beta"].get_w()
            s_summe += self.__polygon.get_PpointbyPId(pId)["s_vor"].länge()
        w_beta = Winkel((n+2) * pi - beta_summe)
        w_beta_n = Winkel(w_beta.get_w() / n)

        # r, dy, dx
        dy_summe = 0
        dx_summe = 0
        for i in range(n):  # testdata: Standpunkt p1...p6
            if i == 0:
                r = Winkel(0)
            else:
                r = Winkel(self.__polygon.get_PpointbyNr(i-1)["r"].get_w() + self.__polygon.get_PpointbyNr(i)["beta"].get_w() + w_beta_n.get_w() - pi)
            dy = sin(r.get_w()) * self.__polygon.get_PpointbyNr(i)["s_vor"].länge()
            dx = cos(r.get_w()) * self.__polygon.get_PpointbyNr(i)["s_vor"].länge()
            dy_summe += dy
            dx_summe += dx
            self.__polygon.update_PpointAttributebyNr(i, {"r": r, "dy": dy, "dx": dx})

        w_y_s = - dy_summe / s_summe
        w_x_s = - dx_summe / s_summe
        for i in range(1,n):    # testdata: Standpunkt p2...p6
            s = self.__polygon.get_PpointbyNr(i-1)["s_vor"].länge()
            r = self.__polygon.get_PpointbyNr(i-1)["r"].get_w()

            dy = self.__polygon.get_PpointbyNr(i-1)["dy"] + w_y_s * s
            dx = self.__polygon.get_PpointbyNr(i-1)["dx"] + w_x_s * s
            y = self.__polygon.get_PpointbyNr(i-1)["coord"].get_y()
            x = self.__polygon.get_PpointbyNr(i-1)["coord"].get_x()
            pId = self.__polygon.get_PpointbyNr(i-1)["coord"].get_id()

            self.__polygon.update_PpointAttributebyNr(i, {"coord": Punkt(y+dy, x+dx, pId)})
            self.__parameter.update({"w_beta":w_beta, "w_y":dy_summe, "w_x":dx_summe})

    def readFile(self, filepath, sepDec=".", sepVal=","):
        with open(filepath, "r") as fh:
            lines = fh.read()
        for l in lines.splitlines():
            if l == "": 
                break
            if sepDec != ".":
                l = l.replace(sepDec, ".")
            try:
                sId, beta, s_rück, s_vor, y, x = l.split(sepVal)
                a = {}
                if beta != "":
                    a["beta"] = Winkel(float(beta), "gon")
                if s_rück != "":
                    a["s_rück"] = Strecke.init_länge(float(s_rück))
                if s_vor != "":
                    a["s_vor"] = Strecke.init_länge(float(s_vor))
                if y != "" or x != "":
                    p = Punkt(float(y), float(x), sId)
                else:
                    p = Punkt(0, 0, sId)

                if sId in self.__polygon.get_pIdList():
                    self.__polygon.update_PpointAttributebyID(sId, a)
                else:
                    self.__polygon.add_Ppointwithcoords(p, a)
            except:
                pass
            self.__parameter.update({"w_beta":Winkel(0), "w_y":0, "w_x":0})

    def get_polygon(self):
        return self.__polygon
    
    def get_parameter(self):
        return self.__parameter

    def get_json(self):
        d = {"pDic":self.__polygon.get_pDic(), "pIdL":self.__polygon.get_pIdList(), "parameter":self.__parameter}
        return json.dumps(d, default=lambda obj: obj.get_json(), sort_keys=True, indent=4)

    def set_polygon_json(self,s):
        dic_j = json.loads(s)["parameter"]
        self.__parameter = {"w_beta":Winkel.init_json(dic_j["w_beta"]), "w_y":dic_j["w_y"], "w_x":dic_j["w_x"]}

        self.__polygon.set_json(s)

    def clean(self):
        self.__polygon.clean()
        self.__parameter.clear()



if __name__ == "__main__":
    pz = Polygonzug()
    pz.readFile("testdata/polygonzug_angeschlossen.csv", sepDec=".", sepVal=",")
    pz.berechnePolygonzug()
    pz_res = pz.get_polygon()

    n = pz_res.get_counter()
    for i in range(n):
        print(pz_res.get_pIdList()[i], end="   ")
        for k in pz_res.get_PpointbyNr(i).keys():
            if k in ("beta", "t_0", "t_n", "r", "dy", "dx", "coord"):
                if type(pz_res.get_PpointbyNr(i)[k]).__name__ == "Winkel":
                    print(k, pz_res.get_PpointbyNr(i)[k].get_w("gon"), end="   ")
                else: print(k, pz_res.get_PpointbyNr(i)[k], end="   ")
        print("\r")

    rp = Polygonzug()
    rp.readFile("testdata/ringpolygon.csv", sepDec=".", sepVal=",")
    rp.berechneRingpolygon()
    rp_res = rp.get_polygon()
    n = rp_res.get_counter()
    for i in range(n):
        print(rp_res.get_pIdList()[i], end="   ")
        for k in rp_res.get_PpointbyNr(i).keys():
            if k in ("beta", "t_0", "t_n", "r", "dP", "dx", "coord"):
                if type(rp_res.get_PpointbyNr(i)[k]).__name__ == "Winkel":
                    print(k, rp_res.get_PpointbyNr(i)[k].get_w("gon"), end="   ")
                else: print(k, rp_res.get_PpointbyNr(i)[k], end="   ")
        print("\r")
    print(pz.get_json())