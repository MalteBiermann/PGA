from tkinter import Frame,Tk,Button,Toplevel

class FensterRS(Frame):
    def __init__(self, master):
        super().__init__(master)
        pass
        self.focus_set()
        self.grab_set()
        self.wait_window()

if __name__ == "__main__":
    pass