import streamlit as st
from PIL import Image

# Title for the web app
st.title("Image Display Example")

# Load the image
image_path = "/Users/pannawatwhangvisith/Desktop/Coding_Project/LegalTecheiei/logo.png"  # Replace with your image path
image = Image.open(image_path)

# Display the image
st.image(image, caption="", use_column_width=True)
# You can also display images from a URL
#image_url = "https://via.placeholder.com/150"
#st.image(image_url, caption="Image from URL", use_column_width=True)