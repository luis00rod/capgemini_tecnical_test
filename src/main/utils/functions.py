import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.seasonal import STL
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class Functions(object):

    def __init__(self, **kwargs):
        pass

    @staticmethod
    def is_seasonal(data: pd.DataFrame, column_name: str) -> bool:
        if adfuller(data[column_name].tolist())[1] > 0.05:
            return True
        else:
            return False

    @staticmethod
    def seasonal_decomposition(data: pd.DataFrame, column_name: str, make_plot: bool, model='additive'):
        decomposition = seasonal_decompose(data[column_name], model=model)

        if make_plot:
            plt.figure(figsize=(12, 8))
            plt.subplot(4, 1, 1)
            plt.plot(data[column_name], label='Original')
            plt.legend(loc='upper left')
            plt.subplot(4, 1, 2)
            plt.plot(decomposition.trend, label='Trend')
            plt.legend(loc='upper left')
            plt.subplot(4, 1, 3)
            plt.plot(decomposition.seasonal, label='Seasonality')
            plt.legend(loc='upper left')
            plt.subplot(4, 1, 4)
            plt.plot(decomposition.resid, label='Residuals')
            plt.legend(loc='upper left')
            plt.tight_layout()
            plt.show()
        return decomposition

    @staticmethod
    def deseasonalize_data(data: pd.DataFrame, column_name: str, make_plot: bool, seasonal_period=7):

        decomposition = STL(data[column_name], seasonal=seasonal_period)
        result = decomposition.fit()

        deseasonalized_data = data[column_name] - result.seasonal

        if make_plot:
            plt.figure(figsize=(12, 6))
            plt.plot(data[column_name], label='Original')
            plt.plot(deseasonalized_data, label='Deseasonalized')
            plt.legend(loc='upper left')
            plt.xlabel('Date')
            plt.ylabel(column_name)
            plt.title('Deseasonalized Data')
            plt.show()
        return deseasonalized_data

    @staticmethod
    def evaluate_prediction(raw_data_and_simulated_data: pd.DataFrame, target_col: str):
        mae = mean_absolute_error(raw_data_and_simulated_data[target_col],
                                  raw_data_and_simulated_data[target_col + '_Predicted'])
        mse = mean_squared_error(raw_data_and_simulated_data[target_col],
                                 raw_data_and_simulated_data[target_col + '_Predicted'])
        rmse = np.sqrt(mse)
        r2 = r2_score(raw_data_and_simulated_data[target_col], raw_data_and_simulated_data[target_col + '_Predicted'])

        print("Evaluation Metrics:")
        print("Mean Absolute Error (MAE):", mae)
        print("Mean Squared Error (MSE):", mse)
        print("Root Mean Squared Error (RMSE):", rmse)
        print("R-squared (R2) Score:", r2)






