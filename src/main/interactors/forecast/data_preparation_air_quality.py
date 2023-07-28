import numpy as np
import pandas as pd


class DataPreparationAirQuality(object):

    def __init__(self, conf, utils, raw_repo, processed_repo) -> None:
        self.target_col = "CO(GT)"
        self.study_label = "Air Quality"
        self.utils = utils
        self.processed_data = pd.DataFrame()
        self.is_seasonal = False
        self.data_folder = conf.params["air_quality_data_folder"]

    def apply(self) -> None:
        raw_data = pd.read_csv(f"{self.data_folder}AirQualityUCI.csv", sep=';', decimal=',')
        self.processed_data = self.prepare_data(raw_data)
        print(
            f"The sample time series is seasonal before the deseasonality "
            f"{self.utils.is_seasonal(self.processed_data, self.target_col)}"
        )
        self.processed_data[self.target_col + "_deseasonalize"] = self.utils.deseasonalize_data(
            data=self.processed_data, column_name=self.target_col, make_plot=False)
        print(
            f"The sample time series is seasonal after the deseasonality "
            f"{self.utils.is_seasonal(self.processed_data, self.target_col)}"
        )
        self.utils.seasonal_decomposition(
            data=self.processed_data, column_name=f"{self.target_col}_deseasonalize", make_plot=False)

    @staticmethod
    def prepare_data(raw_data) -> pd.DataFrame:
        data = raw_data.copy(deep=True)
        data.drop(columns=["Unnamed: 15", "Unnamed: 16"], inplace=True)
        data.dropna(axis=0, inplace=True)  # Drop rows with missing values
        print(data.shape)
        target_col = "CO(GT)"
        data.dropna(subset=[target_col], inplace=True)
        pd.to_datetime(data["Date"] + " " + data["Time"], format="%d/%m/%Y %H.%M.%S")
        data["datetime"] = pd.to_datetime(data["Date"] + " " + data["Time"], format="%d/%m/%Y %H.%M.%S")
        data.drop(columns=["Date", "Time"], inplace=True)
        data.set_index("datetime", inplace=True)
        return data

