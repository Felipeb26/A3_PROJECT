# MY IMPORTS
import warnings
from enums.colum import HEADER
from format.replaces import replace
from ia.artificial import ArtificialPrediction
# IMPORTS LIBS
import streamlit as st
import pandas as pd
from pandas import DataFrame
from IPython.display import display


warnings.filterwarnings("ignore")


def analise_and_filter_data():
    st.set_page_config(layout="wide", page_title="DATA ANALISED FOR A3")
    df = pd.read_csv("data.csv", delimiter=";", decimal=".")
    df.drop(index=df.index[0], inplace=True)

    df["ANOS"] = df[HEADER.TRIMESTRE_MOVEL.value].apply(
        lambda x: (str(x).split(" ")[1]))

    df = df.sort_values("ANOS")
    anos = st.sidebar.selectbox("ANO", df["ANOS"].unique())

    st.text(
        f"{df[HEADER.TRIMESTRE_MOVEL.value].size} Itens sem analise e filtro")

    df = replace(df, HEADER.UNIDADE_MEDIDA, ["Ponto percentual", "Nenhuma"], "%")
    df = replace(df, HEADER.VALOR, ["A", "Z"], "0")

    df = df.dropna()
    df_filtered: DataFrame = df[df["ANOS"] == anos]

    st.text(f"{df[HEADER.TRIMESTRE_MOVEL.value].size} Itens Sem valores nulos ")
    print(type(st))
    st.text(
        f"{df_filtered[HEADER.TRIMESTRE_MOVEL.value].size} Itens filtrados pelo ano {anos}")

    df_filtered
    ArtificialPrediction(df_filtered)


analise_and_filter_data()
