from repositories.raw_repository import RawRepo
from repositories.processed_repository import ProcessedRepo
from interactors.classificator.data_preparation_titanic import DataPreparationTitanic
from interactors.forecast.data_preparation_air_quality import DataPreparationAirQuality
from interactors.classificator.classificator_titanic import ClassificatorTitanic
from interactors.forecast.forecast_nn import AirQualityPredictor
from pipelines.forecast_pipeline import Pipeline
from utils.functions import Functions


class Main(object):

    def __init__(self, conf):
        raw_repo = RawRepo(conf)
        processed_repo = ProcessedRepo(conf)
        utils = Functions()

        self.pipeline = Pipeline(
            data_preparation_titanic=DataPreparationTitanic(conf, utils),
            data_preparation_air_quality=DataPreparationAirQuality(conf, utils, raw_repo, processed_repo),
            model_titanic=ClassificatorTitanic(conf),
            model_air_quality=AirQualityPredictor()
        )
