import json

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt,Punkt_Dic

# Punkt_Dic(ungeordnet) kombiniert mit einer Liste um Punkte in eine Reihenfolge zu bringen
class Polygon:
    def __init__(self):
        self.__pIdList = []
        self.__PDic = Punkt_Dic()
    
    def get_pIdList(self):
        return self.__pIdList
        
    def add_Ppointwithcoords(self,p,attribute=None):
        self.__PDic.addPoint(p)
        self.__pIdList.append(p.get_id())
        if attribute != None:
            pId = self.__pIdList[-1]
            self.__PDic.setAttribute(pId,attribute)

    def update_PpointAttributebyNr(self, OrderNr, a):
        pId = self.__pIdList[OrderNr]
        self.__PDic.setAttribute(pId,a)

    def update_PpointAttributebyID(self, sId, a):
        self.__PDic.setAttribute(sId,a)

    def add_NextPointByDirDist(self, dir, dist):
        currentNr = len(self.__pIdList)
        previousPId = self.__pIdList[-1]
        p = self.__PDic.get_dic()[previousPId]["coord"].ersteHA(dist, dir)
        p.set_id(currentNr)
        self.add_Ppointwithcoords(p)

    def get_PpointbyNr(self,OrderNr):
        pId = self.__pIdList[OrderNr]
        return self.get_PpointbyPId(pId)

    def get_PpointbyPId(self,pId):
        return self.__PDic.get_dic()[pId]

    def get_counter(self):
        return len(self.__pIdList)
    
    def get_pDic(self):
        return self.__PDic.get_dic()

    def get_json(self):
        pDic_j = json.dumps(self.__PDic.get_json(), default=lambda objekt: objekt.get_json(), sort_keys=True, indent=4)
        pIdL_j = json.dumps(self.__pIdList)
        return {"pDic": pDic_j, "pIdL":pIdL_j}

    def set_json(self,s):
        p_j = json.loads(s)
        pIdL = p_j["pIdL"]
        pDic = p_j["pDic"]
        self.__PDic.from_json(json.loads(pDic))
        self.__pIdList = json.loads(pIdL)

    def clean(self):
        self.__pIdList.clear()
        self.__PDic.clear()



if __name__ == "__main__":
    from datentyp.winkel import Winkel
    from datentyp.strecke import Strecke

    p0 = Punkt(1,1,"p01")

    dir01 = Winkel(50, "gon")
    dist01 = Strecke.init_länge(3)

    poly = Polygon()
    poly.add_Ppointwithcoords(p0)
    poly.add_NextPointByDirDist(dir01,dist01)
    poly.add_NextPointByDirDist(dir01,dist01)
    poly.update_PpointAttributebyNr(2,{"test": 1235})


    print(poly.get_PpointbyNr(2))

