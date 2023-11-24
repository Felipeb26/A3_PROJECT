# MY IMPORTS
from email import header
import warnings

import numpy as np
from enums.colum import HEADER
from format.replaces import replace, drop_column
from format.dates import month_to_number, str_to_date
from artificial import ArtificialPrediction

# IMPORTS LIBS
import streamlit as st
import pandas as pd
from IPython.display import display


warnings.filterwarnings("ignore")

header: list = [
    HEADER.NIVEL_TERRITORIAL.value,
    HEADER.NIVEL_TERRITORIAL_COD.value,
    HEADER.UNIDADE_MEDIDA.value,
    # HEADER.UNIDADE_MEDIDA_COD.value,
    HEADER.BRASIL.value,
    HEADER.BRASIL_COD.value,
    HEADER.VARIAVEL.value,
    # HEADER.VARIAVEL_COD.value,
    HEADER.TRIMESTRE_MOVEL.value,
    # HEADER.TRIMESTRE_MOVEL_COD.value,
    HEADER.VALOR.value,
    "MESES",
]

df_analise: pd.DataFrame


def analise_and_filter_data():
    global df_analise
    global header

    st.set_page_config(layout="wide", page_title="DATA ANALISED FOR A3")
    df = pd.read_csv("data.csv", delimiter=";", decimal=".")
    df.drop(index=df.index[0], inplace=True)

    df["ANOS"] = df[HEADER.TRIMESTRE_MOVEL.value].apply(
        lambda x: str(x).split(" ")[1] + "-" + month_to_number(x.split(" ")[0]) + "-01"
    )
    df["MESES"] = df[HEADER.TRIMESTRE_MOVEL.value].apply(
        lambda x: month_to_number(x.split(" ")[0], False)
    )

    df = df.sort_values("MESES")
    meses = st.sidebar.selectbox("MES", df["MESES"].unique())

    st.text(f"{df[HEADER.TRIMESTRE_MOVEL.value].size} Itens sem analise e filtro")

    df = replace(df, HEADER.UNIDADE_MEDIDA, ["Ponto percentual", "Nenhuma"], "%")
    df = replace(df, HEADER.VALOR, ["A", "Z"], "0")

    df = df.dropna()
    df.to_csv("./filtered_data.csv")

    df_analise = df
    df_analise[HEADER.VARIAVEL_COD.value] = df_analise[HEADER.VARIAVEL_COD.value].apply(
        lambda x: int(x)
    )
    df_analise.sort_values(HEADER.VARIAVEL_COD.value)
    df_analise = drop_column(df, header)
    # df_analise= df_analise.drop(df_analise.columns[[0,1,2,3,4]],axis=1)
    # df_analise = df_analise.assign(df_analise,lambda x: df[HEADER.TRIMESTRE_MOVEL.value])
    # df_analise.loc[:, "VARIAVEL"] = df[HEADER.TRIMESTRE_MOVEL.value].values.tolist()

    df_filtered: pd.DataFrame = df[df["MESES"] == meses]

    st.text(f"{df[HEADER.TRIMESTRE_MOVEL.value].size} Itens Sem valores nulos ")
    print(type(st))
    st.text(
        f"{df_filtered[HEADER.TRIMESTRE_MOVEL.value].size} Itens filtrados pelo Mes {meses}"
    )

    df_filtered
    df_analise
    artificial = ArtificialPrediction(df_analise)

    artificial.setDataFrame(df_analise)
    artificial.createLinearRegression()


analise_and_filter_data()
