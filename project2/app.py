import streamlit as st
import pandas as pd
st.title("Student's Placement Data")
data = st.file_uploader("Upload your file here", type=["csv"])
if data is not None:
    st.success("File uploaded successfully!")
    df = pd.read_csv(data)
    st.dataframe(df)
