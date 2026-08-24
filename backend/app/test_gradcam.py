import tensorflow as tf


from app.model import model, class_names
from app.preprocessing import preprocess_image
from app.gradcam import make_gradcam_heatmap
from app.visualization import create_gradcam_overlay

image = tf.keras.utils.load_img(
    r"C:\Users\ASHUTOSH KUMAR\OneDrive\Desktop\AI-ML\projects\P3-Plant-Disease-Prediction\Test_img\Grape_blackRot.jpg"
)

img_array = preprocess_image(image)

print("Image shape:", img_array.shape)

predictions = model.predict(img_array, verbose=0)

predicted_class = int(tf.argmax(predictions[0]))

print("Predicted class ID:", predicted_class)
print("Predicted class:", class_names[predicted_class])

heatmap = make_gradcam_heatmap(
    img_array,
    predicted_class
)

print("Heatmap shape:", heatmap.shape)

overlay = create_gradcam_overlay(
    image,
    heatmap
)

overlay.save(
    "gradcam_result.jpg"
)

print("Grad-CAM image saved successfully")