from tkinter import Frame,Tk,Toplevel,Label,Entry,StringVar,Checkbutton,BooleanVar


if __name__ == "__main__":
    import sys
    sys.path.append(".")


class FensterRound(Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.int_round = StringVar(value=self.controller.int_round)
        self.int_round.trace_add('write', self.callback_int)
        if self.controller.bool_roundActive:
            self.bool_roundActive = BooleanVar(value=1)
        else:
            self.bool_roundActive = BooleanVar(value=0)

        self.grid()
        self.chkb = Checkbutton(master, text="Runden", var=self.bool_roundActive, command=self.callback_chkb)
        self.chkb.grid(row=0, column=0, padx=3, pady=3, sticky="w")
        Label(master, text="Anzahl Nachkommastellen").grid(row=1, column=0, padx=3, pady=3, sticky="w")
        self.entry_round = Entry(master,textvariable=self.int_round, validate="all", validatecommand=self.callback_int, width=5)
        self.entry_round.grid(row=1, column=1, padx=3, pady=3, sticky="e")
        self.init_chkb()
        self.callback_chkb()

    def callback_chkb(self):
        if self.bool_roundActive.get() == 1:
            self.entry_round.config(state="normal")
            self.controller.bool_roundActive = True
        else:
            self.entry_round.config(state="disabled")
            self.controller.bool_roundActive = False

    def callback_int(self, *args):
        if self.int_round.get() != "":
            self.controller.int_round = int(self.int_round.get())

    def init_chkb(self):
        if self.controller.bool_roundActive:
            self.chkb.select()
        else:
            self.chkb.deselect()


if __name__ == "__main__":

    root = Tk()
    root.title("Rundestellen")
    root.geometry
    appRound = FensterRound(root,root)
    appRound.mainloop()