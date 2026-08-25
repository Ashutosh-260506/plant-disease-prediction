import tensorflow as tf

from app.model import model


# EfficientNetB0 is the second layer of the outer model
efficientnet = model.layers[1]

# Final classifier layer
dense_layer = model.layers[4]

# Last convolutional feature layer
top_conv_layer = efficientnet.get_layer("top_conv")


# Grad-CAM model
grad_model = tf.keras.models.Model(
    inputs=efficientnet.input,
    outputs=top_conv_layer.output
)


def make_gradcam_heatmap(img_array, predicted_class):

    with tf.GradientTape() as tape:

        conv_outputs = grad_model(
            img_array,
            training=False
        )

        pooled_features = tf.reduce_mean(
            conv_outputs,
            axis=(1, 2)
        )

        logits = tf.matmul(
            pooled_features,
            dense_layer.kernel
        ) + dense_layer.bias

        class_logit = logits[:, predicted_class]

    gradients = tape.gradient(
        class_logit,
        conv_outputs
    )

    if gradients is None:
        raise RuntimeError(
            "Gradients are None. "
            "Grad-CAM graph is not connected."
        )

    pooled_gradients = tf.reduce_mean(
        gradients,
        axis=(0, 1, 2)
    )

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(
        conv_outputs * pooled_gradients,
        axis=-1
    )

    heatmap = tf.maximum(
        heatmap,
        0
    )

    max_value = tf.reduce_max(heatmap)

    heatmap = heatmap / (
        max_value +
        tf.keras.backend.epsilon()
    )

    return heatmap.numpy()