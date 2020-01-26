# Biermann, Malte
# Matr.-Nr.: 5013167
# 2019-09-26

from tkinter import *
from gui.hauptaufgaben import *
from gui.winkelrechner import *


class HauptFenster(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.root = master

        self.grid()
        Label(self, text="Geodätisches Gedöhns").grid(row=0, column=0)

        Button(self, text="Winkelrechner", command=self.openWinEinheitenrechner).grid(
            row=1, column=0, padx=3, pady=3)
        Button(self, text="Hauptaufgaben", command=self.openWinGGA).grid(
            row=1, column=1, padx=3, pady=3)
        Button(self, text="Bogenschnitt", command=self.openWinBS).grid(
            row=1, column=2, padx=3, pady=3)
        Button(self, text="Rückwärtsschnitt", command=self.openWinRWS).grid(
            row=1, column=3, padx=3, pady=3)

    def openWinEinheitenrechner(self):
        top = Toplevel()
        top.title("Toolbox / Einheitenrechner")
        WinEinheitenrechner = FensterWinkelrechner(top)

    def openWinGGA(self):
        top = Toplevel()
        top.title("Toolbox / Geodätische Hauptaufgaben")
        WinHauptaufgabe = FensterGeoGA(top)

    def openWinBS(self):
        top = Toplevel()
        top.title("Toolbox / Bogenschnitt")
        WinBogenschnitt = FensterBS(top)

    def openWinRWS(self):
        top = Toplevel()
        top.title("Toolbox / Rückwärtsschnitt")
        WinRWschnitt = FensterRWS(top)


if __name__ == "__main__":

    root = Tk()
    root.title("Toolbox / Hauptfenster")
    root.geometry("350x75")
    app = HauptFenster(root)
    app.mainloop()
