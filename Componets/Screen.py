import tkinter
from tkinter import ttk
from tkinter.ttk import Entry


def render(entrada):
    root = tkinter.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
