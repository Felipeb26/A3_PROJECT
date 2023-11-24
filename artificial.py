import re
from turtle import color
from numpy import ndarray
import numpy as np
import pandas as pd
from IPython.display import display
from pandas import DataFrame
from sklearn import linear_model
import matplotlib.pyplot as plt
from enums.colum import HEADER


class ArtificialPrediction:
    def __init__(self, data_frame: DataFrame):
        self.df = (
            data_frame if data_frame is not None else pd.read_csv("filtered_data.csv")
        )

    def setDataFrame(self, data: DataFrame):
        self.df = data

    def createLinearRegression(self):
        self.df.sort_values("ANOS")
        reg = linear_model.LinearRegression()
        plt.scatter(
            self.df["ANOS"],
            self.df[HEADER.VARIAVEL_COD.value],
        )

        series_x = self.df["ANOS"]
        series_y = self.df[HEADER.VARIAVEL_COD.value]

        x0 = ndarray_to_array(series_x.unique(), [])
        y0 = ndarray_to_array(series_y.unique(), x0)

        plt.show()

        plt.plot(x0, y0, "r")
        plt.show()

        reg.fit(
            self.df[HEADER.TRIMESTRE_MOVEL_COD.value].values.reshape(-1,1),
            self.df[HEADER.VARIAVEL_COD.value],
        )
        print(reg.coef_)
        print(reg.predict([[75]]))

        plt.scatter(
            self.df[HEADER.TRIMESTRE_MOVEL_COD.value],
            self.df[HEADER.VARIAVEL_COD.value],
        )
        plt.scatter(75, reg.predict([[75]])[0], color="k")
        x = ndarray_to_array(self.df[HEADER.TRIMESTRE_MOVEL_COD.value], [])
        # reg.intercept_+x*reg.coef_
        # y =  calc_array(x,reg.intercept_, reg.coef_)
        y = reg.intercept_ + arrays_to_float(x) * reg.coef_
        plt.plot(x, y, "r")
        plt.show()


# 14:13


def encontraY(x_reta, y_reta, x):
    a = (y_reta[1] - y_reta[0]) / (x_reta[1] - x_reta[0])
    b = y_reta[1] - a * x_reta[1]
    y = a * x + b
    print(y)
    return y


def ndarray_to_array(values: ndarray, list: list):
    array = []
    if len(list) > 0:
        for value in values:
            if len(array) < len(list):
                array.append(value)
    else:
        for value in values:
            if len(array) < 3:
                array.append(value)
    return array


def arrays_to_float(list: list):
    array = []
    for item in list:
        array.append(float(item))
    return array
