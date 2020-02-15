from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Entry,StringVar,filedialog,Text,Radiobutton,END,Label, IntVar
from tkinter.ttk import Treeview

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.helmerttransformation import HelmertTrans, Punkt_Dic


class Fenster_loadPList(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.filePathSource = StringVar()
        self.sepDec = StringVar(self,value=".")
        self.sepVal = StringVar(self,value=";")
        self.radioSystem = IntVar(self,value=0)
        self.grid()


        lfFile = LabelFrame(self, text="Dateiauswahl")
        lfFile.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Button(lfFile, text="Öffnen", command=self.btnPressedOpenFileDialog).grid(row=0, column=0, padx=3, pady=3, sticky="w")

        lfText = LabelFrame(self, text="Einfügen")
        lfText.grid(row=1, column=0, padx=3, pady=3, columnspan=3, sticky="w")
        self.tField = Text(lfText,height=30,width=50)
        self.tField.grid(row=0, column=0, padx=3, pady=3, sticky="w")

        lfRadio = LabelFrame(self, text="System")
        lfRadio.grid(row=2, column=0, padx=3, pady=3, sticky="w")
        Radiobutton(lfRadio,text="Quellsystem", variable=self.radioSystem, value=0).grid(row=0, column=0, padx=3, pady=3)
        Radiobutton(lfRadio,text="Zielsystem", variable=self.radioSystem, value=1).grid(row=0, column=1, padx=3, pady=3)

        lfSep = LabelFrame(self, text="Trennzeichen")
        lfSep.grid(row=2, column=1, padx=3, pady=3, sticky="w")
        Label(lfSep,text="Werte").grid(row=0, column=0, padx=3, pady=3)
        Entry(lfSep, textvariable=self.sepVal, width=3).grid(row=0, column=1, padx=3, pady=3)
        Label(lfSep,text="Dezimal").grid(row=1, column=0, padx=3, pady=3)
        Entry(lfSep, textvariable=self.sepDec, width=3).grid(row=1, column=1, padx=3, pady=3)

        Button(self,text="Lade Punkte", command=self.btnPressedLoad).grid(row=2, column=2, padx=3, pady=3, sticky="w")

        # self.focus_set()
        # self.grab_set()
        # self.wait_window()

    def btnPressedOpenFileDialog(self):
        try:
            fileInput = filedialog.askopenfile(mode="r",filetypes =[('CSV', '*.csv'),('*', '*.*')])
        except:
            pass

        if fileInput is not None: 
            self.tField.delete("1.0",END)
            self.tField.insert(END, fileInput.read())


    def btnPressedLoad(self):
        self.controller.loadPoints(self.tField.get(1.0,END), self.sepDec.get(), self.sepVal.get(), self.radioSystem.get())




if __name__ == "__main__":

    root = Tk()
    root.title("Punktlisten laden")
    root.geometry
    appLoadPList = Fenster_loadPList(root,root)
    appLoadPList.mainloop()