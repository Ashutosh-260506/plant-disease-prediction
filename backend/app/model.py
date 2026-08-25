import json
import os

# Force TensorFlow to use CPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "plant_disease_model.keras"
)

CLASS_NAMES_PATH = os.path.join(
    BASE_DIR,
    "model",
    "class_names.json"
)


# Load model once when the application starts
model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)


with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)


print("Model loaded successfully")
print("Number of classes:", len(class_names))