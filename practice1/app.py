import tkinter

class Text:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.timer_text = tkinter.StringVar()

        self.build_grid()
        self.build_banner()
        self.build_text()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            background='blue',
            text='Get Text Data',
            fg='white',
            font=('Helvetica', 24)
        )
        banner.grid(
            row=0, column=0,
            sticky='ew',
            padx=10, pady=10
        )

    def build_text(self):
        text = Text(root, width=40, height=10)
        text.insert('1.0', 'Hello World!')

root = tkinter.Tk()
Text(root)
root.mainloop(0)