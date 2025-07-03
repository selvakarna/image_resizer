import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Image Resizer", layout="centered")

st.title("📷 Upload & Resize Your Image")
uploaded = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Original Image", use_column_width=True)

    w = st.number_input("Width", value=image.width)
    h = st.number_input("Height", value=image.height)

    resized = image.resize((int(w), int(h)))
    st.image(resized, caption="Resized Image", use_column_width=True)

    format_option = st.selectbox("Download Format", ["JPG", "PNG", "PDF"])
    
    if st.button("Download"):
        buffer = io.BytesIO()
        ext = format_option.lower()
        if ext == "jpg":
            resized.save(buffer, format="JPEG")
        elif ext == "png":
            resized.save(buffer, format="PNG")
        elif ext == "pdf":
            resized.convert("RGB").save(buffer, format="PDF")
        st.download_button(f"Download {format_option}", buffer.getvalue(), file_name=f"resized.{ext}")
