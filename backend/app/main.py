import asyncio
import base64
import gc
from io import BytesIO

import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

from app.model import model, class_names
from app.preprocessing import preprocess_image
from app.gradcam import make_gradcam_heatmap
from app.visualization import create_gradcam_overlay


app = FastAPI()


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Prediction lock
# Prevent multiple TensorFlow predictions from
# running simultaneously on the small Render instance.
# --------------------------------------------------

prediction_lock = asyncio.Lock()


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Plant Disease AI API is running"
    }


# --------------------------------------------------
# Model information
# --------------------------------------------------

@app.get("/model-info")
def model_info():
    return {
        "model": "EfficientNetB0",
        "number_of_classes": len(class_names)
    }


# --------------------------------------------------
# Prediction
# --------------------------------------------------

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    async with prediction_lock:

        image_data = None
        image = None
        img_array = None
        predictions = None
        heatmap = None
        overlay = None
        buffer = None

        try:

            # --------------------------------------------------
            # Read uploaded image
            # --------------------------------------------------

            image_data = await file.read()

            image = Image.open(
                BytesIO(image_data)
            ).convert("RGB")


            # --------------------------------------------------
            # Preprocess image
            # --------------------------------------------------

            img_array = preprocess_image(
                image
            )


            # --------------------------------------------------
            # Model prediction
            # --------------------------------------------------

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


            # --------------------------------------------------
            # Grad-CAM
            # --------------------------------------------------

            heatmap = make_gradcam_heatmap(
                img_array,
                predicted_class
            )


            # --------------------------------------------------
            # Create Grad-CAM overlay
            # --------------------------------------------------

            overlay = create_gradcam_overlay(
                image,
                heatmap
            )


            # --------------------------------------------------
            # Convert overlay to Base64
            # --------------------------------------------------

            buffer = BytesIO()

            overlay.save(
                buffer,
                format="JPEG",
                quality=85,
                optimize=True
            )

            gradcam_base64 = base64.b64encode(
                buffer.getvalue()
            ).decode("utf-8")


            # --------------------------------------------------
            # Prepare response
            # --------------------------------------------------

            result = {
                "disease": class_names[predicted_class],
                "confidence": confidence,
                "gradcam": gradcam_base64
            }


            return result


        finally:

            # --------------------------------------------------
            # Explicitly release temporary objects
            # --------------------------------------------------

            del image_data
            del image
            del img_array
            del predictions
            del heatmap
            del overlay
            del buffer

            # Ask Python to release unused objects
            gc.collect()