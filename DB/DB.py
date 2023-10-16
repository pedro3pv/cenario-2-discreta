import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from matplotlib_venn import venn2


def repetidos(DB1, DB2):
    LengthDB1 = DB1.shape[0]
    LengthDB2 = DB2.shape[0]

    loop = False
    x = 0
    y = 0

    while x < int(LengthDB1):
        for y in range(int(LengthDB2)):
            if DB1["Nome"][x] == DB2["Nome"][y] and DB1["Nome da Mae"][x] == DB2["Nome da Mae"][y] and \
                    DB1["Nome do Pai"][x] == DB2["Nome do Pai"][y] and DB1["Sexo"][x].upper() == DB2["Sexo"][y]:
                print("DB1:" + str(x))
                print("DB2:" + str(y) + "\n")
                print("DB1:" + DB1["Nome"][x])
                print("DB2:" + DB2["Nome"][y])
                DB1.drop(x, axis=0, inplace=True)
                DB1.reset_index(drop=True, inplace=True)
                LengthDB1 -= 1
                loop = True
                if x < LengthDB1:
                    print("afterDB1:" + DB1["Nome"][x] + "\n")
        x += 1
    if loop:
        repetidos(DB1, DB2)
    DB1.reset_index(drop=True, inplace=True)
    return DB1


def iguais(DB1, DB2):
    DB1["Sexo"] = DB1["Sexo"].str.upper()
    DB2["Sexo"] = DB2["Sexo"].str.upper()

    chave = ["Nome", "Nome da Mae", "Nome do Pai", "Sexo"]

    DB_iguais = pd.merge(DB1, DB2, on=chave, how='inner')

    DB_iguais.drop(list(DB_iguais.filter(regex='_y')), axis=1, inplace=True)
    DB_iguais = DB_iguais.rename(columns={
        "ID_x": "ID",
        "Ônibus_x": "Ônibus",
        "Data da Dengue_x": "Data da Dengue",
        "Data de Nascimento_x": "Data de Nascimento",
    })

    return DB_iguais


def adicionar(DB1, DB2):
    DB1 = repetidos(DB1, DB2)
    DB1 = pd.concat([DB1, DB2], ignore_index=True)
    DB1.reset_index(drop=True, inplace=True)
    return DB1
