import json
import os
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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


model = tf.keras.models.load_model(MODEL_PATH)


with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)


print("Model loaded successfully")
print("Number of classes:", len(class_names))