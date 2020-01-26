from tkinter import *

if __name__ == "__main__":
    import sys
    sys.path.append(".")
    
from operation.winkelrechner import *
from datentyp.punkt import Punkt
from datentyp.strecke import Strecke


class FensterHA(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.eingabeX1 = StringVar()
        self.eingabeY1 = StringVar()
        self.eingabeX2 = StringVar()
        self.eingabeY2 = StringVar()
        self.eingabeS = StringVar()
        self.eingabeT = StringVar()
        self.grid()

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

        Label(self, text="(Rechts) Y:").grid(row=1, column=0)
        Label(self, text="(Hoch) X:").grid(row=2, column=0)
        Label(self, text="Punkt A:").grid(row=0, column=1)
        Label(self, text="Punkt B:").grid(row=0, column=4)
        Label(self, text="Winkel t / gon:").grid(row=0, column=3)
        Label(self, text="Strecke s:").grid(row=0, column=2)

        Button(self, text="Berechne 1. Hauptaufgabe", command=self.btnBerechneErsteHAPressed).grid(
            row=3, column=0, padx=3, pady=3)
        Button(self, text="Berechne 2. Hauptaufgabe", command=self.btnBerechneZweiteHAPressed).grid(
            row=4, column=0, padx=3, pady=3)

        
        self.focus_set()
        self.grab_set()
        self.wait_window()

    def btnBerechneErsteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        t = gon2rad(float(self.eingabeT.get().replace(",", ".")))
        s = float(self.eingabeS.get().replace(",", "."))
        X2, Y2 = Punkt.erstegga(X1, Y1, s, t)
        self.eingabeX2.set(X2)
        self.eingabeY2.set(Y2)

    def btnBerechneZweiteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        Y2 = float(self.eingabeY2.get().replace(",", "."))
        X2 = float(self.eingabeX2.get().replace(",", "."))

        s = Strecke.init_koor(Y1, X1, Y2, X2)
        s, t = s.zweitegga()
        t = rad2gon(t)
        self.eingabeS.set(s)
        self.eingabeT.set(t)



if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Hauptaufgaben")
    #root.geometry("350x75")
    app = FensterHA(root)
    app.mainloop()