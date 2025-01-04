import streamlit as st

# Function for Page 1
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    if st.button("Go Back"):
        st.session_state["page"] = "main"

# Main App Function
def main():
    st.title("ตรวจสอบการเข้าหลักเกณฑ์")

    st.write("ประเภทโรงงานของคุณ :")
    st.write("ต้องการตรวจสอบประเภทโรงงานของคุณอีกครั้ง หรือไม่")

    # Navigation buttons
    if st.button("Go to Page 1"):
        st.session_state["page"] = "page1"

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# Navigation logic
if st.session_state["page"] == "main":
    main()
elif st.session_state["page"] == "page1":
    page1()