# 🛠️ Import necessary libraries
import streamlit as st
import os
from io import BytesIO
from PIL import Image

# 🎨 Set up page configuration
st.set_page_config(page_title="PNG TO OTHERS", page_icon="♥️", layout='wide')

# 🏷️ Title & Description
st.title("♥️ PNG TO OTHER FORMAT")
st.write("🔄 Convert your image to another format instantly!")

# 📤 File Upload
file = st.file_uploader("📂 Upload your Image", type=["png", "jpg", "jpeg", "webp", "bmp", "tiff"])

if file is not None:
    st.success("✅ File uploaded successfully!")
    st.write("**Filename:**", file.name)
    
    # 🖼️ Load the image
    image = Image.open(file)

    # 🎯 Select output format
    output_format = st.selectbox("🎨 Choose output format:", ["png", "jpg", "jpeg", "webp", "bmp", "tiff"])

    # 🔘 Convert button
    if st.button("🚀 Convert Now"):
        buffer = BytesIO()
        format_map = {"jpg": "JPEG", "jpeg": "JPEG"}
        save_format = format_map.get(output_format.lower(), output_format.upper())

        image.save(buffer, format=save_format)
        buffer.seek(0)

        output_name = os.path.splitext(file.name)[0] + "." + output_format
        st.download_button(
            label="📥 Download Converted Image",
            data=buffer,
            file_name=output_name,
            mime=f"image/{'jpeg' if output_format in ['jpg', 'jpeg'] else output_format}"
        )
st.markdown("This app is created by XpertSphere")