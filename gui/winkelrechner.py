from tkinter import Frame,Tk,Button,Toplevel,Entry,Label,StringVar,filedialog
import json

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from datentyp.winkel import Winkel
from gui.template import GuiTemplate

class FensterWinkelrechner(GuiTemplate):
    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.strEntryGrad = StringVar()
        self.strEntryRad = StringVar()
        self.strEntryGon = StringVar()

        Label(self, text="Grad").grid(row=0, column=0)
        Label(self, text="Rad").grid(row=1, column=0)
        Label(self, text="Gon").grid(row=2, column=0)

        Entry(self, textvariable=self.strEntryGrad).grid(
            row=0, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.strEntryRad).grid(
            row=1, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.strEntryGon).grid(
            row=2, column=1, padx=3, pady=3)

        Button(self, text="Berechne", command=self.btnPressedBerechneGrad).grid(
            row=0, column=2, padx=3, pady=3)
        Button(self, text="Berechne", command=self.btnPressedBerechneRad).grid(
            row=1, column=2, padx=3, pady=3)
        Button(self, text="Berechne", command=self.btnPressedBerechneGon).grid(
            row=2, column=2, padx=3, pady=3)

    def btnPressedBerechneGrad(self):
        w = Winkel(float(self.strEntryGrad.get().replace(",", ".")),einheit="grad")
        self.strEntryRad.set(w.get_w(einheit="rad"))
        self.strEntryGon.set(w.get_w(einheit="gon"))

    def btnPressedBerechneRad(self):
        w = Winkel(float(self.strEntryRad.get().replace(",", ".")),einheit="rad")
        self.strEntryGon.set(w.get_w(einheit="gon"))
        self.strEntryGrad.set(w.get_w(einheit="grad"))

    def btnPressedBerechneGon(self):
        w = Winkel(float(self.strEntryGon.get().replace(",", ".")),einheit="gon")
        self.strEntryRad.set(w.get_w(einheit="rad"))
        self.strEntryGrad.set(w.get_w(einheit="grad"))

    def save_json(self):
        str_wRad =  Winkel(float(self.strEntryRad.get().replace(",", ".")),einheit="rad").get_json()
        str_wGon =  Winkel(float(self.strEntryGon.get().replace(",", ".")),einheit="gon").get_json()
        str_wGrad =  Winkel(float(self.strEntryGrad.get().replace(",", ".")),einheit="grad").get_json()
        return json.dumps({"rad":str_wRad, "gon":str_wGon, "grad":str_wGrad})

    def load_json(self,s):
            dic_j = json.loads(s)
            wgrad = Winkel()
            wrad = Winkel()
            wgon = Winkel()
            wgrad.set_json(dic_j["grad"])
            wrad.set_json(dic_j["rad"])
            wgon.set_json(dic_j["gon"])
            self.strEntryGrad.set(wgrad.get_w("grad")) 
            self.strEntryRad.set(wrad.get_w("rad")) 
            self.strEntryGon.set(wgon.get_w("gon")) 

if __name__ == "__main__":
    root = Tk()
    root.title("Winkelrechner")
    root.geometry
    app = FensterWinkelrechner(root)
    app.mainloop()