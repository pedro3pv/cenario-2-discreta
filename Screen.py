import streamlit as st
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import pandas as pd

baseDeAlunos = pd.read_csv("DB/Base de Alunos7.csv", sep=";")
baseDeDengue = pd.read_csv("DB/Base de Dengue7.csv", sep=";")
baseDeOnibus = pd.read_csv("DB/Base de Onibus7.csv", encoding="cp1252", sep=";")

def render(DB1, DB2, DB3, DB4, DB5, DB6, DB7, DB8, DB9, DB10):
    st.set_page_config(layout="wide")

    #col1, col2, col3 = st.columns(3)
    st.dataframe(DB1)

    #fig, ax = plt.subplots()
    #venn2(subsets=(baseDeAlunos.shape[0], baseDeDengue.shape[0], DB1.shape[0]),
    #      set_labels=("Frequentaram a escola", "Tiveram dengue", "G"), ax=ax)
    #st.pyplot(fig)