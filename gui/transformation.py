from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Label,Entry,StringVar,Radiobutton,IntVar,DoubleVar,Scrollbar
from tkinter.ttk import Treeview
import json
from matplotlib import pyplot as plt
from matplotlib import use
use('TkAgg')

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.helmerttransformation import HelmertTrans
from operation.affintransformation import AffinTrans
from datentyp.punkt import Punkt_Dic
from gui.load_pointList import Fenster_loadPList
from gui.template import GuiTemplate
from datentyp.winkel import Winkel


class FensterTrans(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        tv_column_width_id = 50
        tv_column_width = 200
        tv_column_width_min = 200
        self.__pd_PLQuelle = Punkt_Dic()
        self.__pd_PLZiel = Punkt_Dic()
        self.__pd_PLTrans = Punkt_Dic()

        self.__dict_para = {}

        self.str_filePathSource = StringVar()
        self.str_filePathDest = StringVar()
        self.int_radioTrans = IntVar(value=0)

        self.dbl_ParaMY = DoubleVar()
        self.dbl_ParaMX = DoubleVar()
        self.dbl_ParaRotY = DoubleVar()
        self.dbl_ParaRotX = DoubleVar()
        self.dbl_ParaTransY = DoubleVar()
        self.dbl_ParaTransX = DoubleVar()

        lf_transType = LabelFrame(self, text="Ebene Transformationen")
        lf_transType.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        lf_Source = LabelFrame(self, text="Quellsystem")
        lf_Source.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=2)
        lf_Dest = LabelFrame(self, text="Zielsystem (Markierung: Nichtbeachtung des Passpunktes bei der Transformation)")
        lf_Dest.grid(row=1, column=3, padx=3, pady=3, sticky="w", columnspan=2)
        lf_Parameter = LabelFrame(self, text="Parameter")
        lf_Parameter.grid(row=2, column=2, padx=3, pady=3, sticky="", columnspan=3)
        lf_Trans = LabelFrame(self, text="Zielsystem / transformiert")
        lf_Trans.grid(row=4, column=0, padx=3, pady=3, sticky="",columnspan=4)

        Radiobutton(lf_transType,text="Helmerttransformation", variable=self.int_radioTrans, value=0)\
            .grid(row=0, column=0, padx=3, pady=3)
        Radiobutton(lf_transType,text="Affintransformation", variable=self.int_radioTrans, value=1)\
            .grid(row=0, column=1, padx=3, pady=3)
        Button(self,text="Lade Punkte",command=self.BtnPressedLoadPoints)\
            .grid(row=0, column=1, padx=3, pady=3, sticky="w")
        Button(self,text="Berechnen",command=self.BtnPressedCalc)\
            .grid(row=2, column=0, padx=3, pady=3, columnspan=1,sticky="e")
        Button(self,text="Zeige Grafik",command=self.BtnPressedPlot)\
            .grid(row=2, column=1, padx=3, pady=3, columnspan=1,sticky="w")

        self.tv_punktListSource = Treeview(lf_Source,selectmode="none")
        self.tv_punktListSource.grid(row=0, column=0, padx=3, pady=3)
        self.tv_punktListSource["columns"] = ("y", "x")
        self.tv_punktListSource.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.tv_punktListSource.column("y",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListSource.column("x",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListSource.heading("#0",text="id")
        self.tv_punktListSource.heading("y",text="y")
        self.tv_punktListSource.heading("x",text="x")
        self.scr_punktListSourceScroll = Scrollbar(lf_Source,orient="vertical", command=self.tv_punktListSource.yview)
        self.scr_punktListSourceScroll.grid(row=0, column=1, sticky="nse")
        self.tv_punktListSource.configure(yscrollcommand=self.scr_punktListSourceScroll.set)

        self.tv_punktListDest = Treeview(lf_Dest)
        self.tv_punktListDest.grid(row=0, column=0, padx=3, pady=3)
        self.tv_punktListDest["columns"] = ("Y", "X")
        self.tv_punktListDest.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.tv_punktListDest.column("Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListDest.column("X",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListDest.heading("#0",text="id")
        self.tv_punktListDest.heading("Y",text="Y")
        self.tv_punktListDest.heading("X",text="X")
        self.scr_punktListDestScroll = Scrollbar(lf_Dest,orient="vertical", command=self.tv_punktListDest.yview)
        self.scr_punktListDestScroll.grid(row=0, column=1, sticky="nse")
        self.tv_punktListDest.configure(yscrollcommand=self.scr_punktListDestScroll.set)

        Label(lf_Parameter,text="Maßstab Y").grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Label(lf_Parameter,text="Maßstab X").grid(row=0, column=3, padx=3, pady=3, sticky="e")
        Label(lf_Parameter,text="Rotation Y / gon").grid(row=1, column=0, padx=3, pady=3, sticky="w")
        Label(lf_Parameter,text="Rotation X / gon").grid(row=1, column=3, padx=3, pady=3, sticky="e")
        Label(lf_Parameter,text="Translation Y").grid(row=2, column=0, padx=3, pady=3, sticky="w")
        Label(lf_Parameter,text="Translation X").grid(row=2, column=3, padx=3, pady=3, sticky="e")

        Entry(lf_Parameter,textvariable=self.dbl_ParaMY,state="readonly").grid(row=0, column=1, padx=3, pady=3)
        Entry(lf_Parameter,textvariable=self.dbl_ParaMX,state="readonly").grid(row=0, column=2, padx=3, pady=3)
        Entry(lf_Parameter,textvariable=self.dbl_ParaRotY,state="readonly").grid(row=1, column=1, padx=3, pady=3)
        Entry(lf_Parameter,textvariable=self.dbl_ParaRotX,state="readonly").grid(row=1, column=2, padx=3, pady=3)
        Entry(lf_Parameter,textvariable=self.dbl_ParaTransY,state="readonly").grid(row=2, column=1, padx=3, pady=3)
        Entry(lf_Parameter,textvariable=self.dbl_ParaTransX,state="readonly").grid(row=2, column=2, padx=3, pady=3)

        self.tv_punktListTrans = Treeview(lf_Trans,selectmode="none")
        self.tv_punktListTrans.grid(row=0, column=0, padx=3, pady=3)
        self.tv_punktListTrans["columns"] = ("Y", "X","Rk Y","Rk X")
        self.tv_punktListTrans.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.tv_punktListTrans.column("Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListTrans.column("X",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListTrans.column("Rk Y",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListTrans.column("Rk X",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_punktListTrans.heading("#0",text="id")
        self.tv_punktListTrans.heading("Y",text="Y")
        self.tv_punktListTrans.heading("X",text="X")
        self.tv_punktListTrans.heading("Rk Y",text="Restklaffe Y")
        self.tv_punktListTrans.heading("Rk X",text="Restklaffe X")
        self.scr_punktListTransScroll = Scrollbar(lf_Trans,orient="vertical", command=self.tv_punktListTrans.yview)
        self.scr_punktListTransScroll.grid(row=0, column=1, sticky="nse")
        self.tv_punktListTrans.configure(yscrollcommand=self.scr_punktListTransScroll.set)

    def loadPoints(self, text, sepDec, sepVal, systemtype):
        if systemtype == 0:
            self.__pd_PLQuelle.clear()
            self.__pd_PLQuelle.einlesenListe(text, sepDec, sepVal)
            self.showPoints(systemtype, self.__pd_PLQuelle)
        else:
            self.__pd_PLZiel.clear()
            self.__pd_PLZiel.einlesenListe(text, sepDec, sepVal)
            self.showPoints(systemtype, self.__pd_PLZiel)

    def showPoints(self, systemtype, dP):
        if systemtype == 0:
            self.fillTree(self.tv_punktListSource, dP)
        elif systemtype == 1:
            self.fillTree(self.tv_punktListDest, dP)
        else:
            self.fillTree(self.tv_punktListTrans,dP)

    def showParam(self, parameter):
        self.dbl_ParaMY.set(self.runde(parameter["m_Y"]))
        self.dbl_ParaRotY.set(self.runde(Winkel(parameter["rot_Y"],"rad").get_w("gon")))
        self.dbl_ParaTransY.set(self.runde(parameter["Y0"]))
        self.dbl_ParaTransX.set(self.runde(parameter["X0"]))
        if "m_X" in parameter:
            self.dbl_ParaMX.set(self.runde(parameter["m_X"]))
            self.dbl_ParaRotX.set(self.runde(Winkel(parameter["rot_X"],"rad").get_w("gon")))
        else:
            self.dbl_ParaMX.set(self.runde(parameter["m_Y"]))
            self.dbl_ParaRotX.set(self.runde(Winkel(parameter["rot_Y"],"rad").get_w("gon")))

    def fillTree(self, treename, dP):
        for row in treename.get_children():
            treename.delete(row)
        dP = dP.get_dic()
        keys = list(dP.keys())
        for i in range(len(dP)):
            pId = keys[i]
            y =  self.runde(dP[pId]["coord"].get_y())
            x =  self.runde(dP[pId]["coord"].get_x())
            if "w" in dP[pId]:
                wy = self.runde(dP[pId]["w"].get_y())
                wx = self.runde(dP[pId]["w"].get_x())
                treename.insert("",i+1,text=pId, values=(y, x, wy, wx))
            else:
                treename.insert("",i+1,text=pId, values=(y, x))

    def BtnPressedLoadPoints(self):
        top = Toplevel()
        top.title("Punkte laden")
        self.F_loadPList = Fenster_loadPList(top, self)

    def BtnPressedCalc(self):
        l_p1exclude = []
        for i in self.tv_punktListDest.selection():
            l_p1exclude.append(self.tv_punktListDest.item(i,"text"))
        if self.int_radioTrans.get() == 0:
            self.__pd_PLTrans, self.__dict_para = HelmertTrans(self.__pd_PLQuelle, self.__pd_PLZiel, l_p1exclude).get_result()
        else:
            self.__pd_PLTrans, self.__dict_para = AffinTrans(self.__pd_PLQuelle, self.__pd_PLZiel, l_p1exclude).get_result()
        self.showPoints(2, self.__pd_PLTrans)
        self.showParam(self.__dict_para)

    def load_json(self,s):
        pDic = json.loads(s)
        for k,v in pDic.items():
            if k == "source":
                self.__pd_PLQuelle.from_json(v)
            elif k == "dest":
                self.__pd_PLZiel.from_json(v)
            elif k == "trans":
                self.__pd_PLTrans.from_json(v)
            elif k == "parameter":
                self.__dict_para = v
        
        self.showPoints(0, self.__pd_PLQuelle)
        self.showPoints(1, self.__pd_PLZiel)
        self.showPoints(2, self.__pd_PLTrans)
        self.showParam(self.__dict_para)

    def save_json(self):
        return json.dumps({"source":self.__pd_PLQuelle.get_json(), "dest":self.__pd_PLZiel.get_json(),
                          "trans":self.__pd_PLTrans.get_json(), "parameter":self.__dict_para}, default=lambda obj: obj.get_json(),
                          sort_keys=True, indent=4)

    def BtnPressedPlot(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_aspect("equal")

        pl_plot = []
        for k in self.__pd_PLTrans.get_dic().values():
            pl_plot.append(k)
        
        l_y = []
        l_x = []
        l_id = []
        for p in pl_plot:
            l_y.append(p["coord"].get_y())
            l_x.append(p["coord"].get_x())
            l_id.append(p["coord"].get_id())

        for i in range(len(l_y)):
            ax.text(l_y[i]+10, l_x[i]+10, l_id[i])

        plt.plot(l_y,l_x, '.', color='black')

        ax.relim()
        ax.autoscale_view()
        ax.set_xlabel("Y")
        ax.set_ylabel("X")
        ax.grid(True)
        plt.show()


if __name__ == "__main__":
    self = Tk()
    self.title("Transformationen")
    self.geometry
    appTrans = FensterTrans(self)
    appTrans.mainloop()

