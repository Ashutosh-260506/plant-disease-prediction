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
# Existing ML modules
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
# Custom CSS
# --------------------------------------------------

st.markdown(
    """
<style>

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Brand */

.brand {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 45px;
}

/* Hero */

.hero {
    text-align: center;
    margin-bottom: 35px;
}

.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    background-color: #e8f7ed;
    color: #237a3b;
    font-size: 12px;
    font-weight: 600;
}

.hero-title {
    font-size: 46px;
    line-height: 1.1;
    margin: 18px 0 12px 0;
    font-weight: 700;
}

.hero-subtitle {
    font-size: 17px;
    color: #6b7280;
}

/* Model information */

.model-info {
    text-align: center;
    color: #7a827c;
    font-size: 13px;
    margin-bottom: 25px;
}

/* Result card */

.result-card {
    border: 1px solid #d9e2dc;
    border-radius: 15px;
    padding: 24px;
    margin-top: 25px;
    margin-bottom: 20px;
    text-align: center;
    background-color: #f8faf9;
}

.result-disease {
    font-size: 24px;
    font-weight: 700;
}

.result-confidence {
    font-size: 17px;
    color: #59635c;
    margin-top: 8px;
}

/* Footer */

.footer {
    text-align: center;
    color: #8a918c;
    font-size: 13px;
    margin-top: 50px;
}

</style>
""",
    unsafe_allow_html=True
)


# --------------------------------------------------
# Brand
# --------------------------------------------------

st.markdown(
    '<div class="brand">🌿 PlantLens AI</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Hero section
# --------------------------------------------------

st.markdown(
    '<div class="hero">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="badge">🌱 AI POWERED PLANT HEALTH</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">See the health<br>of your plants.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Upload a plant image and let AI analyze its health.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# Model information
# --------------------------------------------------

st.markdown(
    f"""
<div class="model-info">
    EfficientNetB0 • {len(class_names)} disease classes
</div>
""",
    unsafe_allow_html=True
)


# --------------------------------------------------
# Image upload
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
# Display uploaded image
# --------------------------------------------------

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        image,
        caption=uploaded_file.name,
        use_container_width=True
    )


    # --------------------------------------------------
    # Analyze button
    # --------------------------------------------------

    analyze = st.button(
        "🔍 Analyze Plant Health",
        use_container_width=True
    )


    if analyze:

        try:

            with st.spinner(
                "Analyzing your plant..."
            ):

                # ------------------------------------------
                # Original preprocessing
                # ------------------------------------------

                img_array = preprocess_image(
                    image
                )


                # ------------------------------------------
                # Model prediction
                # ------------------------------------------

                predictions = model.predict(
                    img_array,
                    verbose=0
                )[0]


                predicted_class = int(
                    predictions.argmax()
                )


                confidence = float(
                    predictions[
                        predicted_class
                    ]
                )


                # ------------------------------------------
                # Grad-CAM
                # ------------------------------------------

                heatmap = make_gradcam_heatmap(
                    img_array,
                    predicted_class
                )


                # ------------------------------------------
                # Create Grad-CAM overlay
                # ------------------------------------------

                gradcam_image = create_gradcam_overlay(
                    image,
                    heatmap
                )


            # ------------------------------------------
            # Prediction result
            # ------------------------------------------

            disease = class_names[
                predicted_class
            ]


            confidence_percent = (
                confidence * 100
            )


            # ------------------------------------------
            # Success message
            # ------------------------------------------

            st.success(
                "Plant analysis complete!"
            )


            # ------------------------------------------
            # Result card
            # ------------------------------------------

            st.markdown(
                f"""
<div class="result-card">
    <div class="result-disease">
        {disease}
    </div>
    <div class="result-confidence">
        Confidence: {confidence_percent:.2f}%
    </div>
</div>
""",
                unsafe_allow_html=True
            )


            # ------------------------------------------
            # Confidence
            # ------------------------------------------

            st.progress(
                confidence
            )


            # ------------------------------------------
            # AI Focus
            # ------------------------------------------

            st.subheader(
                "🔥 AI Focus"
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


            # ------------------------------------------
            # Explanation
            # ------------------------------------------

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


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'PlantLens AI • EfficientNetB0 • Grad-CAM'
    '</div>',
    unsafe_allow_html=True
)