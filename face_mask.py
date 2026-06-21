import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("Face_mask.keras")

st.title("😷 Face Mask Detection")
st.write("Upload an image to detect whether a person is wearing a mask.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png","WEBP"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    img = image.resize((128,128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    if prediction[0][0] > 0.5:
        st.error("Mask Detected")
    else:
        st.success(" No Mask Detected")