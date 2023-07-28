import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataPreparationTitanic(object):

    def __init__(self, conf, utils) -> None:
        self.target_col = "Survived"
        self.study_label = "Titanic Survivors"
        self.utils = utils
        self.raw_data = pd.DataFrame()
        self.processed_data = pd.DataFrame()
        self.clean_data = pd.DataFrame()
        self.data_local_train = pd.DataFrame()
        self.data_local_test = pd.DataFrame()
        self.data_folder = conf.params["titanic_data_folder"]
        self.rdn_number = np.random.randint(200)

    def apply(self) -> None:
        self.raw_data = pd.read_csv(f"{self.data_folder}train.csv", sep=',', decimal=',')
        self.preprocess_data()

    def preprocess_data(self, ):
        raw_data = self.raw_data.copy(deep=True)
        raw_data["Age"] = pd.to_numeric(raw_data["Age"], errors='coerce')

        raw_data.rename(columns={"Survived": "target"}, inplace=True)

        self.clean_data = raw_data.copy(deep=True)

        raw_data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)

        raw_data_sex = pd.concat([raw_data, pd.get_dummies(raw_data["Sex"], prefix='sex', drop_first=False)],
                                 axis=1).drop(columns=['Sex'])

        raw_data_sex_embarked = pd.concat(
            [raw_data_sex, pd.get_dummies(raw_data["Embarked"], prefix='embarked', drop_first=False)],
            axis=1).drop(columns=['Embarked'])

        scale = StandardScaler()
        scale.fit(raw_data_sex_embarked.drop("target", axis=1))
        x_scaled = scale.transform(raw_data_sex_embarked.drop("target", axis=1))
        x_scaled = pd.DataFrame(x_scaled, columns=raw_data_sex_embarked.drop("target", axis=1).columns)
        self.processed_data = pd.concat([pd.DataFrame(x_scaled), raw_data_sex_embarked.target], axis=1)

        self.processed_data.fillna(self.processed_data.mean(), inplace=True)

        def sample(group):
            return group.sample(frac=0.8, random_state=self.rdn_number)

        self.data_local_train = self.processed_data.groupby("target", as_index=False).apply(sample). \
            reset_index(drop=True)
        self.data_local_test = self.processed_data.drop(self.data_local_train.index)
