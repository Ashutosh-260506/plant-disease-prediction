from PIL import Image
import numpy as np


IMAGE_SIZE = (224, 224)


def preprocess_image(image: Image.Image):

    image = image.convert("RGB")

    image = image.resize(IMAGE_SIZE)

    image_array = np.array(image)

    image_array = np.expand_dims(image_array, axis=0)

    return image_array