class Params(object):

    def __init__(self, **kwargs):
        self.params = self.get_params(**kwargs)

    def get_params(self, **kwargs) -> dict:
        air_quality_data_folder = "C:/Users/Asus/Desktop/capgemini_test/data_air_quality/"
        titanic_data_folder = "C:/Users/Asus/Desktop/capgemini_test/data_titanic/"

        default_params = {
            "air_quality_data_folder": air_quality_data_folder,
            "titanic_data_folder": titanic_data_folder,
        }

        default_params.update(kwargs)

        return default_params
