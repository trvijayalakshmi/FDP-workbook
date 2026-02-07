import streamlit as st
import sqlite3
conn = sqlite3.connect('contact.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS contact(name TEXT,mobile INTEGER,email TEXT)')
conn.commit()
cur.close()

name = st.text_input('Enter Your Name')
mobile = st.number_input('Enter your Mobile')
email = st.text_input("Enter your Email Id")
if st.button('Save'):
    cur = conn.cursor()
    cur.execute('INSERT INTO contact(name,mobile,email)VALUES(?,?,?)',(name,mobile,email))
    conn.commit()
    cur.close()
    st.success("Data Saved")

if st.button('Display'):
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM contact')
    st.dataframe(data)
    cur.close()