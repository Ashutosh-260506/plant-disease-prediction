# 🌿 PlantLens AI — Plant Disease Prediction

PlantLens AI is an AI-powered plant disease detection system that classifies plant leaf images using a **fine-tuned EfficientNetB0** model and provides an interpretable **Grad-CAM** visualization of the regions influencing each prediction.

The project evaluates three modeling approaches — a baseline **Simple CNN**, **EfficientNetB0 with Transfer Learning**, and **EfficientNetB0 with Fine-Tuning** — with the final fine-tuned EfficientNetB0 model achieving **97.23% validation accuracy**.

---

## 🚀 Features

- 🌱 Plant disease classification across **38 classes**
- 🧠 EfficientNetB0 with transfer learning
- 🔧 EfficientNetB0 fine-tuning
- 🔥 Grad-CAM based model explainability
- 📊 Prediction confidence score
- 🖼️ Original image vs. AI Focus visualization
- 📤 Plant leaf image upload
- 🌐 Streamlit web application
- ☁️ Cloud deployment
- ⚡ CPU-based TensorFlow inference

---

## 🌐 Live Demo

**Live Website:** [Open PlantLens AI](https://plantdiseaseprediction3000.streamlit.app/)

The live application allows users to:

- Upload a plant leaf image
- Predict the plant disease
- View prediction confidence
- Generate a Grad-CAM visualization
- Compare the original image with the AI Focus overlay

---

## 📦 Repository

**Source Code:** [github.com/Ashutosh-260506/plant-disease-prediction](https://github.com/Ashutosh-260506/plant-disease-prediction)

---

## 🎯 Problem Statement

Plant diseases can significantly affect crop productivity and agricultural output. Identifying diseases manually from leaf symptoms can be difficult, especially when different diseases share visually similar characteristics.

PlantLens AI aims to provide an AI-assisted solution that can:

- Analyze plant leaf images
- Identify the most likely disease
- Provide a prediction confidence score
- Highlight important image regions using Grad-CAM
- Provide an accessible, web-based interface

This project is intended as an educational and demonstration application of Deep Learning and Explainable AI for agricultural image classification.

---

## 🏗️ Architecture

```text
                    Plant Leaf Image
                           │
                           ▼
                  Image Preprocessing
                           │
                           ▼
                Fine-Tuned EfficientNetB0
                           │
                           ▼
                  Disease Classification
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
               Prediction      Grad-CAM
                    │             │
                    │             ▼
                    │       Heatmap Generation
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                  Result + AI Focus
```

---

## 🔄 Prediction Pipeline

1. User uploads a plant leaf image
2. Image is converted to RGB
3. Image is resized to 224 × 224
4. Image is passed to EfficientNetB0
5. Model predicts one of 38 classes
6. Highest-probability class is selected
7. Prediction confidence is calculated
8. Grad-CAM generates an activation heatmap
9. Heatmap is resized to image dimensions
10. Heatmap is overlaid on the original image
11. Disease, confidence, and AI Focus are displayed

---

## 🖥️ Application Preview

| Plant Image Upload | Disease Prediction & Grad-CAM |
|---|---|
| ![Upload Screen](docs/upload-screen.png) | ![Result Screen](docs/result-screen.png) |

---

## 📊 Model Performance

Three different approaches were evaluated during development.

| Model | Validation Loss | Validation Accuracy |
|---|---|---|
| Simple CNN | 0.4184 | 86.89% |
| EfficientNetB0 (Transfer Learning) | 0.1176 | 96.08% |
| EfficientNetB0 (Fine-Tuned) | 0.0812 | **97.23%** |

The fine-tuned EfficientNetB0 model was selected as the final model, improving validation accuracy by approximately **10.45 percentage points** over the baseline Simple CNN.

> **Note:** These are validation metrics and should not be interpreted as test-set performance.

### 📈 Accuracy Progression

```text
Simple CNN                    86.89%
    │  +9.19 pts
    ▼
EfficientNetB0                96.08%
    │  +1.15 pts
    ▼
Fine-Tuned EfficientNetB0     97.23%
```

---

## 🧠 Model

The final application uses a fine-tuned EfficientNetB0 model for plant disease classification, developed across three stages:

```text
Simple CNN → EfficientNetB0 Transfer Learning → EfficientNetB0 Fine-Tuning → Final Model
```

### Why EfficientNetB0?

EfficientNetB0 was selected because it provides a strong balance between:

- Classification performance
- Computational efficiency
- Model complexity
- Transfer learning capability

The pretrained network provides useful visual features, while fine-tuning allows the model to adapt those features to the plant disease classification task.

---

## 🔥 Grad-CAM Explainability

PlantLens AI uses **Grad-CAM** (Gradient-weighted Class Activation Mapping) to make model predictions more interpretable.

A traditional image classifier typically only provides output like:

> Disease: *Pepper Bell — Bacterial Spot*
> Confidence: *94.97%*

PlantLens AI additionally generates an **AI Focus** visualization showing the regions that contributed most strongly to the prediction:

```text
Plant Image → EfficientNetB0 → Predicted Class → Gradient Calculation
→ Feature Map Analysis → Grad-CAM Heatmap → AI Focus Overlay
```

Warmer regions generally represent stronger model activation. Grad-CAM provides a visual explanation of the model's decision instead of only returning a class label.

### Example

```text
Plant Leaf Image → Preprocessing → Fine-Tuned EfficientNetB0
→ Disease Prediction → Confidence Score → Grad-CAM Visualization
```

**Output:**
- Disease: *Grape — Black Rot*
- Confidence: *99%+*
- AI Focus: Grad-CAM visualization

---

## 🔬 Image Preprocessing

Uploaded images are processed before being passed to the model:

```text
Input Image → Convert to RGB → Resize to 224 × 224
→ Convert to NumPy Array → Add Batch Dimension → EfficientNetB0
```

The same preprocessing pipeline is used during both model inference and Grad-CAM generation.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Deep Learning | TensorFlow / Keras |
| Baseline Model | Simple CNN |
| Final Model | Fine-Tuned EfficientNetB0 |
| Transfer Learning | EfficientNetB0 |
| Fine-Tuning | EfficientNetB0 |
| Explainable AI | Grad-CAM |
| Web Application | Streamlit |
| Image Processing | Pillow |
| Numerical Computing | NumPy |
| Visualization | Matplotlib |
| Version Control | Git / GitHub |
| Deployment | Streamlit Community Cloud |

---

## 📁 Project Structure

```text
plant-disease-prediction/
│
├── backend/
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── gradcam.py
│   │   ├── main.py
│   │   ├── model.py
│   │   ├── preprocessing.py
│   │   └── visualization.py
│   │
│   ├── model/
│   │   ├── class_names.json
│   │   └── plant_disease_model.keras
│   │
│   └── requirements.txt
│
├── frontend/
├── notebooks/
├── Test_img/
│
├── docs/
│   ├── upload-screen.png.png
│   └── result-screen.png.png
│
├── streamlit_app.py
├── requirements.txt
├── .python-version
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Prerequisites

Make sure the following are installed:

- Python 3.12
- Git

### 💻 Run Locally

**1. Clone the repository**

```bash
git clone https://github.com/Ashutosh-260506/plant-disease-prediction.git
cd plant-disease-prediction
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the Streamlit application**

```bash
streamlit run streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📚 Model Classes

The model supports classification across **38 plant disease classes**.

- Class names: `backend/model/class_names.json`
- Trained model: `backend/model/plant_disease_model.keras`

---

## 📈 Project Evolution

```text
Simple CNN → Transfer Learning → EfficientNetB0 → Fine-Tuning
→ Grad-CAM Explainability → Streamlit Application → Cloud Deployment
```

---

## 🧩 Challenges Solved

**1. Model Performance**
A baseline CNN was initially developed and achieved 86.89% validation accuracy. EfficientNetB0 transfer learning improved performance to 96.08%, and fine-tuning further improved it to 97.23%.

**2. Model Explainability**
A prediction alone does not show *why* a model made a particular decision. Grad-CAM was implemented to visualize the leaf regions that most influenced the model's prediction.

**3. Memory Optimization**
TensorFlow inference and Grad-CAM require additional computational resources. The inference pipeline was optimized to reduce unnecessary memory usage and improve deployment reliability.

**4. Cloud Deployment**
The application was deployed as a Streamlit web app with a compatible Python environment and TensorFlow configuration, running on CPU-based inference.

---

## 💡 Key Learning Outcomes

**Machine Learning**
Image classification, model evaluation, validation metrics, model comparison

**Deep Learning**
Convolutional Neural Networks, transfer learning, EfficientNetB0, fine-tuning, TensorFlow / Keras

**Computer Vision**
Image preprocessing, image resizing, feature extraction, image classification

**Explainable AI**
Grad-CAM, feature maps, gradient-based visualization, model interpretability

**Deployment**
Streamlit, Git, GitHub, cloud deployment, dependency management, CPU-based TensorFlow inference

---

## 🎓 Placement-Relevant Skills

Python · Deep Learning · Computer Vision · TensorFlow / Keras · CNNs · Transfer Learning · Model Fine-Tuning · EfficientNet · Explainable AI · Grad-CAM · Streamlit · Git / GitHub · Machine Learning Deployment · Model Optimization

---

## 🔮 Future Improvements

- Improve model robustness on real-world plant images
- Add more plant species and disease classes
- Improve Grad-CAM visualization quality
- Add prediction history
- Add confidence-based warnings
- Add disease treatment recommendations
- Improve mobile responsiveness
- Optimize inference latency
- Add model monitoring and versioning
- Improve the Streamlit UI
- Add more explainability techniques

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes**. The predictions generated by the system should not be considered a substitute for professional agricultural diagnosis. For real-world crop disease management, please consult qualified agricultural professionals.

---

## 👨‍💻 Author

**Ashutosh Kumar Singh**

- GitHub: [@Ashutosh-260506](https://github.com/Ashutosh-260506)
- Project Repository: [plant-disease-prediction](https://github.com/Ashutosh-260506/plant-disease-prediction)

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub!

---

## 📌 Project Summary

| Attribute | Details |
|---|---|
| Project | PlantLens AI |
| Domain | Artificial Intelligence / Deep Learning |
| Task | Plant Disease Classification |
| Number of Classes | 38 |
| Baseline Model | Simple CNN |
| Transfer Learning Model | EfficientNetB0 |
| Final Model | Fine-Tuned EfficientNetB0 |
| Validation Accuracy | 97.23% |
| Validation Loss | 0.0812 |
| Explainability | Grad-CAM |
| Web Application | Streamlit |
| Deployment | Streamlit Community Cloud |
| Repository | GitHub |

---

**Built With:** Python • TensorFlow • Keras • EfficientNetB0 • Grad-CAM • Streamlit • NumPy • Pillow • Matplotlib • Git • GitHub