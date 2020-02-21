from tkinter import Frame,Tk,Button,Toplevel,StringVar,Label,Entry

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.vorwärtsschnitt import Vorwärtsschnitt
from datentyp.punkt import Punkt
from datentyp.winkel import Winkel
from gui.template import GuiTemplate


class FensterVS(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.str_1y = StringVar()
        self.str_1x = StringVar()
        self.str_2y = StringVar()
        self.str_2x = StringVar()
        self.str_3y = StringVar()
        self.str_3x = StringVar()
        self.str_4y = StringVar()
        self.str_4x = StringVar()
        self.str_Tphi = StringVar()
        self.str_Tpsi = StringVar()

        self.str_Ny = StringVar()
        self.str_Nx = StringVar()

        Label(self,text="Punkt 1").grid(row=0, column=2, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt 4").grid(row=0, column=4, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt 2").grid(row=0, column=6, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt 3").grid(row=0, column=8, padx=3, pady=3, columnspan=2)
        Label(self,text="Y").grid(row=1, column=0, padx=3, pady=3, columnspan=2)
        Label(self,text="X").grid(row=2, column=0, padx=3, pady=3, columnspan=2)
        Label(self,text="Winkel / gon").grid(row=4, column=0, padx=3, pady=3, columnspan=2)
        Label(self,text="t1,4,N").grid(row=3, column=3, padx=3, pady=3, columnspan=2)
        Label(self,text="t2,3,N").grid(row=3, column=7, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt N").grid(row=6, column=5, padx=3, pady=3, columnspan=2)
        Label(self,text="Y").grid(row=7, column=3, padx=3, pady=3, columnspan=2)
        Label(self,text="X").grid(row=8, column=3, padx=3, pady=3, columnspan=2)

        Entry(self, textvariable=self.str_1y).grid(row=1, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_1x).grid(row=2, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_4y).grid(row=1, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_4x).grid(row=2, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_2y).grid(row=1, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_2x).grid(row=2, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_3y).grid(row=1, column=8, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_3x).grid(row=2, column=8, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Tphi).grid(row=4, column=3, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Tpsi).grid(row=4, column=7, padx=3, pady=3, columnspan=2)

        Entry(self, textvariable=self.str_Ny, state="readonly").grid(row=7, column=5, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Nx, state="readonly").grid(row=8, column=5, padx=3, pady=3, columnspan=2)

        Button(self,text="Berechnen",command=self.BtnPressedCalc).grid(row=5, column=5, padx=3, pady=3, columnspan=2)

    def BtnPressedCalc(self):
        p1_y = float(self.str_1y.get().replace(",", "."))
        p1_x = float(self.str_1x.get().replace(",", "."))
        p2_y = float(self.str_2y.get().replace(",", "."))
        p2_x = float(self.str_2x.get().replace(",", "."))
        p3_y = float(self.str_3y.get().replace(",", "."))
        p3_x = float(self.str_3x.get().replace(",", "."))
        p4_y = float(self.str_4y.get().replace(",", "."))
        p4_x = float(self.str_4x.get().replace(",", "."))
        p1 = Punkt(p1_y,p1_x)
        p2 = Punkt(p2_y,p2_x)
        p3 = Punkt(p3_y,p3_x)
        p4 = Punkt(p4_y,p4_x)
        tPhi = Winkel(float(self.str_Tphi.get().replace(",", ".")),"gon")
        tPsi = Winkel(float(self.str_Tpsi.get().replace(",", ".")),"gon")
        pN = Vorwärtsschnitt(p1,p2,p3,p4,tPhi,tPsi).schneiden()
        self.str_Ny.set(self.runde(pN.get_y()))
        self.str_Nx.set(self.runde(pN.get_x()))


if __name__ == "__main__":
    root = Tk()
    root.title("Vorwärtsschnitt")
    root.geometry
    app = FensterVS(root)
    app.mainloop()