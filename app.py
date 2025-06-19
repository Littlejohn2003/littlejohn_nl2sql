
import streamlit as st
from littlejohn_bot import nl2sql

# Page setup
st.set_page_config(page_title="NL2SQL Bot", layout="centered")
st.title("Natural Language to SQL Translator")

# Input field
query = st.text_input("Enter your question in natural language:")

# SQL generation when user clicks on the button
if st.button("Generate SQL"):
    if query.strip(): #Ensure query is not empty
        with st.spinner("Generating SQL..."):
            try:
                sql = nl2sql(query) #Core function that generates SQL
                st.success("SQL Query Generated:")
                st.code(sql, language="sql")
            except Exception as e:
                st.error(f"An error occurred: {e}") #Handle runtime errors
    else:
        st.warning("Please enter a natural language query.") #Handle empty input
