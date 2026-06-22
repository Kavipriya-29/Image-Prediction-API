import streamlit as st
from PIL import Image
import numpy as np

st.title("🖼️ Image Prediction API")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    width, height = image.size

    if width > height:
        prediction = "Landscape Image"
    elif height > width:
        prediction = "Portrait Image"
    else:
        prediction = "Square Image"

    st.success(f"Prediction: {prediction}")