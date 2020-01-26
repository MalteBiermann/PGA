from tkinter import *

from operation.winkelrechner import *

class FensterWinkelrechner(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.eingabe1 = StringVar()
        self.eingabe2 = StringVar()
        self.eingabe3 = StringVar()
        self.grid()

        Label(self, text="Grad:").grid(row=0, column=0)
        Label(self, text="Rad:").grid(row=1, column=0)
        Label(self, text="Gon:").grid(row=2, column=0)

        Entry(self, textvariable=self.eingabe1).grid(
            row=0, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabe2).grid(
            row=1, column=1, padx=3, pady=3)
        Entry(self, textvariable=self.eingabe3).grid(
            row=2, column=1, padx=3, pady=3)

        Button(self, text="Berechne", command=self.btnBerechneGradPressed).grid(
            row=0, column=2, padx=3, pady=3)
        Button(self, text="Berechne", command=self.btnBerechneRadPressed).grid(
            row=1, column=2, padx=3, pady=3)
        Button(self, text="Berechne", command=self.btnBerechneGonPressed).grid(
            row=2, column=2, padx=3, pady=3)

        Button(self, text="exit", command=master.destroy).grid(
            row=5, column=0, padx=3, pady=3)

        self.focus_set()
        self.grab_set()
        self.wait_window()

    def btnBerechneGradPressed(self):
        #m = "rad={:5.3f}".format(grad2rad(float(self.eingabe1.get())))
        gon = grad2gon(float(self.eingabe1.get().replace(",", ".")))
        rad = grad2rad(float(self.eingabe1.get().replace(",", ".")))
        self.eingabe2.set(rad)
        self.eingabe3.set(gon)

    def btnBerechneRadPressed(self):
        gon = rad2gon(float(self.eingabe2.get().replace(",", ".")))
        grad = rad2grad(float(self.eingabe2.get().replace(",", ".")))
        self.eingabe3.set(gon)
        self.eingabe1.set(grad)

    def btnBerechneGonPressed(self):
        grad = gon2grad(float(self.eingabe3.get().replace(",", ".")))
        rad = gon2rad(float(self.eingabe3.get().replace(",", ".")))
        self.eingabe2.set(rad)
        self.eingabe1.set(grad)


if __name__ == "__main__":

    root = Tk()
    root.title("Winkelrechner")
    root.geometry
    app = FensterWinkelrechner(root)
    app.mainloop()