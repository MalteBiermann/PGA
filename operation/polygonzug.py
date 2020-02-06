from math import pi,sin,cos

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.strecke import Strecke
from datentyp.punkt import Punkt
from datentyp.winkel import Winkel

class Polygonzug():
    def __init__(self):
        self.__Slist = []
    def berechnePolygonzug(self):
        self.__Slist[0]["t_0"] = Strecke(self.__Slist[0]["Punkt"], self.__Slist[1]["Punkt"]).zweiteHA()[1]
        self.__Slist[-2]["t_n"] = Strecke(self.__Slist[-2]["Punkt"], self.__Slist[-1]["Punkt"]).zweiteHA()[1]


        # w_beta
        n = len(self.__Slist)-2 # Anzahl Messstandpunkte 5
        beta_summe = 0
        for i in range(1,n+1):  # Standpunkt 1...6
            beta_summe += self.__Slist[i]["beta"].get_w()
        
        w_beta = self.__Slist[-2]["t_n"].get_w() - (self.__Slist[0]["t_0"].get_w() + beta_summe - (n*pi))
        w_beta = 2*pi - w_beta
        w_beta_n = w_beta / n

        # r
        for i in range(1,n+1): # Standpunkt 1...6
            if i == 1:
                r = self.__Slist[0]["t_0"].get_w() + self.__Slist[i]["beta"].get_w() + w_beta_n + pi
            else:
                r = self.__Slist[i-1]["r"].get_w() + self.__Slist[i]["beta"].get_w() + w_beta_n + pi
            if r<(2*pi):
                r += 2*pi
            elif r>(2*pi):
                r -= 2*pi
            self.__Slist[i]["r"] = Winkel(r)

        #dy, dx
        dy_summe = 0
        dx_summe = 0
        s_summe = 0
        for i in range(1,n):    # Standpunkt 1...5
            dy = self.__Slist[i]["s_vor"].länge() * sin(self.__Slist[i]["r"].get_w())
            dx = self.__Slist[i]["s_vor"].länge() * cos(self.__Slist[i]["r"].get_w())
            dy_summe += dy
            dx_summe += dx
            self.__Slist[i+1]["dy"] = dy
            self.__Slist[i+1]["dx"] = dx
            s_summe += self.__Slist[i]["s_vor"].länge()

        w_y = (self.__Slist[-2]["Punkt"].get_y() - self.__Slist[1]["Punkt"].get_y()) - dy_summe
        w_x = (self.__Slist[-2]["Punkt"].get_x() - self.__Slist[1]["Punkt"].get_x()) - dx_summe

        # y,x
        for i in range(2,n):    #Standpuntk 2...5
            s = self.__Slist[i-1]["s_vor"].länge()
            y = self.__Slist[i-1]["Punkt"].get_y() + s * sin(self.__Slist[i-1]["r"].get_w()) + w_y / s_summe * s
            x = self.__Slist[i-1]["Punkt"].get_x() + s * cos(self.__Slist[i-1]["r"].get_w()) + w_x / s_summe * s
            self.__Slist[i]["Punkt"] = Punkt(y,x)


    def readFilePolygonzug(self, filepath, sepDec=".", sepVal=","):
        with open(filepath,"r") as fh:
            lines = fh.read()
        for l in lines.splitlines():
            if sepDec != ".":
                l = l.replace(sepDec,".")
            try:
                sId, beta, s_rück, s_vor, y, x = l.split(sepVal)

                if beta != "":
                    beta = Winkel(float(beta),"gon")
                else:
                    beta = None

                if s_rück != "":
                    s_rück = Strecke.init_länge(float(s_rück))
                else:
                    s_rück = None

                if s_vor != "":
                    s_vor = Strecke.init_länge(float(s_vor))
                else:
                    s_vor = None

                if y != "" or x != "":
                    p = Punkt(float(y), float(x), sId)
                else:
                    p = None

                self.__Slist.append({"sId":sId, "beta":beta, "s_rück":s_rück, "s_vor":s_vor, "Punkt":p})
            except:
                pass

    def get_Slist(self):
        return self.__Slist


if __name__ == "__main__":
    pz = Polygonzug()
    pz.readFilePolygonzug("testdata/polygonzug_angeschlossen.csv", sepDec=".", sepVal=",")
    pz.berechnePolygonzug()
    res = pz.get_Slist()
    n = len(res)
    for i in range(n):
        for k in res[i].keys():
            if k in ("sId", "beta", "t_0", "t_n", "r", "dy", "dx", "Punkt"):
                if type(res[i][k]).__name__ == "Winkel":
                    print(k, res[i][k].get_w("gon"), end=" ")
                else:
                    print(k, res[i][k], end=" ")
        print("\r")