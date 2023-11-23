from pandas import DataFrame

dataframe: DataFrame | list = []


class ArtificialPrediction:
    def __init__(self, data_frame):
        self.dataFrame = data_frame

    def setDataFrame(self):
        global dataframe
        dataframe = self.dataFrame