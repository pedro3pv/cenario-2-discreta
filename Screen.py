from streamlit_option_menu import option_menu
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn3, venn3_unweighted
import streamlit as st
import pandas as pd

from DB import DB

baseDeAlunos = pd.read_csv("DB/Base de Alunos7.csv", sep=";")
baseDeDengue = pd.read_csv("DB/Base de Dengue7.csv", sep=";")
baseDeOnibus = pd.read_csv("DB/Base de Onibus7.csv", encoding="cp1252", sep=";")

def render(DB1, DB2, DB3, DB4, DB5, DB6, DB7, DB8, DB9, DB10):
    st.set_page_config(layout="wide")
    selected = option_menu(
        menu_title=None,
        options=[
            "1 Relatório Educação",
            "2 Relatório Saúde",
            "3 Relatório Mobilidade",
            "4 Relatório Educação e Saúde",
            "5 Relatório Educação e Mobilidade",
            "6 Relatório Saúde e Mobilidade",
            "7 Relatório Saúde, Mobilidade e Educação",
            "8 Relatório Saúde e Não Mobilidade",
            "9 Relatório Saúde e Não Educação",
            "10 Relatório Saúde, Não Mobilidade e Não Educação",
        ],
        default_index=0,
        icons=["bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill"],
        orientation="horizontal",
    )
    selected

    if selected == "1 Relatório Educação":
        screen_componets(baseDeAlunos, baseDeDengue, DB1, baseDeAlunos.shape[0]-DB1.shape[0], "Relatório Educação", "frequenta a escola", "tiveram dengue")
    if selected == "2 Relatório Saúde":
        BaseNaoOnibus = DB.iguais(baseDeDengue, baseDeOnibus)
        screen_componets(baseDeDengue, BaseNaoOnibus, DB2, baseDeDengue.shape[0]-DB2.shape[0], "Relatório Saúde", "frequenta o posto de saúde", "não utilizam ônibus")
    if selected == "3 Relatório Mobilidade":
        BasenaoDengue = DB.iguais(baseDeOnibus, baseDeDengue)
        screen_componets(baseDeOnibus, BasenaoDengue, DB3, baseDeOnibus.shape[0]-DB3.shape[0], "Relatório Mobilidade", "utilizam o transporte público", "não tiveram dengue")
    if selected == "4 Relatório Educação e Saúde":
        screen_componets(baseDeAlunos, baseDeDengue, DB4, DB4.shape[0], "Relatório Educação e Saúde", "frequenta a escola", "tiveram dengue")
    if selected == "5 Relatório Educação e Mobilidade":
        screen_componets(baseDeAlunos, baseDeOnibus,DB5,DB5.shape[0], "Relatório Educação e Mobilidade", "frequenta a escola", "utiliza transporte público.")
    if selected == "6 Relatório Saúde e Mobilidade":
        screen_componets(baseDeDengue, baseDeOnibus, DB6, DB6.shape[0], "Relatório Saúde e Mobilidade", "frequenta o posto de saúde", "utiliza transporte público")
    if selected == "7 Relatório Saúde, Mobilidade e Educação":
        screen_componets_venn3_unweighted(baseDeDengue, baseDeAlunos, baseDeOnibus, DB7, DB7.shape[0], "Relatório Saúde, Mobilidade e Educação", "frequenta o posto de saúde", "frequenta a escola", "utiliza transporte público")
    if selected == "8 Relatório Saúde e Não Mobilidade":
        DB_temp = DB.iguais(baseDeDengue,baseDeOnibus)
        screen_componets(baseDeDengue, baseDeOnibus,DB8, DB_temp.shape[0], "Relatório Saúde e Não Mobilidade", "frequenta o posto de saúde", "não utiliza transporte público")
    if selected == "9 Relatório Saúde e Não Educação":
        BaseNaoAlunos = DB.repetidos(baseDeDengue, baseDeAlunos)
        screen_componets(baseDeDengue, BaseNaoAlunos, DB9, DB9.shape[0], "Relatório Saúde e Não Educação", "frequenta o posto de saúde", "não frequenta a escola")
    if selected == "10 Relatório Saúde, Não Mobilidade e Não Educação":
        BaseNaoOnibus = DB.repetidos(baseDeDengue, baseDeOnibus)
        BaseNaoAlunos = DB.repetidos(baseDeDengue, baseDeAlunos)
        screen_componets_venn3_unweighted(baseDeDengue, BaseNaoAlunos, BaseNaoOnibus, DB10, DB10.shape[0], "Relatório Saúde, Não Mobilidade e Não Educação", "frequenta o posto de saúde", "não frequenta a escola", "não utiliza transporte público")

def screen_componets(DB1, DB2, DB3, G, Title, Label1, Label2):
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns([4, 2])
    col6, col7, col8 = st.columns(3)
    fig, ax = plt.subplots()
    venn2(subsets=(DB1.shape[0], DB2.shape[0], G),
          set_labels=(Label1, Label2, "G"),
          ax=ax,
          subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x/(DB1.shape[0]+DB2.shape[0])):1.0%}" + ")")
    with col2:
        st.write("# "+Title)
    with col4:
        st.dataframe(DB3,width=1200,height=525)
    with col5:
        st.pyplot(fig)
    with col7:
        with open("Relatorios/"+Title+".xlsx", "rb") as template_file:
            template_byte = template_file.read()

        st.download_button(label="Click to Download Excel File",
                           data=template_byte,
                           file_name=Title+".xlsx",
                           mime='application/octet-stream')

def screen_componets_venn3_unweighted(DB1, DB2 , DB4, DB7, G, Title, Label1, Label2, Label3):
    DB3 = DB.iguais(DB1, DB2)
    DB5 = DB.iguais(DB1, DB4)
    DB6 = DB.iguais(DB2, DB4)
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns([3, 2])
    col6, col7, col8 = st.columns(3)
    fig, ax = plt.subplots()
    venn3_unweighted(subsets=(DB1.shape[0], DB2.shape[0], DB3.shape[0], DB4.shape[0], DB5.shape[0], DB6.shape[0], G),
          set_labels=(Label1, Label2, Label3)
          , ax=ax,
            subset_label_formatter=lambda x: str(x) + "\n(" + f"{(x / (DB1.shape[0] + DB2.shape[0] + DB3.shape[0])):1.0%}" + ")"
          )
    with col2:
        st.write("# "+Title)
    with col4:
        st.dataframe(DB7,width=1200,height=525)
    with col5:
        st.pyplot(fig)
    with col7:
        with open("Relatorios/"+Title+".xlsx", "rb") as template_file:
            template_byte = template_file.read()

        st.download_button(label="Click to Download Excel File",
                           data=template_byte,
                           file_name=Title+".xlsx",
                           mime='application/octet-stream')