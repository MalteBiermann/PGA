from tkinter import Frame,Tk,Button,Toplevel,Radiobutton,IntVar,StringVar,DoubleVar,LabelFrame,Entry,Label,Scrollbar,filedialog
from tkinter.ttk import Treeview

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from gui.template import GuiTemplate
from operation.polygonzug import Polygonzug
from datentyp.punkt import Punkt_Dic



class FensterPZ(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        # self.__polygonzug = Polygonzug()

        tv_column_width_id = 40
        tv_column_width = 120
        tv_column_width_min = 100
        self.radioPolygonType = IntVar(value=0)

        self.str_sepDec = StringVar(value=".")
        self.str_sepVal = StringVar(value=",")

        self.str_StnName = StringVar()
        self.dbl_Beta = DoubleVar()
        self.dbl_T = DoubleVar()
        self.dbl_Sahead = DoubleVar()
        self.dbl_Y = DoubleVar()
        self.dbl_X = DoubleVar()
        self.dbl_Wbeta = DoubleVar()
        self.dbl_Wy = DoubleVar()
        self.dbl_Wx = DoubleVar()

        lf_PolygonType = LabelFrame(self, text="Polygonart")
        lf_PolygonType.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Radiobutton(lf_PolygonType,text="Polygonzug beidseitig in Richtung und Lage angeschlossen", variable=self.radioPolygonType, value=0).grid(row=0, column=0, padx=3, pady=3,sticky="w")
        Radiobutton(lf_PolygonType,text="Ringpolygon", variable=self.radioPolygonType, value=1).grid(row=1, column=0, padx=3, pady=3,sticky="w")
        
        lf_OpenFile = LabelFrame(self,text=".CSV laden")
        lf_OpenFile.grid(row=0, column=1, padx=3, pady=3)
        lf_Sep = LabelFrame(lf_OpenFile, text="Trennzeichen")
        lf_Sep.grid(row=0, column=1, padx=3, pady=3)
        Label(lf_Sep,text="Werte").grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Label(lf_Sep,text="Dezimal").grid(row=1, column=0, padx=3, pady=3, sticky="w")
        Entry(lf_Sep, textvariable=self.str_sepVal, width=3).grid(row=0, column=1, padx=3, pady=3)
        Entry(lf_Sep, textvariable=self.str_sepDec, width=3).grid(row=1, column=1, padx=3, pady=3)

        Button(lf_OpenFile,text="Suche Datei", command=self.BtnPressedLoadPoints).grid(row=0, column=3, padx=3, pady=3, sticky="w")
        Button(self,text="Berechnen", command=self.BtnPressedCalc).grid(row=2, column=0, padx=3, pady=3, columnspan=1)

        lf_TVPoints = LabelFrame(self, text="Punktliste")
        lf_TVPoints.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=2)
        self.tv_points = Treeview(lf_TVPoints,selectmode="extended")
        self.tv_points.grid(row=0, column=0, padx=3, pady=3)
        self.tv_points["columns"] = ("beta","t","s","y", "x")
        self.tv_points.column("#0",width = tv_column_width_id, minwidth=tv_column_width_id)
        self.tv_points.column("beta",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_points.column("t",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_points.column("s",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_points.column("y",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_points.column("x",width = tv_column_width, minwidth=tv_column_width_min)
        self.tv_points.heading("#0",text="id")
        self.tv_points.heading("beta",text="beta")
        self.tv_points.heading("t",text="t")
        self.tv_points.heading("s",text="s")
        self.tv_points.heading("y",text="y")
        self.tv_points.heading("x",text="x")
        self.punktListScroll = Scrollbar(lf_TVPoints,orient="vertical", command=self.tv_points.yview)
        self.punktListScroll.grid(row=0, column=1, sticky="nse")
        self.tv_points.configure(yscrollcommand=self.punktListScroll.set)

        lf_Parameter = LabelFrame(self, text="Parameter")
        lf_Parameter.grid(row=2, column=1, padx=3, pady=3, sticky="", columnspan=3)
        Label(lf_Parameter,text="w_beta / gon").grid(row=0, column=0, padx=3, pady=3)
        Entry(lf_Parameter, textvariable=self.dbl_Wbeta,state="readonly").grid(row=0, column=1, padx=3, pady=3)
        Label(lf_Parameter,text="w_y").grid(row=1, column=0, padx=3, pady=3)
        Entry(lf_Parameter, textvariable=self.dbl_Wy,state="readonly").grid(row=1, column=1, padx=3, pady=3)
        Label(lf_Parameter,text="w_x").grid(row=2, column=0, padx=3, pady=3)
        Entry(lf_Parameter, textvariable=self.dbl_Wx,state="readonly").grid(row=2, column=1, padx=3, pady=3)

    def BtnPressedCalc(self):
        if self.radioPolygonType.get() == 0:
            self.__polygonzug.berechnePolygonzug()
        else:
            self.__polygonzug.berechneRingpolygon()
        self.showPoints()

    def BtnPressedLoadPoints(self):
        try:
            filePath = filedialog.askopenfilename(filetypes =[('CSV', '*.csv'),('*', '*.*')])
        except:
            pass
        if filePath:
            self.__polygonzug = Polygonzug()
            self.__polygonzug.readFile(filePath,self.str_sepDec.get(), self.str_sepVal.get())
            self.showPoints()

    def showPoints(self):
        for row in self.tv_points.get_children():
            self.tv_points.delete(row)
        dic_Polygon = self.__polygonzug.get_polygon().get_pDic()
        l_Polygon = self.__polygonzug.get_polygon().get_pIdList()

        for i in range(len(l_Polygon)):
            pId = l_Polygon[i]
            keys = dic_Polygon[pId].keys()
            if "beta" in keys:
                beta = dic_Polygon[pId]["beta"].get_w("gon")
            else:
                beta = ""
            if "r" in keys:
                t = dic_Polygon[pId]["r"].get_w("gon")
            else:
                t = ""
            if "s_vor" in keys:
                s = dic_Polygon[pId]["s_vor"].länge()
            else:
                s = ""
            y = dic_Polygon[pId]["coord"].get_y()
            x = dic_Polygon[pId]["coord"].get_x()
            self.tv_points.insert("",i+1,text=pId,values=(beta,t,s,y,x))
        self.dbl_Wbeta.set(self.__polygonzug.get_parameter()["w_beta"].get_w("gon"))
        self.dbl_Wx.set(self.__polygonzug.get_parameter()["w_x"])
        self.dbl_Wy.set(self.__polygonzug.get_parameter()["w_y"])
    


if __name__ == "__main__":
    pass
    root = Tk()
    root.title("Polygonzug")
    root.geometry
    app = FensterPZ(root)
    app.mainloop()