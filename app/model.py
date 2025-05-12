import pickle
import numpy as np


def from_log(n: int):
    return np.exp(n)-1


class Model():
    def __init__(self):
        with open("app/static/data/gbr_model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, sample):
        return from_log(self.model.predict(sample))[0]
