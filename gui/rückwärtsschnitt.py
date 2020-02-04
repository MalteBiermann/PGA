from tkinter import Tk,Button,StringVar,Entry,Label,Button,Radiobutton,IntVar

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.punkt import Punkt
from datentyp.winkel import Winkel
from operation.rückwärtsschnitt import Rückwärtsschnitt
from gui.template import GuiTemplate

class FensterRS(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.eingabeA_y = StringVar()
        self.eingabeA_x = StringVar()
        self.eingabeB_y = StringVar()
        self.eingabeB_x = StringVar()
        self.eingabeM_y = StringVar()
        self.eingabeM_x = StringVar()
        self.eingabeT_NA = StringVar()
        self.eingabeT_NB = StringVar()
        self.eingabeT_NM = StringVar()

        self.radioButtonSelection = IntVar()
        self.radioButtonSelection.set(1)

        self.eingabeAlpha = StringVar()
        self.eingabeBeta = StringVar()
        self.ausgabeN_y = StringVar()
        self.ausgabeN_x = StringVar()

        Label(self,text="Y").grid(row=1, column=0, padx=3, pady=3, columnspan=2)
        Label(self,text="X").grid(row=2, column=0, padx=3, pady=3, columnspan=2)

        Label(self,text="Punkt A").grid(row=0, column=2, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt M").grid(row=0, column=4, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt B").grid(row=0, column=6, padx=3, pady=3, columnspan=2)

        Label(self,text="Richtung / gon").grid(row=3, column=0, padx=3, pady=3)
        Label(self,text="Alpha").grid(row=4, column=3, padx=3, pady=3, columnspan=2)
        Label(self,text="Beta").grid(row=4, column=5, padx=3, pady=3 ,columnspan=2)
        Label(self,text="Winkel / gon").grid(row=5, column=0, padx=3, pady=3, columnspan=1)
        Label(self,text="Y").grid(row=8, column=2, padx=3, pady=3, columnspan=2)
        Label(self,text="X").grid(row=9, column=2, padx=3, pady=3, columnspan=2)
        Label(self,text="Punkt N").grid(row=7, column=4, padx=3, pady=3, columnspan=2)

        self.RBdir = Radiobutton(self, value=0, variable=self.radioButtonSelection, command=self.toggleEntry)
        self.RBdir.grid(row=3, column=1, padx=3, pady=3)
        self.RBangle = Radiobutton(self, value=1, variable=self.radioButtonSelection, command=self.toggleEntry)
        self.RBangle.grid(row=5, column=1, padx=3, pady=3)

        Entry(self, textvariable=self.eingabeA_y).grid(row=1, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeA_x).grid(row=2, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeM_y).grid(row=1, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeM_x).grid(row=2, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeB_y).grid(row=1, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.eingabeB_x).grid(row=2, column=6, padx=3, pady=3, columnspan=2)
        self.eInputT_NA = Entry(self, textvariable=self.eingabeT_NA, state="readonly")
        self.eInputT_NA.grid(row=3, column=2, padx=3, pady=3, columnspan=2)
        self.eInputT_NM = Entry(self, textvariable=self.eingabeT_NM, state="readonly")
        self.eInputT_NM.grid(row=3, column=4, padx=3, pady=3, columnspan=2)
        self.eInputT_NB = Entry(self, textvariable=self.eingabeT_NB, state="readonly")
        self.eInputT_NB.grid(row=3, column=6, padx=3, pady=3, columnspan=2)
        self.eInputAlpha = Entry(self, textvariable=self.eingabeAlpha)
        self.eInputAlpha.grid(row=5, column=3, padx=3, pady=3, columnspan=2)
        self.eInputBeta = Entry(self, textvariable=self.eingabeBeta)
        self.eInputBeta.grid(row=5, column=5, padx=3, pady=3, columnspan=2)

        Button(self,text="Berechnen",command=self.BtnPressedCalc).grid(row=6, column=4, padx=3, pady=3, columnspan=2)

        Entry(self, textvariable=self.ausgabeN_y, state="readonly").grid(row=8, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.ausgabeN_x, state="readonly").grid(row=9, column=4, padx=3, pady=3, columnspan=2)

    def BtnPressedCalc(self):
        A_y = float(self.eingabeA_y.get().replace(",", "."))
        A_x = float(self.eingabeA_x.get().replace(",", "."))
        B_y = float(self.eingabeB_y.get().replace(",", "."))
        B_x = float(self.eingabeB_x.get().replace(",", "."))
        M_y = float(self.eingabeM_y.get().replace(",", "."))
        M_x = float(self.eingabeM_x.get().replace(",", "."))
        pA = Punkt(A_y,A_x)
        pB = Punkt(B_y,B_x)
        pM = Punkt(M_y,M_x)

        if self.radioButtonSelection.get() == 0:
            t_NA = Winkel(float(self.eingabeT_NA.get().replace(",", ".")),"gon")
            t_NM = Winkel(float(self.eingabeT_NM.get().replace(",", ".")),"gon")
            t_NB = Winkel(float(self.eingabeT_NB.get().replace(",", ".")),"gon")
            pN = Rückwärtsschnitt.init_dir(pA,pB,pM,t_NA,t_NB,t_NM).schneiden()
        else:
            aAlpha = Winkel(float(self.eingabeAlpha.get().replace(",", ".")), "gon")
            aBeta = Winkel(float(self.eingabeBeta.get().replace(",", ".")), "gon")
            pN = Rückwärtsschnitt(pA,pB,pM,aAlpha,aBeta).schneiden()
        self.ausgabeN_y.set(pN.get_y())
        self.ausgabeN_x.set(pN.get_x())

    def toggleEntry(self):
        if self.radioButtonSelection.get() == 1:
            self.eInputAlpha.config(state="normal")
            self.eInputBeta.config(state="normal")
            self.eInputT_NA.config(state="readonly")
            self.eInputT_NM.config(state="readonly")
            self.eInputT_NB.config(state="readonly")
        else:
            self.eInputAlpha.config(state="readonly")
            self.eInputBeta.config(state="readonly")
            self.eInputT_NA.config(state="normal")
            self.eInputT_NM.config(state="normal")
            self.eInputT_NB.config(state="normal")


if __name__ == "__main__":
    self = Tk()
    self.title("Rückwärtseinschnitt")
    self.geometry
    appRS = FensterRS(self)
    appRS.mainloop()