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

        self.str_x1 = StringVar()
        self.str_y1 = StringVar()
        self.str_x2 = StringVar()
        self.str_y2 = StringVar()
        self.str_s = StringVar()
        self.str_t = StringVar()

        Entry(self, textvariable=self.str_y1).grid(
            row=1, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.str_x1).grid(
            row=2, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.str_y2).grid(
            row=1, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.str_x2).grid(
            row=2, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.str_s).grid(
            row=1, column=2, padx=3, pady=3)
        Entry(self, textvariable=self.str_t).grid(
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
        Y1 = float(self.str_y1.get().replace(",", "."))
        X1 = float(self.str_x1.get().replace(",", "."))
        t = Winkel(float(self.str_t.get().replace(",", ".")), "gon")
        s = Strecke.init_länge(float(self.str_s.get().replace(",", ".")))
        P2 = Punkt.ersteHA(Punkt(X1, Y1), s, t)
        self.str_x2.set(self.runde(P2.get_x()))
        self.str_y2.set(self.runde(P2.get_y()))

    def btnBerechneZweiteHAPressed(self):
        Y1 = float(self.str_y1.get().replace(",", "."))
        X1 = float(self.str_x1.get().replace(",", "."))
        Y2 = float(self.str_y2.get().replace(",", "."))
        X2 = float(self.str_x2.get().replace(",", "."))
        s = Strecke.init_koor(Y1, X1, Y2, X2)
        s, t = s.zweiteHA()
        t = t.get_w("gon")
        self.str_s.set(self.runde(s))
        self.str_t.set(self.runde(t))


if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Hauptaufgaben")
    app = FensterHA(root)
    app.mainloop()
