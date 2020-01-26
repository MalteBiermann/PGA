import gui.hauptfenster
from tkinter import Tk


root = Tk()
root.title("Geodätische Toolbox")
#root.geometry("350x75")
app = gui.hauptfenster.HauptFenster(root)
app.mainloop()




