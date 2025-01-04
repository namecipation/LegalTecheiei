import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

def app():
    # Load the cleaned dataset
    file_path = "factory_types.csv"  # Ensure this file is in the same directory
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        st.error("The file 'factory_types.csv' was not found. Please ensure it is in the correct directory.")
        return

    # Clean the data
    df = df.dropna(subset=['ประเภทหรือชนิดของโรงงาน'])  # Drop rows with NaN in the key column
    df = df[~df['ประเภท โรงงานหลัก'].str.contains('ประเภท โรงงานหลัก', na=False)]
    df['ประเภทหรือชนิดของโรงงาน'] = df['ประเภทหรือชนิดของโรงงาน'].str.strip()
    df = df.reset_index(drop=True)

    # Inject custom CSS for enhanced styling
    st.markdown(
        """
        <style>
        /* General background with gradient */
        body {
            background: linear-gradient(to bottom right, #D2E0ED, #5884E7);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #0B1957; /* Deep Penn Blue */
        }

        /* Styling the title */
        .stMarkdown h1 {
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
            color: #141031; /* Dark Blue */
            background-color: #FFBE98; /* Peach Fuzz */
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
        }

        /* Dropdown styling */
        .stSelectbox {
            border: 2px solid #0B1957; /* Penn Blue */
            background-color: #FFFFFF;
            color: #0B1957; /* Penn Blue */
            font-size: 1.1rem;
            padding: 8px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        /* Enhanced table styling */
        table {
            margin: 20px auto;
            border-collapse: collapse;
            width: 90%;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        th {
            background-color: #5884E7; /* Azure for table header */
            color: #FFFFFF; /* White text */
            padding: 12px;
            text-align: center;
            text-transform: uppercase;
        }
        td {
            background-color: #D2E0ED; /* Columbia Blue for table rows */
            color: #141031; /* Dark Blue for text */
            padding: 12px;
            text-align: center;
            border-bottom: 1px solid #5884E7;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Streamlit App UI
    st.title("🏭 Factory Classification: Types 1, 2, 3")
    st.write("Select a factory type to explore classifications:")

    # Dropdown for factory selection
    choices = df["ประเภทหรือชนิดของโรงงาน"].tolist()
    selected_choice = st.selectbox("เลือกประเภทหรือชนิดของโรงงาน", options=choices)

    # Display selected data
    if selected_choice:
        matching_row = df[df["ประเภทหรือชนิดของโรงงาน"] == selected_choice]
        selected_columns = matching_row[["โรงงานจำพวกที่ 1", "โรงงานจำพวกที่ 2", "โรงงานจำพวกที่ 3"]]
        st.subheader("ผลลัพธ์ที่ค้นพบ:") 
        st.table(selected_columns)
    
    