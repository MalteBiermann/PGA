from tkinter import Frame, Tk, Button, Toplevel, Menu, messagebox, filedialog
from os import startfile

if __name__ == "__main__":
    import sys
    sys.path.append(".")


class GuiTemplate(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.createmenu()
        self.master = master

    def createmenu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load JSON", command=self.open_loadJson)
        filemenu.add_command(label="Save JSON", command=self.open_saveJson)
        menubar.add_cascade(label="File", menu=filemenu)

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command=self.open_help)
        aboutmenu.add_command(label="About", command=self.open_msgAbout)
        menubar.add_cascade(label="?", menu=aboutmenu)
        self.master.config(menu=menubar)


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
        if filepath is not None:
            with open(filepath,'w') as fh:
                fh.writelines(j_s)
    
    def save_json(self):
        return ""

    def open_help(self):
        filepath = ""
        if sys.platform == 'darwin':
            open(filepath)
        else:
            startfile(filepath)

    def open_msgAbout(self):
        authors="Svenja Rode,\nChris Arends,\nHendrik Gebben,\nMalte Biermann"
        messagebox.showinfo("Autoren",authors)



if __name__ == "__main__":
    root = Tk()
    #root.title("Geodätische Toolbox")
    # root.geometry("350x75")
    app = GuiTemplate(root)
    app.mainloop()
