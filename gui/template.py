from tkinter import Frame, Tk, Button, Toplevel, Menu, messagebox, filedialog, Label
from os import startfile
import webbrowser
import sys

if __name__ == "__main__":
    import sys
    sys.path.append(".")

from gui.round import FensterRound

class GuiTemplate(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createmenu()
        self.master = master

        self.int_round = 3
        self.bool_roundActive = False

    def createmenu(self):
        menubar = Menu(self)
        
        filemenu = Menu(menubar, tearoff=0)
        classlist = ("FensterTrans", "FensterPZ")
        if self.get_class_name(self) in classlist:
            filemenu.add_command(label="Load JSON", command=self.open_loadJson)
            filemenu.add_command(label="Save JSON", command=self.open_saveJson)
        else:
            filemenu.add_command(label="Load JSON", command=self.open_loadJson, state="disabled")
            filemenu.add_command(label="Save JSON", command=self.open_saveJson, state="disabled")
        menubar.add_cascade(label="File", menu=filemenu)

        menubar.add_cascade(label="Runden", command=self.open_roundWindow)

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command=self.open_help)
        aboutmenu.add_command(label="About", command=self.open_msgAbout)
        menubar.add_cascade(label="?", menu=aboutmenu)
        self.master.config(menu=menubar)
    
    def get_class_name(self, instance):
        return instance.__class__.__name__

    def open_loadJson(self):
        filepath = filedialog.askopenfilename(filetypes =[('JSON', '*.json'),('*', '*.*')])
        if filepath is not None:
            with open(filepath, 'r') as fh:
                s = fh.read()
            self.load_json(s)

    def load_json(self,s=""):
        pass

    def open_saveJson(self):
        j_s = self.save_json()
        filepath = filedialog.asksaveasfilename(filetypes=[("JSON","*.json")], defaultextension=[("JSON","*.json")])
        if filepath != "":
            with open(filepath,'w') as fh:
                fh.writelines(j_s)
    
    def save_json(self):
        return ""

    def open_help(self):
        filepath = "manual.pdf"
        if sys.platform == 'darwin':
            open(filepath)
        else:
            startfile(filepath)

    def open_msgAbout(self):
        authors = "Malte Biermann\n\n https://github.com/MalteBiermann/PGA"
        messagebox.showinfo("Autoren",authors)

    def open_roundWindow(self):
        top = Toplevel()
        top.title("Runden")
        self.F_round = FensterRound(top, self)
    
    def runde(self, f):
        if self.bool_roundActive:
            return round(f, self.int_round)
        else:
            return f


if __name__ == "__main__":
    root = Tk()
    #root.title("Geodätische Toolbox")
    # root.geometry("350x75")
    app = GuiTemplate(root)
    app.mainloop()
