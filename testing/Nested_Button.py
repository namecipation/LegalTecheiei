import streamlit as st

# Main button
if st.button("Main Button"):
    st.write("Main button clicked!")
    
    # Nested button logic
    if st.button("Nested Button 1"):
        st.write("Nested Button 1 clicked!")
    
    if st.button("Nested Button 2"):
        st.write("Nested Button 2 clicked!")

    # You can also have conditional logic for different levels
    if st.button("Another Nested Button"):
        st.write("Another action can be triggered here!")