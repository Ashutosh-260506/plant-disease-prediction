import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def create_gradcam_overlay(image, heatmap, alpha=0.45):

    image = image.convert("RGB")

    heatmap_image = Image.fromarray(
        np.uint8(255 * heatmap)
    )

    heatmap_image = heatmap_image.resize(
        image.size,
        Image.Resampling.BILINEAR
    )

    heatmap_array = np.array(
        heatmap_image
    ) / 255.0

    colormap = plt.get_cmap("jet")

    colored_heatmap = colormap(
        heatmap_array
    )[:, :, :3]

    original = np.array(
        image
    ) / 255.0

    overlay = (
        original * (1 - alpha)
        + colored_heatmap * alpha
    )

    overlay = np.uint8(
        np.clip(overlay * 255, 0, 255)
    )

    return Image.fromarray(overlay)