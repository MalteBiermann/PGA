from tkinter import Frame,Tk,Button,Toplevel,LabelFrame,Label,Entry,StringVar
from tkinter.ttk import Treeview

class FensterTrans(Frame):
    def __init__(self, master):
        super().__init__(master)

        
        self.eingabe1 = StringVar()
        self.eingabe2 = StringVar()
        self.eingabe3 = StringVar()
        self.grid()

        lfSource = LabelFrame(root, text="Quellsystem")
        lfSource.grid(row=0, column=0, padx=3, pady=3)
        lfDest = LabelFrame(root, text="Zielsystem")
        lfDest.grid(row=0, column=1, padx=3, pady=3)

        punktListSource = Treeview(lfSource)
        punktListSource.grid(row=0, column=0, padx=3, pady=3)
        punktListSource["columns"] = ("y", "x", "status")
        punktListSource.column("#0",width = 100, minwidth=100)
        punktListSource.column("status",width = 50, minwidth=50)
        punktListSource.heading("#0",text="id")
        punktListSource.heading("y",text="y")
        punktListSource.heading("x",text="x")
        punktListSource.heading("status",text="aktiv")

        punktListDest = Treeview(lfDest)
        punktListDest.grid(row=0, column=0, padx=3, pady=3)
        punktListDest["columns"] = ("y", "x", "status")
        punktListDest.column("#0",width = 100, minwidth=100)
        punktListDest.column("status",width = 50, minwidth=50)
        punktListDest.heading("#0",text="id")
        punktListDest.heading("y",text="y")
        punktListDest.heading("x",text="x")
        punktListDest.heading("status",text="aktiv")



        #Label(lf, text="TEST").grid(row=0, column=0)
        #Label(self, text="Rad:").grid(row=1, column=0)
        #Label(self, text="Gon:").grid(row=2, column=0)

        #Entry(self, textvariable=self.eingabe1).grid(row=0, column=1, padx=3, pady=3)
        #Entry(self, textvariable=self.eingabe2).grid(row=1, column=1, padx=3, pady=3)
        #Entry(self, textvariable=self.eingabe3).grid(row=2, column=1, padx=3, pady=3)

        # self.focus_set()
        # self.grab_set()
        # self.wait_window()

if __name__ == "__main__":

    root = Tk()
    root.title("Transformationen")
    root.geometry
    app = FensterTrans(root)
    app.mainloop()