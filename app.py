# app.py

import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO

st.set_page_config(page_title="Image to PDF Converter", layout="centered")

st.title("🖼️ Image to PDF Converter with Filters")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "bmp", "webp"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    st.subheader("Apply Filters")

    # Filter selection
    filter_option = st.selectbox(
        "Choose a filter",
        [
            "None",
            "Grayscale",
            "Blur",
            "Sharpen",
            "Edge Enhance"
        ]
    )

    # Brightness and contrast sliders
    brightness = st.slider(
        "Brightness",
        min_value=0.5,
        max_value=2.0,
        value=1.0,
        step=0.1
    )

    contrast = st.slider(
        "Contrast",
        min_value=0.5,
        max_value=2.0,
        value=1.0,
        step=0.1
    )

    processed_image = image.copy()

    # Apply selected filter
    if filter_option == "Grayscale":
        processed_image = processed_image.convert("L")

    elif filter_option == "Blur":
        processed_image = processed_image.filter(ImageFilter.BLUR)

    elif filter_option == "Sharpen":
        processed_image = processed_image.filter(ImageFilter.SHARPEN)

    elif filter_option == "Edge Enhance":
        processed_image = processed_image.filter(ImageFilter.EDGE_ENHANCE)

    # Apply brightness
    enhancer = ImageEnhance.Brightness(processed_image)
    processed_image = enhancer.enhance(brightness)

    # Apply contrast
    enhancer = ImageEnhance.Contrast(processed_image)
    processed_image = enhancer.enhance(contrast)

    st.subheader("Filtered Image Preview")
    st.image(processed_image, use_container_width=True)

    if st.button("Convert to PDF"):

        # Convert to RGB for PDF compatibility
        if processed_image.mode != "RGB":
            processed_image = processed_image.convert("RGB")

        pdf_buffer = BytesIO()

        processed_image.save(pdf_buffer, format="PDF")

        pdf_buffer.seek(0)

        st.success("PDF created successfully!")

        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_buffer,
            file_name="filtered_image.pdf",
            mime="application/pdf"
        )
