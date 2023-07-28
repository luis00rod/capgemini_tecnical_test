# This program classifies the type of volcano based on the vibrations detected by sensors.
import operator
import pdb
import pickle

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler


class ClassificatorTitanic:

    def __init__(self, conf):
        self.model = None
        self.data_train = pd.DataFrame()
        self.data_local_train = pd.DataFrame()
        self.data_local_test = pd.DataFrame()
        self.prediction = pd.DataFrame()
        self.best_params = {"n_estimators": 50, "max_depth": 3, "random_state": 2}
        self.models_f1_scores = dict()
        self.data_folder = conf.params["titanic_data_folder"]
        self.rdn_number = np.random.randint(200)

    def apply(self, data):
        self.data_local_train = data.data_local_train.copy(deep=True)
        self.data_local_test = data.data_local_test.copy(deep=True)
        self.train_model()

    def train_model(self):
        sk_fold = StratifiedKFold(n_splits=4, shuffle=True, random_state=self.rdn_number)

        self.model = RandomForestClassifier(n_estimators=self.best_params['n_estimators'],
                                            max_depth=self.best_params['max_depth'],
                                            random_state=self.rdn_number)

        x_train = self.data_local_train.drop("target", axis=1)
        y_train = self.data_local_train.target

        for (train_index, test_index) in sk_fold.split(self.data_local_train, self.data_local_train['target']):

            self.model.fit(x_train.iloc[train_index], y_train.iloc[train_index])
            self.prediction = self.model.predict(x_train.iloc[test_index])
            f1_score = metrics.f1_score(y_train.iloc[test_index], self.prediction, average='macro')
            self.models_f1_scores[self.model] = f1_score
            print("F1 score for model: ", str(self.model), " is: ", f1_score)
            print("models_f1_scores", self.models_f1_scores)

            print("\n")

        self.models_f1_scores = sorted(self.models_f1_scores.items(), key=operator.itemgetter(1), reverse=True)
        print("models_f1_scores_sorted", self.models_f1_scores)

        pass

    def evaluate_model(self):
        x_test = self.data_local_test.drop("target", axis=1)
        y_test = self.data_local_test.target

        y_prediction = self.model.predict(x_test)
        print("Local TEST", metrics.f1_score(y_test, y_prediction, average='macro'))

        y_prediction = self.model.predict(self.data_local_test.drop("target", axis=1))
        pd.DataFrame(y_prediction, columns=["target"]).to_csv(f"{self.data_folder}y_prediction.csv", header=True,
                                                              index=False)
