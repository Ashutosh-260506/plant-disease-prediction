import numpy as np
from PIL import Image


def create_gradcam_overlay(
    image,
    heatmap,
    alpha=0.45
):

    image = image.convert("RGB")

    # Convert heatmap to 0-255
    heatmap_uint8 = np.uint8(
        np.clip(heatmap, 0, 1) * 255
    )

    # Resize heatmap to original image size
    heatmap_image = Image.fromarray(
        heatmap_uint8,
        mode="L"
    )

    heatmap_image = heatmap_image.resize(
        image.size,
        Image.Resampling.BILINEAR
    )

    heatmap_array = np.asarray(
        heatmap_image,
        dtype=np.float32
    ) / 255.0

    # --------------------------------------------------
    # Lightweight JET-like color mapping
    # --------------------------------------------------

    red = np.clip(
        1.5 - np.abs(4 * heatmap_array - 3),
        0,
        1
    )

    green = np.clip(
        1.5 - np.abs(4 * heatmap_array - 2),
        0,
        1
    )

    blue = np.clip(
        1.5 - np.abs(4 * heatmap_array - 1),
        0,
        1
    )

    colored_heatmap = np.stack(
        [red, green, blue],
        axis=-1
    )

    # Original image
    original = np.asarray(
        image,
        dtype=np.float32
    ) / 255.0

    # Blend
    overlay = (
        original * (1 - alpha)
        + colored_heatmap * alpha
    )

    overlay = np.uint8(
        np.clip(
            overlay * 255,
            0,
            255
        )
    )

    return Image.fromarray(
        overlay,
        mode="RGB"
    )