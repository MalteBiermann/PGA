from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Label,Entry,StringVar,Radiobutton,IntVar,DoubleVar,END
from tkinter.ttk import Treeview

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.helmerttransformation import HelmertTrans, Punkt_Dic
from gui.load_pointList import Fenster_loadPList

class FensterTrans(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.__dict_PLQuelle = Punkt_Dic()
        self.__dict_PLZiel = Punkt_Dic()
        self.__dict_PLTrans = Punkt_Dic()

        self.filePathSource = StringVar()
        self.filePathDest = StringVar()

        self.dblParaM = DoubleVar()
        self.dblParaRot = DoubleVar()
        self.dblParaTransY = DoubleVar()
        self.dblParaTransX = DoubleVar()

        self.radioTrans = IntVar(root,value=0)

        self.grid()

        lfTransType = LabelFrame(root, text="Ebene Transformationen")
        lfTransType.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        lfSource = LabelFrame(root, text="Quellsystem")
        lfSource.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=2)
        lfDest = LabelFrame(root, text="Zielsystem")
        lfDest.grid(row=1, column=2, padx=3, pady=3, sticky="w", columnspan=2)
        lfParameter = LabelFrame(root, text="Parameter")
        lfParameter.grid(row=2, column=2, padx=3, pady=3, sticky="e", columnspan=2)
        lfTrans = LabelFrame(root, text="Transformiert")
        lfTrans.grid(row=4, column=0, padx=3, pady=3, sticky="w",columnspan=3)

        Radiobutton(lfTransType,text="Helmerttransformation", variable=self.radioTrans, value=0).grid(row=0, column=0, padx=3, pady=3)
        Radiobutton(lfTransType,text="Affintransformation", variable=self.radioTrans, value=1).grid(row=0, column=1, padx=3, pady=3)

        Button(root,text="Lade Punkte",command=self.BtnPressedLoadPoints).grid(row=0, column=1, padx=3, pady=3, sticky="w")

        self.punktListSource = Treeview(lfSource)
        self.punktListSource.grid(row=0, column=0, padx=3, pady=3)
        self.punktListSource["columns"] = ("y", "x")
        self.punktListSource.column("#0",width = 50, minwidth=50)
        self.punktListSource.heading("#0",text="id")
        self.punktListSource.heading("y",text="y")
        self.punktListSource.heading("x",text="x")

        self.punktListDest = Treeview(lfDest)
        self.punktListDest.grid(row=0, column=0, padx=3, pady=3)
        self.punktListDest["columns"] = ("y", "x")
        self.punktListDest.column("#0",width = 50, minwidth=50)
        self.punktListDest.heading("#0",text="id")
        self.punktListDest.heading("y",text="y")
        self.punktListDest.heading("x",text="x")

        Button(root,text="Berechnen",command=self.BtnPressedCalc).grid(row=2, column=1, padx=3, pady=3, columnspan=1)

        Label(lfParameter,text="Maßstab").grid(row=0, column=0, padx=3, pady=3,)
        Label(lfParameter,text="Rotation").grid(row=1, column=0, padx=3, pady=3,)
        Label(lfParameter,text="Translation Y").grid(row=2, column=0, padx=3, pady=3,)
        Label(lfParameter,text="Translation X").grid(row=3, column=0, padx=3, pady=3,)

        Entry(lfParameter,textvariable=self.dblParaM,state="readonly").grid(row=0, column=1, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaRot,state="readonly").grid(row=1, column=1, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaTransY,state="readonly").grid(row=2, column=1, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaTransX,state="readonly").grid(row=3, column=1, padx=3, pady=3,)

        self.punktListTrans = Treeview(lfTrans)
        self.punktListTrans.grid(row=0, column=0, padx=3, pady=3)
        self.punktListTrans["columns"] = ("Y", "X","Rk Y","Rk X")
        self.punktListTrans.column("#0",width = 50, minwidth=50)
        self.punktListTrans.heading("#0",text="id")
        self.punktListTrans.heading("Y",text="Y")
        self.punktListTrans.heading("X",text="X")
        self.punktListTrans.heading("Rk Y",text="Restklaffe Y")
        self.punktListTrans.heading("Rk X",text="Restklaffe X")
        
        # self.focus_set()
        # self.grab_set()
        # self.wait_window()

    def loadPoints(self, text, sepDec, sepVal, system):
        if system == 0:
            self.__dict_PLQuelle.einlesenListe(text, sepDec, sepVal)
            self.showPoints(system, self.__dict_PLQuelle)
        else:
            self.__dict_PLZiel.einlesenListe(text, sepDec, sepVal)
            self.showPoints(system, self.__dict_PLZiel)


    def showPoints(self, system, dicP):
        if system == 0:
            self.fillTree(self.punktListSource, dicP)
        elif system == 1:
            self.fillTree(self.punktListDest, dicP)
        else:
            self.fillTree(self.punktListTrans,dicP)

    def fillTree(self, treename, dicP):
        treename.delete(*treename.get_children())
        dP = dicP.get_dic()
        keys = list(dP.keys())
        if treename == self.punktListTrans:
            for i in range(len(dP)):
                id = keys[i]
                if "w" in dP[id]:
                    treename.insert("",i+1,text=id, values=(dP[id]["Punkt"].get_y(), dP[id]["Punkt"].get_x(), \
                        dP[id]["w"]["y"].länge(), dP[id]["w"]["x"].länge() ))
                else:
                    treename.insert("",i+1,text=id, values=(dP[id]["Punkt"].get_y(), dP[id]["Punkt"].get_x()))
        else:
            for i in range(len(dP)):
                id = keys[i]
                treename.insert("",i+1,text=id, values=(dP[id].get_y(), dP[id].get_x()))


    def BtnPressedLoadPoints(self):
        top = Toplevel()
        top.title("Punkte laden")
        self.F_loadPList = Fenster_loadPList(top, self)
        

    def BtnPressedCalc(self):
        ht = HelmertTrans(self.__dict_PLQuelle, self.__dict_PLZiel)
        punkte, parameter = ht.get_result()
        self.showPoints(2, punkte)
        self.__dict_PLTrans.set_dic(punkte)

        self.dblParaM.set(parameter["m"])
        self.dblParaRot.set(parameter["epsilon"])
        self.dblParaTransY.set(parameter["Y0"])
        self.dblParaTransX.set(parameter["X0"])




if __name__ == "__main__":

    root = Tk()
    root.title("Transformationen")
    root.geometry
    appTrans = FensterTrans(root,root)
    appTrans.mainloop()

