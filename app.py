import tkinter

root = tkinter.Tk()

hi_there = tkinter.Label(
    root,
    text='hi there',
    bg='red',
    fg='white'
)
hi_there.pack(fill=tkinter.BOTH, expand=True)

my_name = tkinter.Label(
    root,
    text='Marcell Gibbs'
)
my_name.pack()

root.mainloop()