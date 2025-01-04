import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

# Load the cleaned dataset
file_path = "factory_types.csv"  # Ensure this file is in the same directory
df = pd.read_csv(file_path)

# Clean the data
df = df.dropna(subset=['ประเภทหรือชนิดของโรงงาน'])  # Drop rows with NaN in the key column
df = df[~df['ประเภท โรงงานหลัก'].str.contains('ประเภท โรงงานหลัก', na=False)]
df['ประเภทหรือชนิดของโรงงาน'] = df['ประเภทหรือชนิดของโรงงาน'].str.strip()
df = df.reset_index(drop=True)

# Inject custom CSS for design
st.markdown(
    """
    <style>
    /* General styling */
    body {
        background: linear-gradient(to bottom right, #D2E0ED, #5884E7);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #0B1957; /* Deep Penn Blue */
    }

    /* Title styling */
    .stMarkdown h1 {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        color: #141031; /* Dark Blue */
        background-color: #FFBE98; /* Peach Fuzz */
        border-radius: 10px;
        padding: 10px 20px;
        margin: 20px auto;
        width: 80%;
    }

    /* Dropdown styling */
    .stSelectbox {
        border: 2px solid #0B1957; /* Penn Blue */
        background-color: #FFFFFF;
        color: #0B1957;
        font-size: 1.2rem;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    /* Enhanced table styling */
    table {
        width: 80%;
        margin: 10px auto;
        border-collapse: collapse;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    th {
        background-color: #5884E7; /* Azure */
        color: #FFFFFF;
        padding: 12px;
        text-transform: uppercase;
    }
    td {
        background-color: #D2E0ED; /* Columbia Blue */
        color: #141031; /* Dark Blue */
        padding: 12px;
        text-align: center;
        border-bottom: 1px solid #5884E7;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App UI
st.title("Factory-Classification-Type-1-2-3")
st.write("Please select your factory type:")

# Dropdown for selection
choices = df["ประเภทหรือชนิดของโรงงาน"].tolist()
selected_choice = st.selectbox("เลือกประเภทหรือชนิดของโรงงาน", options=choices)

# Display specific columns from matching row
if selected_choice:
    matching_row = df[df["ประเภทหรือชนิดของโรงงาน"] == selected_choice]
    selected_columns = matching_row[["โรงงานจำพวกที่ 1", "โรงงานจำพวกที่ 2", "โรงงานจำพวกที่ 3"]]
    
    st.write("ผลลัพธ์ที่ค้นพบ:")
    st.table(selected_columns)