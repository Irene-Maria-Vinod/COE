# app.py

import streamlit as st
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image to PDF Converter")

st.title("🖼️ Image to PDF Converter")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "bmp", "webp"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Convert to PDF"):
        # Convert image to RGB (required for PDF)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        pdf_buffer = BytesIO()

        # Save image as PDF
        image.save(pdf_buffer, format="PDF")

        pdf_buffer.seek(0)

        st.success("PDF created successfully!")

        st.download_button(
            label="⬇️ Download PDF",
            data=pdf_buffer,
            file_name="converted_image.pdf",
            mime="application/pdf"
        )
