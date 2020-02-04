from tkinter import Frame, Tk, Button, Toplevel, Menu

if __name__ == "__main__":
    import sys
    sys.path.append(".")


class GuiTemplate(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)

        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Load JSON", command=self.load_json)
        filemenu.add_command(label="Save JSON", command=self.save_json)
        menubar.add_cascade(label="File", menu=filemenu)

        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label="Help", command=self.open_help)
        aboutmenu.add_command(label="About", command=self.open_msgAbout)
        menubar.add_cascade(label="?", menu=aboutmenu)
        master.config(menu=menubar)

    def load_json(self):
        pass

    def save_json(self):
        pass

    def open_help(self):
        pass

    def open_msgAbout(self):
        pass


if __name__ == "__main__":
    root = Tk()
    #root.title("Geodätische Toolbox")
    # root.geometry("350x75")
    app = GuiTemplate(root)
    app.mainloop()
