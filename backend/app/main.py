import base64
from io import BytesIO

import numpy as np
from fastapi import FastAPI, UploadFile, File
from PIL import Image

from app.model import model, class_names
from app.preprocessing import preprocess_image
from app.gradcam import make_gradcam_heatmap
from app.visualization import create_gradcam_overlay

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Plant Disease AI API is running"
    }


@app.get("/model-info")
def model_info():
    return {
        "model": "EfficientNetB0",
        "number_of_classes": len(class_names)
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_data = await file.read()

    image = Image.open(
        BytesIO(image_data)
    )

    img_array = preprocess_image(
        image
    )

    predictions = model.predict(
        img_array,
        verbose=0
    )[0]

    predicted_class = int(
        np.argmax(predictions)
    )

    confidence = float(
        predictions[predicted_class]
    )

    heatmap = make_gradcam_heatmap(
        img_array,
        predicted_class
    )

    overlay = create_gradcam_overlay(
        image,
        heatmap
    )

    buffer = BytesIO()

    overlay.save(
        buffer,
        format="JPEG"
    )

    gradcam_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    return {
        "disease": class_names[predicted_class],
        "confidence": confidence,
        "gradcam": gradcam_base64
    }