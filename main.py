import Screen
from DB import DB
import pandas as pd

baseDeAlunos = pd.read_csv("DB/Base de Alunos7.csv", sep=";")
baseDeDengue = pd.read_csv("DB/Base de Dengue7.csv", sep=";")
baseDeOnibus = pd.read_csv("DB/Base de Onibus7.csv", encoding="cp1252", sep=";")

#baseDeCidadoes = DB.adicionar(DB.adicionar(baseDeAlunos, baseDeDengue), baseDeOnibus)

#TEST
#test = DB.iguais(baseDeAlunos, baseDeDengue)
#print(test)
#test[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("test.xlsx")

#1
relatorioEducacao = DB.repetidos(baseDeAlunos, baseDeDengue)
relatorioEducacao[["Nome", "Data de Nascimento", "ID"]].to_excel("Relatorios/Relatório Educação.xlsx")

#2
BaseNaoOnibus = DB.iguais(baseDeDengue, baseDeOnibus)
relatorioSaude = DB.repetidos(baseDeDengue, baseDeOnibus)
relatorioSaude[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("Relatorios/Relatório Saúde.xlsx")

#3
BasenaoDengue = DB.iguais(baseDeOnibus, baseDeDengue)
relatorioMobilidade = DB.repetidos(baseDeOnibus, BasenaoDengue)
relatorioMobilidade[["Nome", "Data de Nascimento", "Ônibus"]].to_excel("Relatorios/Relatório Mobilidade.xlsx")

#4
RelatorioEducacaoeSaude = DB.iguais(baseDeAlunos, baseDeDengue)
RelatorioEducacaoeSaude[["Nome", "Data de Nascimento", "ID", "Data da Dengue"]].to_excel("Relatorios/Relatório Educação e Saúde.xlsx")

#5
RelatorioEducacaoeMobilidade = DB.iguais(baseDeAlunos, baseDeOnibus)
RelatorioEducacaoeMobilidade[["Nome", "Data de Nascimento", "ID", "Ônibus"]].to_excel("Relatorios/Relatório Educação e Mobilidade.xlsx")

#6
RelatorioSaudeeMobilidade = DB.iguais(baseDeDengue, baseDeOnibus)
RelatorioSaudeeMobilidade[["Nome", "Data de Nascimento", "Data da Dengue", "Ônibus"]].to_excel("Relatorios/Relatório Saúde e Mobilidade.xlsx")

#7
db = DB.iguais(baseDeDengue, baseDeAlunos)
db2 = DB.iguais(baseDeDengue, baseDeOnibus)
RelatorioSaudeMobilidadeeEducacao = DB.iguais(db, db2)
RelatorioSaudeMobilidadeeEducacao[["Nome", "Data de Nascimento", "Data da Dengue", "Ônibus"]].to_excel("Relatorios/Relatório Saúde, Mobilidade e Educação.xlsx")

#8
BaseNaoOnibus = DB.repetidos(baseDeDengue, baseDeOnibus)
RelatorioSaudeeNaoMobilidade = DB.iguais(baseDeDengue, BaseNaoOnibus)
RelatorioSaudeeNaoMobilidade[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("Relatorios/Relatório Saúde e Não Mobilidade.xlsx")

#9
BaseNaoAlunos = DB.repetidos(baseDeDengue, baseDeAlunos)
RelatorioSaudeeNaoEducacao = DB.iguais(baseDeDengue, BaseNaoAlunos)
RelatorioSaudeeNaoEducacao[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("Relatorios/Relatório Saúde e Não Educação.xlsx")

#10
BaseNaoOnibus = DB.repetidos(baseDeDengue, baseDeOnibus)
BaseNaoAlunos = DB.repetidos(baseDeDengue, baseDeAlunos)
RelatorioSaudeNaoMobilidadeNaoEducacao = DB.iguais(BaseNaoAlunos,BaseNaoOnibus)
RelatorioSaudeNaoMobilidadeNaoEducacao[["Nome", "Data de Nascimento", "Data da Dengue"]].to_excel("Relatorios/Relatório Saúde, Não Mobilidade e Não Educação.xlsx")

Screen.render(relatorioEducacao, relatorioSaude, relatorioMobilidade, RelatorioEducacaoeSaude, RelatorioEducacaoeMobilidade, RelatorioSaudeeMobilidade, RelatorioSaudeMobilidadeeEducacao, RelatorioSaudeeNaoMobilidade, RelatorioSaudeeNaoEducacao, RelatorioSaudeNaoMobilidadeNaoEducacao)