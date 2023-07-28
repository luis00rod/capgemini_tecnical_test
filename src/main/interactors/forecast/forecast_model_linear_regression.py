import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


class Model(object):

    def __init__(self, utils) -> None:
        self.target_col = str
        self.study_label = str
        self.utils = utils
        self.raw_time_series = pd.DataFrame()
        self.datasets_for_model = pd.DataFrame()
        self.future_predictions = pd.DataFrame()
        self.scaler = StandardScaler()

    def apply(self, data) -> None:
        self.study_label = data.study_label
        self.target_col = data.target_col
        self.raw_time_series = data.processed_data.copy(deep=True)
        self.datasets_for_model = self.data_preparation_for_model()
        self.future_predictions = self.forecast()
        self.plotter()
        self.utils.evaluate_prediction(self.future_predictions, self.target_col)

    def forecast(self) -> pd.DataFrame:
        data = self.raw_time_series.copy(deep=True)
        datasets = self.datasets_for_model.copy()
        model = LinearRegression()
        model.fit(datasets["x_train_scaled"], datasets["y_train"])
        x = data.drop(self.target_col, axis=1)

        future_time_instants = data.index[-100:]
        future_data = data.loc[future_time_instants, x.columns]
        future_data_scaled = self.scaler.transform(future_data)
        future_predictions = model.predict(future_data_scaled)
        future_predictions_df = pd.DataFrame(future_predictions, index=future_time_instants,
                                             columns=[f"{self.target_col}_Predicted"])
        results = pd.concat([data.iloc[-100:], future_predictions_df], axis=1)
        return results[[self.target_col, f"{self.target_col}_Predicted"]]

    def data_preparation_for_model(self) -> dict:
        data = self.raw_time_series.copy(deep=True)
        x = data.drop(self.target_col, axis=1)
        y = data[self.target_col]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        return {
            "x_train_scaled": self.scaler.fit_transform(x_train),
            "x_test": x_test,
            "y_train": y_train,
            "y_test": y_test}

    def plotter(self) -> None:
        plt.figure(figsize=(12, 6))
        plt.plot(self.future_predictions.index, self.future_predictions[self.target_col],
                 label="Actual Values", color="blue")
        plt.plot(self.future_predictions.index, self.future_predictions[f"{self.target_col}_Predicted"],
                 label="Predictions", color="red")
        plt.xlabel("Time")
        plt.ylabel(f"{self.target_col} Value")
        plt.title(f"Actual Values vs. Predictions for Future Time Instants {self.study_label}")
        plt.legend()
        plt.show()
