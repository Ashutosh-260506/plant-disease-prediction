import os
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import streamlit as st
from PIL import Image


# --------------------------------------------------
# Project paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

BACKEND_DIR = os.path.join(
    BASE_DIR,
    "backend"
)

sys.path.insert(
    0,
    BACKEND_DIR
)


# --------------------------------------------------
# Existing backend modules
# --------------------------------------------------

from app.model import model, class_names
from app.preprocessing import preprocess_image
from app.gradcam import make_gradcam_heatmap
from app.visualization import create_gradcam_overlay


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="PlantLens AI",
    page_icon="🌿",
    layout="centered"
)


# --------------------------------------------------
# Styling
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #444;
        margin-top: 20px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🌿 PlantLens AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered plant disease detection with Grad-CAM'
    '</div>',
    unsafe_allow_html=True
)

st.caption(
    f"EfficientNetB0 • {len(class_names)} classes"
)


# --------------------------------------------------
# Upload image
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a plant image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ]
)


# --------------------------------------------------
# Analyze image
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        image,
        caption="Uploaded plant image",
        use_container_width=True
    )

    if st.button(
        "🔍 Analyze Plant Health",
        use_container_width=True
    ):

        try:

            with st.spinner(
                "Analyzing plant health..."
            ):

                # Use your original preprocessing
                img_array = preprocess_image(
                    image
                )

                # Model prediction
                predictions = model.predict(
                    img_array,
                    verbose=0
                )[0]

                predicted_class = int(
                    predictions.argmax()
                )

                confidence = float(
                    predictions[predicted_class]
                )

                # Grad-CAM
                heatmap = make_gradcam_heatmap(
                    img_array,
                    predicted_class
                )

                # Create overlay
                gradcam_image = create_gradcam_overlay(
                    image,
                    heatmap
                )

            disease = class_names[
                predicted_class
            ]

            confidence_percent = (
                confidence * 100
            )


            # --------------------------------------------------
            # Result
            # --------------------------------------------------

            st.success(
                "Plant analysis complete!"
            )

            st.markdown(
                f"""
                <div class="result-box">

                <h2>{disease}</h2>

                <h3>
                Confidence: {confidence_percent:.2f}%
                </h3>

                </div>
                """,
                unsafe_allow_html=True
            )


            # --------------------------------------------------
            # Confidence bar
            # --------------------------------------------------

            st.progress(
                confidence
            )


            # --------------------------------------------------
            # Grad-CAM
            # --------------------------------------------------

            st.subheader(
                "AI Focus"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.image(
                    image,
                    caption="Original Image",
                    use_container_width=True
                )

            with col2:

                st.image(
                    gradcam_image,
                    caption="Grad-CAM",
                    use_container_width=True
                )


            st.info(
                "AI Focus highlights the regions "
                "that contributed most strongly "
                "to the model's prediction."
            )


        except Exception as e:

            st.error(
                "Failed to analyze the image."
            )

            st.exception(e)