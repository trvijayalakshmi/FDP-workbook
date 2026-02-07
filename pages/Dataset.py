import streamlit as st
import pandas as pd

# df = pd.read_csv("salesdata.csv")
df = pd.read_csv('salesdata.csv')
st.dataframe(df)
