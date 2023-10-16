from streamlit_option_menu import option_menu
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
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
            "Relatório Educação",
            "Relatório Saúde",
            "Relatório Mobilidade",
            "Relatório Educação e Saúde",
            "Relatório Educação e Mobilidade",
            "Relatório Saúde e Mobilidade",
            "Relatório Saúde, Mobilidade e Educação",
            "Relatório Saúde e Não Mobilidade",
            "Relatório Saúde e Não Educação",
            "Relatório Saúde, Não Mobilidade e Não Educação",
        ],
        default_index=0,
        icons=["bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill", "bi-file-earmark-fill"],
        orientation="horizontal",
    )
    selected

    if selected == "Relatório Educação":
        screen_componets(baseDeAlunos, baseDeDengue, DB1, "Relatório Educação", "frequenta a escola", "tiveram dengue")
    if selected == "Relatório Saúde":
        BaseNaoOnibus = DB.iguais(baseDeDengue, baseDeOnibus)
        screen_componets(baseDeDengue, BaseNaoOnibus, DB2, "Relatório Saúde", "frequenta o posto de saúde", "não utilizam ônibus")
    if selected == "Relatório Mobilidade":
        BasenaoDengue = DB.iguais(baseDeOnibus, baseDeDengue)
        screen_componets(baseDeOnibus, BasenaoDengue, DB3, "Relatório Mobilidade", "utilizam o transporte público", "não tiveram dengue")
    if selected == "Relatório Educação e Saúde":
        screen_componets(baseDeAlunos, baseDeDengue, DB4, "Relatório Educação e Saúde", "frequenta a escola", "tiveram dengue")

def screen_componets(DB1, DB2, DB3, Title, Label1, Label2):
    col1, col2, col3 = st.columns(3)
    col4, col5 = st.columns([3, 2])
    fig, ax = plt.subplots()
    venn2(subsets=(DB1.shape[0], DB2.shape[0], DB3.shape[0]),
          set_labels=(Label1, Label2, "G"), ax=ax)
    with col2:
        st.write("# "+Title)
    with col4:
        st.dataframe(DB3,width=1200,height=525)
    with col5:
        st.pyplot(fig)