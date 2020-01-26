from tkinter import *

if __name__ == "__main__":
    import sys
    sys.path.append(".")
    
from operation.winkelrechner import *


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

        Label(self, text="Y:").grid(row=1, column=0)
        Label(self, text="X:").grid(row=2, column=0)
        Label(self, text="A:").grid(row=0, column=1)
        Label(self, text="B:").grid(row=0, column=4)
        Label(self, text="t:").grid(row=0, column=3)
        Label(self, text="s:").grid(row=0, column=2)

        Button(self, text="Berechne 1. GeoGA", command=self.btnBerechneErsteHAPressed).grid(
            row=3, column=0, padx=3, pady=3)
        Button(self, text="Berechne 2. GeoGA", command=self.btnBerechneZweiteHAPressed).grid(
            row=4, column=0, padx=3, pady=3)

        
        self.focus_set()
        self.grab_set()
        self.wait_window()

    def btnBerechneErsteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        t = gon2rad(float(self.eingabeT.get().replace(",", ".")))
        s = float(self.eingabeS.get().replace(",", "."))
        X2, Y2 = erstegga(X1, Y1, s, t)
        self.eingabeX2.set(X2)
        self.eingabeY2.set(Y2)

    def btnBerechneZweiteHAPressed(self):
        Y1 = float(self.eingabeY1.get().replace(",", "."))
        X1 = float(self.eingabeX1.get().replace(",", "."))
        Y2 = float(self.eingabeY2.get().replace(",", "."))
        X2 = float(self.eingabeX2.get().replace(",", "."))

        s, t = zweitegga(Y1, X1, Y2, X2)
        t = rad2gon(t)
        self.eingabeS.set(s)
        self.eingabeT.set(t)



if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Hauptaufgaben")
    #root.geometry("350x75")
    app = FensterHA(root)
    app.mainloop()