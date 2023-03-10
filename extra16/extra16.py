# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
#Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:

# Create a pillow image instance
   img = Image.open(camera_image)

# Convert the pillow image to gratscale
   gray_img = img.convert("L")

# Render the grayscale image on the webpage
   st.image(gray_img)