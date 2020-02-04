from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Label,Entry,StringVar,Radiobutton,IntVar,DoubleVar,Scrollbar
from tkinter.ttk import Treeview

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.helmerttransformation import HelmertTrans
from operation.affintransformation import AffinTrans
from datentyp.punkt import Punkt_Dic
from gui.load_pointList import Fenster_loadPList

class FensterTrans(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        tv_column_width_id = 50
        tv_column_width = 200
        tv_column_width_min = 200
        self.__dict_PLQuelle = Punkt_Dic()
        self.__dict_PLZiel = Punkt_Dic()
        self.__dict_PLTrans = Punkt_Dic()

        self.filePathSource = StringVar()
        self.filePathDest = StringVar()
        self.radioTrans = IntVar(value=0)

        self.dblParaM_Y = DoubleVar()
        self.dblParaM_X = DoubleVar()
        self.dblParaRot_Y = DoubleVar()
        self.dblParaRot_X = DoubleVar()
        self.dblParaTrans_Y = DoubleVar()
        self.dblParaTrans_X = DoubleVar()

        lfTransType = LabelFrame(self, text="Ebene Transformationen")
        lfTransType.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        lfSource = LabelFrame(self, text="Quellsystem")
        lfSource.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=2)
        lfDest = LabelFrame(self, text="Zielsystem (Markierung = Nichtbeachtung des Passpunktes)")
        lfDest.grid(row=1, column=2, padx=3, pady=3, sticky="w", columnspan=2)
        lfParameter = LabelFrame(self, text="Parameter")
        lfParameter.grid(row=2, column=1, padx=3, pady=3, sticky="", columnspan=3)
        lfTrans = LabelFrame(self, text="Zielsystem / transformiert")
        lfTrans.grid(row=4, column=0, padx=3, pady=3, sticky="",columnspan=4)

        Radiobutton(lfTransType,text="Helmerttransformation", variable=self.radioTrans, value=0).grid(row=0, column=0, padx=3, pady=3)
        Radiobutton(lfTransType,text="Affintransformation", variable=self.radioTrans, value=1).grid(row=0, column=1, padx=3, pady=3)
        Button(self,text="Lade Punkte",command=self.BtnPressedLoadPoints).grid(row=0, column=1, padx=3, pady=3, sticky="w")
        Button(self,text="Berechnen",command=self.BtnPressedCalc).grid(row=2, column=0, padx=3, pady=3, columnspan=1)

        self.punktListSource = Treeview(lfSource,selectmode="none")
        self.punktListSource.grid(row=0, column=0, padx=3, pady=3)
        self.punktListSource["columns"] = ("y", "x")
        self.punktListSource.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.punktListSource.column("y",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListSource.column("x",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListSource.heading("#0",text="id")
        self.punktListSource.heading("y",text="y")
        self.punktListSource.heading("x",text="x")
        self.punktListSourceScroll = Scrollbar(lfSource,orient="vertical", command=self.punktListSource.yview)
        self.punktListSourceScroll.grid(row=0, column=1, sticky="nse")
        self.punktListSource.configure(yscrollcommand=self.punktListSourceScroll.set)

        self.punktListDest = Treeview(lfDest)
        self.punktListDest.grid(row=0, column=0, padx=3, pady=3)
        self.punktListDest["columns"] = ("Y", "X")
        self.punktListDest.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.punktListDest.column("Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListDest.column("X",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListDest.heading("#0",text="id")
        self.punktListDest.heading("Y",text="Y")
        self.punktListDest.heading("X",text="X")
        self.punktListDestScroll = Scrollbar(lfDest,orient="vertical", command=self.punktListDest.yview)
        self.punktListDestScroll.grid(row=0, column=1, sticky="nse")
        self.punktListDest.configure(yscrollcommand=self.punktListDestScroll.set)

        Label(lfParameter,text="Maßstab Y").grid(row=0, column=0, padx=3, pady=3,)
        Label(lfParameter,text="Maßstab X").grid(row=1, column=0, padx=3, pady=3,)
        Label(lfParameter,text="Rotation Y").grid(row=0, column=2, padx=3, pady=3,)
        Label(lfParameter,text="Rotation X").grid(row=1, column=2, padx=3, pady=3,)
        Label(lfParameter,text="Translation Y").grid(row=0, column=4, padx=3, pady=3,)
        Label(lfParameter,text="Translation X").grid(row=1, column=4, padx=3, pady=3,)

        Entry(lfParameter,textvariable=self.dblParaM_Y,state="readonly").grid(row=0, column=1, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaM_X,state="readonly").grid(row=1, column=1, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaRot_Y,state="readonly").grid(row=0, column=3, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaRot_X,state="readonly").grid(row=1, column=3, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaTrans_Y,state="readonly").grid(row=0, column=5, padx=3, pady=3,)
        Entry(lfParameter,textvariable=self.dblParaTrans_X,state="readonly").grid(row=1, column=5, padx=3, pady=3,)

        self.punktListTrans = Treeview(lfTrans,selectmode="none")
        self.punktListTrans.grid(row=0, column=0, padx=3, pady=3)
        self.punktListTrans["columns"] = ("Y", "X","Rk Y","Rk X")
        self.punktListTrans.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.punktListTrans.column("Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListTrans.column("X",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListTrans.column("Rk Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListTrans.column("Rk X",width = tv_column_width, minwidth=tv_column_width_min)
        self.punktListTrans.heading("#0",text="id")
        self.punktListTrans.heading("Y",text="Y")
        self.punktListTrans.heading("X",text="X")
        self.punktListTrans.heading("Rk Y",text="Restklaffe Y")
        self.punktListTrans.heading("Rk X",text="Restklaffe X")
        self.punktListTransScroll = Scrollbar(lfTrans,orient="vertical", command=self.punktListTrans.yview)
        self.punktListTransScroll.grid(row=0, column=1, sticky="nse")
        self.punktListTrans.configure(yscrollcommand=self.punktListTransScroll.set)

    def loadPoints(self, text, sepDec, sepVal, system):
        if system == 0:
            self.__dict_PLQuelle.clear()
            self.__dict_PLQuelle.einlesenListe(text, sepDec, sepVal)
            self.showPoints(system, self.__dict_PLQuelle)
        else:
            self.__dict_PLZiel.clear()
            self.__dict_PLZiel.einlesenListe(text, sepDec, sepVal)
            self.showPoints(system, self.__dict_PLZiel)

    def showPoints(self, system, dicP):
        if system == 0:
            self.fillTree(self.punktListSource, dicP)
        elif system == 1:
            self.fillTree(self.punktListDest, dicP)
        else:
            self.fillTree(self.punktListTrans,dicP)

    def showParam(self,parameter):
        self.dblParaM_Y.set(parameter["m_Y"])
        self.dblParaRot_Y.set(parameter["rot_Y"])
        self.dblParaTrans_Y.set(parameter["Y0"])
        self.dblParaTrans_X.set(parameter["X0"])
        if "m_X" in parameter:
            self.dblParaM_X.set(parameter["m_X"])
            self.dblParaRot_X.set(parameter["rot_X"])
        else:
            self.dblParaM_X.set(parameter["m_Y"])
            self.dblParaRot_X.set(parameter["rot_Y"])

    def fillTree(self, treename, dicP):
        for row in treename.get_children():
            treename.delete(row)
        dP = dicP.get_dic()
        keys = list(dP.keys())
        if treename == self.punktListTrans:
            for i in range(len(dP)):
                id = keys[i]
                if "w" in dP[id]:
                    treename.insert("",i+1,text=id, values=(dP[id]["coord"].get_y(), dP[id]["coord"].get_x(), \
                        dP[id]["w"]["y"].länge(), dP[id]["w"]["x"].länge() ))
                else:
                    treename.insert("",i+1,text=id, values=(dP[id]["coord"].get_y(), dP[id]["coord"].get_x()))
        else:
            for i in range(len(dP)):
                id = keys[i]
                treename.insert("",i+1,text=id, values=(dP[id]["coord"].get_y(), dP[id]["coord"].get_x()))

    def BtnPressedLoadPoints(self):
        top = Toplevel()
        top.title("Punkte laden")
        self.F_loadPList = Fenster_loadPList(top, self)

    def BtnPressedCalc(self):
        l_p1exclude = []
        for i in self.punktListDest.selection():
            l_p1exclude.append(self.punktListDest.item(i,"text"))
        if self.radioTrans.get() == 0:
            punkte, parameter = HelmertTrans(self.__dict_PLQuelle, self.__dict_PLZiel, l_p1exclude).get_result()
        else:
            punkte, parameter = AffinTrans(self.__dict_PLQuelle, self.__dict_PLZiel, l_p1exclude).get_result()
        self.showPoints(2, punkte)
        self.__dict_PLTrans.set_dic(punkte)
        self.showParam(parameter)


if __name__ == "__main__":
    self = Tk()
    self.title("Transformationen")
    self.geometry
    appTrans = FensterTrans(self)
    appTrans.mainloop()

