import pandas as pd


class Pipeline(object):

    def __init__(self, data_preparation_air_quality, data_preparation_titanic, model_titanic, model_air_quality):
        self.data_preparation_air_quality = data_preparation_air_quality
        self.data_preparation_titanic = data_preparation_titanic
        self.model_titanic = model_titanic
        self.model_air_quality = model_air_quality
        pass

    def run(self):
        self.data_preparation_air_quality.apply()
        self.data_preparation_titanic.apply()
        results_titanic = self.model_titanic.apply(data=self.data_preparation_titanic)
        results_air_quality = self.AirQualityPredictor.apply(data=self.data_preparation_air_quality)
        return

