import tkinter
from tkinter import ttk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

baseDeAlunos = pd.read_csv("DB/BaseAlunos7.csv")
baseDeDengue = pd.read_csv("DB/BaseDengue7.csv")
baseDeOnibus = pd.read_csv("DB/BaseOnibus7.csv",encoding="cp1252")

for x in len(baseDeAlunos["ID"]):
    print(x)


root = tkinter.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Olá Mundo!").grid(column=0, row=0)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=0)
root.mainloop()

print(baseDeAlunos['Sexo'].value_counts(normalize = True) * 100)