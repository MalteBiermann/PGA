from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Entry,StringVar,filedialog,Text,Radiobutton,END,Label, IntVar
from tkinter.ttk import Treeview

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from operation.helmerttransformation import HelmertTrans, Punkt_Dic


class Fenster_loadPList(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.filePathSource = StringVar()
        self.sepDec = StringVar(root,value=".")
        self.sepVal = StringVar(root,value=";")
        self.v = IntVar(root,value=0)
        self.grid()


        lfFile = LabelFrame(root, text="Dateiauswahl")
        lfFile.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Button(lfFile, text="Öffnen", command=self.btnPressedOpenFileDialog).grid(row=0, column=0, padx=3, pady=3, sticky="w")

        lfText = LabelFrame(root, text="Einfügen")
        lfText.grid(row=1, column=0, padx=3, pady=3, columnspan=3, sticky="w")
        self.tField = Text(lfText,height=50,width=50)
        self.tField.grid(row=0, column=0, padx=3, pady=3, sticky="w")

        lfRadio = LabelFrame(root, text="System")
        lfRadio.grid(row=2, column=0, padx=3, pady=3, sticky="w")
        Radiobutton(lfRadio,text="Quellsystem", variable=self.v, value=0).grid(row=0, column=0, padx=3, pady=3)
        Radiobutton(lfRadio,text="Zielsystem", variable=self.v, value=1).grid(row=0, column=1, padx=3, pady=3)

        lfSep = LabelFrame(root, text="Separatoren")
        lfSep.grid(row=2, column=1, padx=3, pady=3, sticky="w")
        Label(lfSep,text="Werte").grid(row=0, column=0, padx=3, pady=3)
        Entry(lfSep, textvariable=self.sepVal, width=3).grid(row=0, column=1, padx=3, pady=3)
        Label(lfSep,text="Dezimal").grid(row=1, column=0, padx=3, pady=3)
        Entry(lfSep, textvariable=self.sepDec, width=3).grid(row=1, column=1, padx=3, pady=3)



        Button(root,text="Lade Punkte", command=self.btnPressedLoad).grid(row=2, column=2, padx=3, pady=3, sticky="w")

        # self.focus_set()
        # self.grab_set()
        # self.wait_window()

    def btnPressedOpenFileDialog(self):
        try:
            fileInput = filedialog.askopenfile(mode="r",filetypes =[('CSV', '*.csv'),('*', '*.*')])
        except:
            pass

        if fileInput is not None: 
            self.tField.insert(END, fileInput.read())


    def btnPressedLoad(self):
        pass




if __name__ == "__main__":

    root = Tk()
    root.title("Punktlisten laden")
    root.geometry
    app = Fenster_loadPList(root)
    app.mainloop()