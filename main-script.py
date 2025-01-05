import streamlit as st
import hashlib
from Prototype.Home import app as home_app
from Prototype.Classification import app as classification_app
#from Prototype.If_Know_Check_Again import app as if_know_check_again_app
from login import app as login_app
# Set page configuration at the very top
st.set_page_config(
    page_title="Factolawies Dashboard",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add all apps to the dictionary
PAGES = {
    "Home": home_app,
    "ตรวจสอบประเภทโรงงานของคุณ": classification_app,
    #"ตรวจสอบการเข้าหลักเกณฑ์": if_know_check_again_app,
    "login/register": login_app
}

# Initialize the session state for the current page
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Navigation function to update the session state
def set_page(page_name):
    st.session_state["current_page"] = page_name

# Main function
def main():
    
    # Custom CSS 
    st.markdown("""
        <style>
        .main {
        background-color: #f7f7f9;
        font-family: 'Arial', sans-serif;
        }  
        body {
            background-color: #D2E0ED; /* Columbia Blue for the background */
            color: #141031; /* Dark Blue for text */
            font-family: 'Arial', sans-serif; /* Professional font */
        }
        .css-18e3th9 {
            background-color: #FFBE98; /* Peach Fuzz for main content */
            border-radius: 10px;
            padding: 10px;
        }
        .css-1d391kg {
            background-color: #D2E0ED; /* Columbia Blue for sidebar */
            border-right: 2px solid #5884E7; /* Subtle border */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #5884E7; /* Azure for headers */
        }
        .stButton button {
            background-color: #5884E7; /* Azure for buttons */
            color: white;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            padding: 8px 16px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #0B1957; /* Penn Blue for hover effect */
        }
        .stSelectbox, .stRadio, .stDateInput {
            background-color: #FFBE98; /* Peach Fuzz for form elements */
            border: 1px solid #5884E7;
            border-radius: 5px;
            color: #141031; /* Dark Blue for text */
        }
        hr {
            border: 1px solid #5884E7;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Display navigation buttons at the top of the page
    col1, col2, col4 = st.columns(3)
    with col1:
        if st.button("Home"):
            set_page("Home")
    with col2:
        if st.button("ตรวจสอบประเภทโรงงานของคุณ"):
            set_page("ตรวจสอบประเภทโรงงานของคุณ")
    #with col3:
    #    if st.button("ตรวจสอบการเข้าหลักเกณฑ์"):
    #        set_page("ตรวจสอบการเข้าหลักเกณฑ์")
    with col4:
        if st.button("Register/Login"):
            set_page("ตรวจสอบการเข้าหลักเกณฑ์")

    # Render the selected page
    PAGES[st.session_state["current_page"]]()

    # Footer
    st.markdown("""
        <hr>
        <footer>
        <p style="text-align: center; color: #1565c0;">
        © 2024 ChulaLegalTech-6 | Team Factolawies | Powered by Streamlit
        </p>
        </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

