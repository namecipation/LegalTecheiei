import streamlit as st

def app():
    st.title("ตรวจสอบการเข้าหลักเกณฑ์")

    st.write('ประเภทโรงงานของคุณ :')
    st.write('ต้องการตรวจสอบประเภทโรงงานของคุณอีกครั้ง หรือไม่')

    # Button for navigation
    # Navigation buttons
    if st.button("Go to Page 1"):
        st.session_state["page"] = "page1"

    if "page" in st.session_state:
        if st.session_state["page"] == "page1":
            st.write("Welcome to Page 1!")


