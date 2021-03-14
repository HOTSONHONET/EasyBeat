from tensorflow.keras.models import load_model
from tensorflow.keras.losses import mean_squared_error
import numpy as np
import json


class AE:
    def __init__(self, model_path = ".//FlaskApp//utils//ecg_ae.h5",
            threshold = 0.018511625084178192):

        self.model = load_model(model_path)       
        self.threshold = threshold

    def predict(self, data):
        data = np.array([data])
        predicted_ecg = self.model.predict(data)
        loss = mean_squared_error(predicted_ecg, data).numpy()[0][0]
        verdict = 'Abnormal ☠' if (loss > self.threshold) else 'Normal ❤️'
        to_give = {'loss' : loss,'verdict' : verdict}

        return to_give


