if __name__ == "__main__":
    import sys
    sys.path.append(".")

from tkinter import *

from gui.hauptaufgaben import *
from gui.winkelrechner import *
from gui.rückwärtsschnitt import *
from gui.rückwärtsschnitt import *


import hauptaufgaben

class HauptFenster(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.root = master

        self.grid()
        #Label(self, text="Geodätisches Gedöhns").grid(row=0, column=0)

        Button(self, text="Winkelrechner", command=self.openFensterWinkelrechner).grid(
            row=1, column=0, padx=3, pady=3)
        Button(self, text="Hauptaufgaben", command=self.openFensterGHA).grid(
            row=1, column=1, padx=3, pady=3)
        Button(self, text="Bogenschnitt", command=self.openFensterBS).grid(
            row=1, column=2, padx=3, pady=3)
        Button(self, text="Rückwärtsschnitt", command=self.openFensterRWS).grid(
            row=1, column=3, padx=3, pady=3)

    def openFensterWinkelrechner(self):
        top = Toplevel()
        top.title("Toolbox / Einheitenrechner")
        FensterWinkelrechner(top)

    def openFensterGHA(self):
        top = Toplevel()
        top.title("Toolbox / Geodätische Hauptaufgaben")
        FensterHA(top)

    def openFensterBS(self):
        top = Toplevel()
        top.title("Toolbox / Bogenschnitt")
        FensterBS(top)

    def openFensterRWS(self):
        top = Toplevel()
        top.title("Toolbox / Rückwärtsschnitt")
        FensterRWS(top)


if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Toolbox / Hauptfenster")
    #root.geometry("350x75")
    app = HauptFenster(root)
    app.mainloop()

