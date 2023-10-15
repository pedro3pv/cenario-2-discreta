from DB import DB
import pandas as pd

baseDeAlunos = pd.read_csv("DB/BaseAlunos7.csv")
baseDeDengue = pd.read_csv("DB/BaseDengue7.csv")
baseDeOnibus = pd.read_csv("DB/BaseOnibus7.csv", encoding="cp1252")
#baseDeCidadoes = DB.adicionar(DB.adicionar(baseDeAlunos, baseDeDengue), baseDeOnibus)

#relatorioEducacao = DB.repetidos(baseDeAlunos, baseDeDengue)
#relatorioEducacao[["Nome", "Data de Nascimento", "ID"]].to_excel("Relatório Educação.xlsx")

test = DB.iguais(baseDeAlunos, baseDeDengue)
print(test)
test[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("test.xlsx")

#BaseNaoOnibus = DB.repetidos(baseDeDengue, baseDeOnibus)
#relatorioSaude = DB.repetidos(baseDeDengue, BaseNaoOnibus)
#relatorioSaude[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("Relatório Saúde.xlsx")

relatorioMobilidade = DB.repetidos(baseDeOnibus, baseDeDengue)
relatorioMobilidade[["Nome", "Data de Nascimento", "Ônibus"]].to_excel("Relatório Mobilidade.xlsx")

#RelatorioEducacaoeSaude =

#RelatorioEducacaoeMobilidade =