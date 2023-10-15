import pandas as pd
from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

# Carregar os dados dos arquivos CSV
db1 = pd.read_csv("DB/BaseDengue7.csv")
db2 = pd.read_csv("DB/BaseOnibus7.csv", encoding="cp1252")
db3 = pd.read_csv("DB/BaseAlunos7.csv")

# 1) Relatório Educação
def relatorio_educacao(db1, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    educacao_ids = db3['ID']
    resultado = db3[educacao_ids.isin(educacao_ids) & ~educacao_ids.isin(dengue_ids)]
    venn2(subsets=(len(educacao_ids), len(dengue_ids), len(resultado)),
          set_labels=('Educação', 'Dengue'))
    plt.title('Relatório Educação')
    resultado.to_excel('Relatorio_Educacao.xlsx', index=False)

# 2) Relatório Saúde
def relatorio_saude(db1, db2):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    sem_onibus = db2.dropna(subset=['Ônibus'])['ID']
    resultado = db2[saude_ids.isin(saude_ids) & ~saude_ids.isin(dengue_ids) & saude_ids.isin(sem_onibus)]
    venn3(subsets=(len(saude_ids), len(dengue_ids), len(sem_onibus), len(resultado), 0, 0, 0),
          set_labels=('Saúde', 'Dengue', 'Sem Ônibus'))
    plt.title('Relatório Saúde')
    resultado.to_excel('Relatorio_Saude.xlsx', index=False)

# 3) Relatório Mobilidade
def relatorio_mobilidade(db1, db2):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    mobilidade_ids = db2['ID']
    resultado = db2[mobilidade_ids.isin(mobilidade_ids) & ~mobilidade_ids.isin(dengue_ids)]
    venn2(subsets=(len(mobilidade_ids), len(dengue_ids), len(resultado)),
          set_labels=('Mobilidade', 'Dengue'))
    plt.title('Relatório Mobilidade')
    resultado.to_excel('Relatorio_Mobilidade.xlsx', index=False)

# 4) Relatório Educação e Saúde
def relatorio_educacao_saude(db1, db2, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    educacao_ids = db3['ID']
    resultado = db3[educacao_ids.isin(educacao_ids) & educacao_ids.isin(dengue_ids)]
    venn2(subsets=(len(educacao_ids), len(dengue_ids), len(resultado)),
          set_labels=('Educação', 'Dengue'))
    plt.title('Relatório Educação e Saúde')
    resultado.to_excel('Relatorio_Educacao_e_Saude.xlsx', index=False)

# 5) Relatório Educação e Mobilidade
def relatorio_educacao_mobilidade(db2, db3):
    mobilidade_ids = db2['ID']
    educacao_ids = db3['ID']
    resultado = db3[educacao_ids.isin(educacao_ids) & mobilidade_ids.isin(mobilidade_ids)]
    venn2(subsets=(len(educacao_ids), 0, len(mobilidade_ids), len(resultado)),
          set_labels=('Educação', 'Mobilidade'))
    plt.title('Relatório Educação e Mobilidade')
    resultado.to_excel('Relatorio_Educacao_e_Mobilidade.xlsx', index=False)

# 6) Relatório Saúde e Mobilidade
def relatorio_saude_mobilidade(db1, db2, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    mobilidade_ids = db2['ID']
    resultado = db2[saude_ids.isin(saude_ids) & mobilidade_ids.isin(mobilidade_ids) & saude_ids.isin(dengue_ids)]
    venn3(subsets=(len(saude_ids), len(dengue_ids), len(mobilidade_ids), len(resultado), 0, 0, 0),
          set_labels=('Saúde', 'Dengue', 'Mobilidade'))
    plt.title('Relatório Saúde e Mobilidade')
    resultado.to_excel('Relatorio_Saude_e_Mobilidade.xlsx', index=False)

# 7) Relatório Saúde, Mobilidade e Educação
def relatorio_saude_mobilidade_educacao(db1, db2, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    mobilidade_ids = db2['ID']
    educacao_ids = db3['ID']
    resultado = db3[saude_ids.isin(saude_ids) & mobilidade_ids.isin(mobilidade_ids) &
                     educacao_ids.isin(educacao_ids) & saude_ids.isin(dengue_ids)]
    venn3(subsets=(len(saude_ids), len(dengue_ids), len(mobilidade_ids),
                   len(educacao_ids), len(resultado), 0, 0),
          set_labels=('Saúde', 'Dengue', 'Mobilidade'))
    plt.title('Relatório Saúde, Mobilidade e Educação')
    resultado.to_excel('Relatorio_Saude_Mobilidade_Educacao.xlsx', index=False)

# 8) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos que frequentaram o posto de saúde, mas não utilizaram transporte público.
def relatorio_saude_sem_mobilidade(db1, db2):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    mobilidade_ids = db2['ID']
    resultado = db2[saude_ids.isin(saude_ids) & ~mobilidade_ids.isin(mobilidade_ids) & saude_ids.isin(dengue_ids)]
    resultado.drop('Ônibus', axis=1, inplace=True)
    venn2(subsets=(len(saude_ids), len(dengue_ids), len(resultado)),
          set_labels=('Saúde', 'Dengue'))
    plt.title('Relatório Saúde sem Mobilidade')
    resultado.to_excel('Relatorio_Saude_Sem_Mobilidade.xlsx', index=False)

# 9) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos que frequentaram o posto de saúde, mas não frequentaram a escola.
def relatorio_saude_sem_educacao(db1, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    educacao_ids = db3['ID']
    resultado = db3[saude_ids.isin(saude_ids) & ~educacao_ids.isin(educacao_ids) & saude_ids.isin(dengue_ids)]
    venn2(subsets=(len(saude_ids), len(dengue_ids), len(resultado)),
          set_labels=('Saúde', 'Dengue'))
    plt.title('Relatório Saúde sem Educação')
    resultado.to_excel('Relatorio_Saude_Sem_Educacao.xlsx', index=False)

# 10) Informar nome, data de nascimento, data que tiveram dengue dos cidadãos que frequentaram o posto de saúde, mas não frequentaram a escola nem utilizaram transporte público.
def relatorio_saude_sem_educacao_mobilidade(db1, db2, db3):
    dengue_ids = db1.dropna(subset=['Data da Dengue'])['ID']
    saude_ids = db2['ID']
    mobilidade_ids = db2['ID']
    educacao_ids = db3['ID']
    resultado = db3[saude_ids.isin(saude_ids) & ~educacao_ids.isin(educacao_ids) &
                     ~mobilidade_ids.isin(mobilidade_ids) & saude_ids.isin(dengue_ids)]
    resultado.drop('Ônibus', axis=1, inplace=True)
    venn2(subsets=(len(saude_ids), len(dengue_ids), len(resultado)),
          set_labels=('Saúde', 'Dengue'))
    plt.title('Relatório Saúde sem Educação e Mobilidade')
    resultado.to_excel('Relatorio_Saude_Sem_Educacao_Mobilidade.xlsx', index=False)

# Executar os relatórios
relatorio_educacao(db1, db3)
relatorio_saude(db1, db2)
relatorio_mobilidade(db1, db2)
relatorio_educacao_saude(db1, db2, db3)
relatorio_educacao_mobilidade(db2, db3)
relatorio_saude_mobilidade(db1, db2, db3)
relatorio_saude_mobilidade_educacao(db1, db2, db3)
relatorio_saude_sem_mobilidade(db1, db2)
relatorio_saude_sem_educacao(db1, db3)
relatorio_saude_sem_educacao_mobilidade(db1, db2, db3)