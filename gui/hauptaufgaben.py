from tkinter import Tk, Entry, StringVar, Frame, Label, Button

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import Winkel
from datentyp.strecke import Strecke
from datentyp.punkt import Punkt
from gui.template import GuiTemplate

class FensterHA(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.eingabeX1 = StringVar()
        self.eingabeY1 = StringVar()
        self.eingabeX2 = StringVar()
        self.eingabeY2 = StringVar()
        self.eingabeS = StringVar()
        self.eingabeT = StringVar()

        Entry(self, textvariable=self.eingabeY1).grid(
            row=1, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeX1).grid(
            row=2, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeY2).grid(
            row=1, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeX2).grid(
            row=2, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeS).grid(
            row=1, column=2, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeT).grid(
            row=1, column=3, padx=3, pady=3)

        Label(self, text="Y").grid(row=1, column=0)
        Label(self, text="X").grid(row=2, column=0)
        Label(self, text="Punkt 1").grid(row=0, column=1)
        Label(self, text="Punkt 2").grid(row=0, column=4)
        Label(self, text="Winkel t / gon").grid(row=0, column=3)
        Label(self, text="Strecke s").grid(row=0, column=2)

        Button(self, text="Berechne 1. Hauptaufgabe -> P2", command=self.btnBerechneErsteHAPressed).grid(
            row=3, column=0, padx=3, pady=3, columnspan=3)
        Button(self, text="Berechne 2. Hauptaufgabe -> t,s", command=self.btnBerechneZweiteHAPressed).grid(
            row=3, column=3, padx=3, pady=3, columnspan=3)

    def btnBerechneErsteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        t = Winkel(float(self.eingabeT.get().replace(",", ".")), "gon")
        s = Strecke.init_länge(float(self.eingabeS.get().replace(",", ".")))
        P2 = Punkt.ersteHA(Punkt(X1, Y1), s, t)
        self.eingabeX2.set(self.runde(P2.get_x()))
        self.eingabeY2.set(self.runde(P2.get_y()))

    def btnBerechneZweiteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        Y2 = float(self.eingabeY2.get().replace(",", "."))
        X2 = float(self.eingabeX2.get().replace(",", "."))
        s = Strecke.init_koor(Y1, X1, Y2, X2)
        s, t = s.zweiteHA()
        t = t.get_w("gon")
        self.eingabeS.set(self.runde(s))
        self.eingabeT.set(self.runde(t))


if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Hauptaufgaben")
    app = FensterHA(root)
    app.mainloop()
