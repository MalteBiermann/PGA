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

        self.str_Ay = StringVar()
        self.str_Ax = StringVar()
        self.str_By = StringVar()
        self.str_Bx = StringVar()
        self.str_My = StringVar()
        self.str_Mx = StringVar()
        self.str_TNA = StringVar()
        self.str_TNB = StringVar()
        self.str_TNM = StringVar()

        self.int_radioBSelect = IntVar(value=1)

        self.str_Alpha = StringVar()
        self.str_Beta = StringVar()
        self.str_Ny = StringVar()
        self.str_Nx = StringVar()

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

        self.RB_dir = Radiobutton(self, value=0, variable=self.int_radioBSelect, command=self.toggleEntry)
        self.RB_dir.grid(row=3, column=1, padx=3, pady=3)
        self.RB_angle = Radiobutton(self, value=1, variable=self.int_radioBSelect, command=self.toggleEntry)
        self.RB_angle.grid(row=5, column=1, padx=3, pady=3)

        Entry(self, textvariable=self.str_Ay).grid(row=1, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Ax).grid(row=2, column=2, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_My).grid(row=1, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Mx).grid(row=2, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_By).grid(row=1, column=6, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Bx).grid(row=2, column=6, padx=3, pady=3, columnspan=2)

        self.e_TNA = Entry(self, textvariable=self.str_TNA, state="readonly")
        self.e_TNA.grid(row=3, column=2, padx=3, pady=3, columnspan=2)
        self.e_TNM = Entry(self, textvariable=self.str_TNM, state="readonly")
        self.e_TNM.grid(row=3, column=4, padx=3, pady=3, columnspan=2)
        self.e_TNB = Entry(self, textvariable=self.str_TNB, state="readonly")
        self.e_TNB.grid(row=3, column=6, padx=3, pady=3, columnspan=2)
        self.e_Alpha = Entry(self, textvariable=self.str_Alpha)
        self.e_Alpha.grid(row=5, column=3, padx=3, pady=3, columnspan=2)
        self.e_Beta = Entry(self, textvariable=self.str_Beta)
        self.e_Beta.grid(row=5, column=5, padx=3, pady=3, columnspan=2)

        Button(self,text="Berechnen",command=self.BtnPressedCalc).grid(row=6, column=4, padx=3, pady=3, columnspan=2)

        Entry(self, textvariable=self.str_Ny, state="readonly").grid(row=8, column=4, padx=3, pady=3, columnspan=2)
        Entry(self, textvariable=self.str_Nx, state="readonly").grid(row=9, column=4, padx=3, pady=3, columnspan=2)

    def BtnPressedCalc(self):
        A_y = float(self.str_Ay.get().replace(",", "."))
        A_x = float(self.str_Ax.get().replace(",", "."))
        B_y = float(self.str_By.get().replace(",", "."))
        B_x = float(self.str_Bx.get().replace(",", "."))
        M_y = float(self.str_My.get().replace(",", "."))
        M_x = float(self.str_Mx.get().replace(",", "."))
        pA = Punkt(A_y,A_x)
        pB = Punkt(B_y,B_x)
        pM = Punkt(M_y,M_x)

        if self.int_radioBSelect.get() == 0:
            t_NA = Winkel(float(self.str_TNA.get().replace(",", ".")),"gon")
            t_NM = Winkel(float(self.str_TNM.get().replace(",", ".")),"gon")
            t_NB = Winkel(float(self.str_TNB.get().replace(",", ".")),"gon")
            self.str_Alpha.set("")
            self.str_Beta.set("")
            pN = Rückwärtsschnitt.init_dir(pA,pB,pM,t_NA,t_NB,t_NM).schneiden()
        else:
            aAlpha = Winkel(float(self.str_Alpha.get().replace(",", ".")), "gon")
            aBeta = Winkel(float(self.str_Beta.get().replace(",", ".")), "gon")
            self.str_TNA.set("")
            self.str_TNM.set("")
            self.str_TNB.set("")
            pN = Rückwärtsschnitt(pA,pB,pM,aAlpha,aBeta).schneiden()
        self.str_Ny.set(self.runde(pN.get_y()))
        self.str_Nx.set(self.runde(pN.get_x()))

    def toggleEntry(self):
        if self.int_radioBSelect.get() == 1:
            self.e_Alpha.config(state="normal")
            self.e_Beta.config(state="normal")
            self.e_TNA.config(state="readonly")
            self.e_TNM.config(state="readonly")
            self.e_TNB.config(state="readonly")
        else:
            self.e_Alpha.config(state="readonly")
            self.e_Beta.config(state="readonly")
            self.e_TNA.config(state="normal")
            self.e_TNM.config(state="normal")
            self.e_TNB.config(state="normal")


if __name__ == "__main__":
    self = Tk()
    self.title("Rückwärtseinschnitt")
    self.geometry
    appRS = FensterRS(self)
    appRS.mainloop()