# smartheat/model.py
import tensorflow as tf

class ModelHandler:
    def __init__(self):
        self.model = tf.keras.models.load_model("../savedfiles/breast_detect.h5")

    def predict(self, input_data):
        return self.model.predict(input_data)
