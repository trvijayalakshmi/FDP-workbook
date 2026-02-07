import streamlit as st
import pandas as pd

data = st.file_uploader("Upload csv files")
if data is not None:
    st.success("File Uploaded")
    df = pd.read_csv(data)
    st.dataframe(df)
if st.button('BarChart'):
    st.bar_chart(df,x='ProductName',y='TotalSales')

