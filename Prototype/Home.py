import streamlit as st
from PIL import Image

def app():
     # Title: Main
    st.title("Welcome to Factolawies~")

        # Load the image
    #image_path = "/Users/pannawatwhangvisith/Desktop/Coding_Project/LegalTecheiei/logo.png"  # Replace with your image path
    #image = Image.open(image_path)

    # Display the image
    #st.image(image, caption="", use_column_width=True)

    # Title: About Us
    st.title("🧑‍💼 About Us")

#    ### Our Team

#    We are a **diverse group** of individuals with complementary expertise:

#    - **Two Law Students**:  
#  Experts in the legal domain with a deep understanding of law and justice.
  
#   - **Three Business Students**:  
#  Equipped with extensive experience in case competitions and a solid foundation in business strategy and development.
  
#    - **One Computer Engineering Student**:  
#  Specializes in technology and software development, currently undertaking an internship as a full-stack developer.


    st.markdown("""
    ### **Our Mission**
    Despite coming from different academic backgrounds, we share a common goal:

    - To **integrate technology** into the legal field.
    - To enhance the **efficiency and effectiveness** of the justice system.

    Together, we aim to bridge the gap between **technology and law**, creating innovative solutions to transform and modernize the legal industry.
    """)

    # Sample Content
    #st.subheader("Main Content Section")
    #st.text("This is a placeholder for your main content.")
    #st.button("Click Me")




