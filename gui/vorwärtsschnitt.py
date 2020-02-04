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

        self.eingabe1_y = StringVar()
        self.eingabe1_x = StringVar()
        self.eingabe2_y = StringVar()
        self.eingabe2_x = StringVar()
        self.eingabe3_y = StringVar()
        self.eingabe3_x = StringVar()
        self.eingabe4_y = StringVar()
        self.eingabe4_x = StringVar()
        self.eingabeT_phi = StringVar()
        self.eingabeT_psi = StringVar()

        self.ausgabeN_y = StringVar()
        self.ausgabeN_x = StringVar()

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

        Entry(self, textvariable=self.eingabe1_y).grid(row=1, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe1_x).grid(row=2, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe4_y).grid(row=1, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe4_x).grid(row=2, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe2_y).grid(row=1, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe2_x).grid(row=2, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe3_y).grid(row=1, column=8, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabe3_x).grid(row=2, column=8, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeT_phi).grid(row=4, column=3, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeT_psi).grid(row=4, column=7, padx=3, pady=3, columnspan=2)

        Entry(self, textvariable=self.ausgabeN_y, state="readonly").grid(row=7, column=5, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.ausgabeN_x, state="readonly").grid(row=8, column=5, padx=3, pady=3, columnspan=2)

        Button(self,text="Berechnen",command=self.BtnPressedCalc).grid(row=5, column=5, padx=3, pady=3, columnspan=2)

    def BtnPressedCalc(self):
        p1_y = float(self.eingabe1_y.get().replace(",", "."))
        p1_x = float(self.eingabe1_x.get().replace(",", "."))
        p2_y = float(self.eingabe2_y.get().replace(",", "."))
        p2_x = float(self.eingabe2_x.get().replace(",", "."))
        p3_y = float(self.eingabe3_y.get().replace(",", "."))
        p3_x = float(self.eingabe3_x.get().replace(",", "."))
        p4_y = float(self.eingabe4_y.get().replace(",", "."))
        p4_x = float(self.eingabe4_x.get().replace(",", "."))
        p1 = Punkt(p1_y,p1_x)
        p2 = Punkt(p2_y,p2_x)
        p3 = Punkt(p3_y,p3_x)
        p4 = Punkt(p4_y,p4_x)
        tPhi = Winkel(float(self.eingabeT_phi.get().replace(",", ".")),"gon")
        tPsi = Winkel(float(self.eingabeT_psi.get().replace(",", ".")),"gon")
        pN = Vorwärtsschnitt(p1,p2,p3,p4,tPhi,tPsi).schneiden()
        self.ausgabeN_y.set(pN.get_y())
        self.ausgabeN_x.set(pN.get_x())


if __name__ == "__main__":
    root = Tk()
    root.title("Vorwärtsschnitt")
    root.geometry
    app = FensterVS(root)
    app.mainloop()