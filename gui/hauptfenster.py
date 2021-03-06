from tkinter import Frame,Tk,Button,Toplevel,Label
from tkinter.ttk import Separator

if __name__ == "__main__":
    import sys
    sys.path.append(".")

import gui.winkelrechner
import gui.rückwärtsschnitt
import gui.vorwärtsschnitt
import gui.hauptaufgaben
import gui.bogenschnitt
import gui.transformation
import gui.polygonzug

class HauptFenster(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        Button(self, text="Winkelrechner", command=self.openFensterWinkelrechner, width=15).grid(
            row=1, column=0, padx=3, pady=3, sticky="w")
        Button(self, text="Hauptaufgaben", command=self.openFensterHA, width=15).grid(
            row=2, column=0, padx=3, pady=3, sticky="w")
        Button(self, text="Bogenschnitt", command=self.openFensterBS, width=15).grid(
            row=3, column=0, padx=3, pady=3, sticky="w")
        Button(self, text="Rückwärtsschnitt", command=self.openFensterRS, width=15).grid(
            row=3, column=1, padx=3, pady=3, sticky="w")
        Button(self, text="Vorwärtsschnitt", command=self.openFensterVS, width=15).grid(
            row=3, column=2, padx=3, pady=3, sticky="w")
        Button(self, text="Polygonzug", command=self.openFensterPZ, width=15).grid(
            row=4, column=0, padx=3, pady=3, sticky="w")
        Button(self, text="Transformation", command=self.openFensterTrans, width=15).grid(
            row=5, column=0, padx=3, pady=3, sticky="w")
        
        Separator(self,orient="horizontal").grid(
            row=6, column=0, padx=3, pady=3, columnspan=3, sticky="we")
        
        Label(self, text="Svenja Rode, Chris Arends, Hendrik Gebben und Malte Biermann").grid(
            row=7, column=0, padx=3, pady=3, columnspan=3, sticky="")

    def openFensterWinkelrechner(self):
        top = Toplevel()
        top.title("Toolbox / Einheitenrechner")
        gui.winkelrechner.FensterWinkelrechner(top)

    def openFensterHA(self):
        top = Toplevel()
        top.title("Toolbox / Geodätische Hauptaufgaben")
        #FensterHA(top)
        gui.hauptaufgaben.FensterHA(top)

    def openFensterBS(self):
        top = Toplevel()
        top.title("Toolbox / Bogenschnitt")
        gui.bogenschnitt.FensterBS(top)

    def openFensterRS(self):
        top = Toplevel()
        top.title("Toolbox / Rückwärtsschnitt")
        gui.rückwärtsschnitt.FensterRS(top)

    def openFensterVS(self):
        top = Toplevel()
        top.title("Toolbox / Vorwärtsschnitt")
        gui.vorwärtsschnitt.FensterVS(top)

    def openFensterPZ(self):
        top = Toplevel()
        top.title("Toolbox / Polygonzug")
        gui.polygonzug.FensterPZ(top)
    
    def openFensterTrans(self):
        top = Toplevel()
        top.title("Toolbox / Transformation")
        gui.transformation.FensterTrans(top)


if __name__ == "__main__":

    root = Tk()
    root.title("Geodätische Toolbox")
    #root.geometry("350x75")
    app = HauptFenster(root)
    app.mainloop()
