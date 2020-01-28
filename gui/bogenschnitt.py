from tkinter import Button, Entry, Frame, Label, StringVar, Tk

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.bogenschnitt import Bogenschnitt
from datentyp.kreis import Kreis
from datentyp.punkt import Punkt


class FensterBS(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.eingabeX1 = StringVar()
        self.eingabeY1 = StringVar()
        self.eingabeX2 = StringVar()
        self.eingabeY2 = StringVar()
        self.eingabeS1 = StringVar()
        self.eingabeS2 = StringVar()

        self.ausgabeX1 = StringVar()
        self.ausgabeY1 = StringVar()
        self.ausgabeX2 = StringVar()
        self.ausgabeY2 = StringVar()
        self.grid()

        Entry(self, textvariable=self.eingabeY1).grid(row=1, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeX1).grid(row=2, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeY2).grid(row=1, column=2, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeX2).grid(row=2, column=2, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeS1).grid(row=3, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabeS2).grid(row=3, column=2, padx=3, pady=3)
        Entry(self, textvariable=self.ausgabeY1, state="readonly").grid(row=1, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.ausgabeX1, state="readonly").grid(row=2, column=4, padx=3, pady=3)
        Entry(self, textvariable=self.ausgabeY2, state="readonly").grid(row=1, column=5, padx=3, pady=3)
        Entry(self, textvariable=self.ausgabeX2, state="readonly").grid(row=2, column=5, padx=3, pady=3)
        
        Label(self, text="(Rechts) Y:").grid(row=1, column=0)
        Label(self, text="(Hoch) X:").grid(row=2, column=0)
        Label(self, text="Punkt A:").grid(row=0, column=1)
        Label(self, text="Punkt B:").grid(row=0, column=2)
        Label(self, text="S:").grid(row=3, column=0)
        Label(self, text="Punkt C:").grid(row=0, column=4)
        Label(self, text="Punkt D:").grid(row=0, column=5)

        Button(self, text="Berechne", command=self.btnBerechnePressed).grid(row=4, column=3, padx=3, pady=3)

        # self.focus_set()
        # self.grab_set()
        # self.wait_window()


    def btnBerechnePressed(self):
        pass
        p1 = Punkt()
        p2 = Punkt()
        k1 = Kreis()
        k2 = Kreis()
        p3, p4 = Bogenschnitt(k1, k2).berechne()




if __name__ == "__main__":
    pass
    root = Tk()
    root.title("Bogenschnitt")
    root.geometry
    app = FensterBS(root)
    app.mainloop()
