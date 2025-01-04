import streamlit as st

# Set the title and sidebar
st.set_page_config(page_title="My Homepage", page_icon=":house:", layout="wide")

# Main title and subtitle
st.title("Welcome to My Homepage! :house_with_garden:")
st.subheader("A place to explore and learn about my projects and interests.")

# Add an introduction section
st.markdown("""
### About Me
Hi there! 👋 I'm a passionate developer and learner interested in IoT, AI, and fintech solutions. This homepage showcases my projects, skills, and experiences. Feel free to explore!
""")

# Add columns for layout
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/150", caption="Project 1", use_column_width=True)
    st.markdown("**Project 1**: Smart Bin System")
    st.button("Learn More", key="project1")

with col2:
    st.image("https://via.placeholder.com/150", caption="Project 2", use_column_width=True)
    st.markdown("**Project 2**: ClickCare App")
    st.button("Learn More", key="project2")

with col3:
    st.image("https://via.placeholder.com/150", caption="Project 3", use_column_width=True)
    st.markdown("**Project 3**: IoT Mini SmartFarm")
    st.button("Learn More", key="project3")

# Add a contact section
st.markdown("""
---
### Contact Me
📧 Email: [your_email@example.com](mailto:your_email@example.com)  
🌐 GitHub: [github.com/yourusername](https://github.com/yourusername)  
💼 LinkedIn: [linkedin.com/in/yourusername](https://linkedin.com/in/yourusername)
""")

# Footer
st.markdown("""
---
Thank you for visiting! 😊
""")